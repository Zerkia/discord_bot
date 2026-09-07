import discord


def create_card_embed(card):
    embed = discord.Embed(
        title=card["name"],
        url=card["url"],
        description=f'{card["type"]} • {card["civilization"]}',
    )

    # Card information
    embed.add_field(
        name="Cost",
        value=card["cost"] or "N/A",
        inline=True
    )

    embed.add_field(
        name="Race",
        value=card["race"] or "N/A",
        inline=True
    )

    embed.add_field(
        name="Power",
        value=card["power"] or "N/A",
        inline=True
    )

    if card.get("effect"):
        embed.add_field(
            name="Effect",
            value=card["effect"],
            inline=False
        )

    # Card image
    if card.get("image"):
        embed.set_image(url=card["image"])

    # Small attribution/source
    embed.set_footer(text="Duel Masters Wiki")

    return embed
