import re
import requests

API_URL = "https://duelmasters.fandom.com/api.php"

def clean_wiki_text(text):
    if not text:
        return None

    # Convert known Duel Masters templates into their English equivalents
    template_replacements = {
        "{{Double Breaker}}": "■ Double Breaker *(This creature breaks 2 shields)*",
        "{{Triple Breaker}}": "■ Triple Breaker *(This creature breaks 3 shields)*",
        "{{Blocker}}": "■ Blocker",
        "{{Shield Trigger}}": "■ Shield Trigger",
        "{{Speed Attacker}}": "■ Speed Attacker",
        "{{Evolution}}": "■ Evolution",
    }

    for template, replacement in template_replacements.items():
        text = text.replace(template, replacement)

    # Convert [[Page|Displayed Text]] -> Displayed Text
    text = re.sub(r"\[\[([^|\]]+)\|([^\]]+)\]\]", r"\2", text)

    # Convert [[Page]] -> Page
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)

    # Remove simple templates such as {{Double Breaker}}
    text = re.sub(r"\{\{[^{}]+\}\}", "", text)

    # Clean up excessive whitespace
    text = re.sub(r"\n\s*\n", "\n\n", text)

    return text.strip()

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

    # Extract fields from the Cardtable
    def get_field(field):
        match = re.search(
            rf"\|\s*{re.escape(field)}\s*=\s*(.*)",
            content
        )

        if match:
            return match.group(1).strip()

        return None

    card = {
        "name": page["title"],
        "civilization": get_field("civilization"),
        "race": get_field("race"),
        "type": get_field("type"),
        "cost": get_field("cost"),
        "power": get_field("power"),
        # "effect": get_field("engtext")
        "effect": clean_wiki_text(get_field("engtext")),
        "image": page.get("original", {}).get("source"),
        "url": page["fullurl"],
    }

    return card


if __name__ == "__main__":
    card = get_card("Bolshack Dragon")
    print(card)
