import html
import re
import requests

API_URL = "https://duelmasters.fandom.com/api.php"

def parse_cardtable(content):
     fields = {}

     current_field = None

     for line in content.splitlines():
         # Stop when we reach the end of the Cardtable
         if line.strip() == "}}":
             break

         # Check whether this line starts a new Cardtable field
         match = re.match(r"^\|\s*([^=]+?)\s*=\s*(.*)$", line)

         if match:
             current_field = match.group(1).strip()
             fields[current_field] = match.group(2).strip()

         elif current_field:
             # This is a continuation of the previous field
             fields[current_field] += "\n" + line.strip()

     return fields

def clean_wiki_text(text):
    if not text:
        return None

    # Remove category links
    text = re.sub(
        r"\[\[Category:[^\]]+\]\]",
        "",
        text,
        flags=re.IGNORECASE
    )

    # Convert [[Page|Displayed Text]] -> Displayed Text
    text = re.sub(
        r"\[\[([^|\]]+)\|([^\]]+)\]\]",
        r"\2",
        text
    )

    # Convert [[Page]] -> Page
    text = re.sub(
        r"\[\[([^\]]+)\]\]",
        r"\1",
        text
    )

    # Convert wiki bold to Discord bold (priority over italics to prevent potential conflicts)
    text = re.sub(
        r"'''(.*?)'''",
        r"**\1**",
        text
    )

    # Convert wiki italics to Discord italics
    text = re.sub(
        r"''(.*?)''",
        r"*\1*",
        text
    )

    # Decode HTML entities such as &#8203;
    text = html.unescape(text)

    # Remove zero-width spaces
    text = text.replace("\u200b", "")

    # Remove HTML tags
    text = re.sub(r"<[^>]+>", "", text)

    # Clean up whitespace around blank lines
    text = re.sub(r"\n\s*\n", "\n\n", text)

    return text.strip()

def expand_wiki_text(text, page_title=None):
    if not text:
        return None

    params = {
        "action": "expandtemplates",
        "format": "json",
        "prop": "wikitext",
        "text": text
    }

    if page_title:
        params["title"] = page_title

    response = requests.get(API_URL, params=params)
    response.raise_for_status()

    data = response.json()

    return data["expandtemplates"]["wikitext"]

def get_card(card_name):
    params = {
        "action": "query",
        "format": "json",
        "titles": card_name,
        "prop": "revisions|info|pageimages",
        "inprop": "url",
        "piprop": "original",
        "rvprop": "content",
        "rvslots": "main"
    }

    response = requests.get(API_URL, params=params)
    response.raise_for_status()

    data = response.json()

    pages = data["query"]["pages"]
    page = next(iter(pages.values()))

    if "missing" in page:
        return None

    # Get the raw wiki markup
    content = page["revisions"][0]["slots"]["main"]["*"]

    # Parse the Cardtable
    cardtable = parse_cardtable(content)

    raw_effect = cardtable.get("engtext")

    print("\n============= RAW EFFECT =============")
    print(raw_effect)

    # Template expand the raw effect
    formatted_effect = expand_wiki_text(raw_effect, page["title"])

    print("\n============= FORMATTED EFFECT =============")
    print(formatted_effect)

    # Remove remaining redundant formatting
    cleaned_effect = clean_wiki_text(formatted_effect)

    print("\n============= CLEANED EFFECT =============")
    print(cleaned_effect)

    print("\n==========================\n")

    card = {
        "name": page["title"],
        "url": page["fullurl"],
        "image": page.get("original", {}).get("source"),
        **cardtable,
        "effect": cleaned_effect,
    }

    return card

if __name__ == "__main__":
    card = get_card("Crystal Lancer")
    print(card)
