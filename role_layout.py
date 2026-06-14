import discord

from config import VERDANT_ROLE_ID, CRIMSON_FLAME_ROLE_ID, VOID_ROLE_ID, CELESTIAL_ROLE_ID
from components.role_button import RoleButton

class RoleLayout(discord.ui.LayoutView):    
    container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="**Choose Your Color Role**"),
        discord.ui.TextDisplay(content="All Oath members can claim one of these base colors to make your name stand out:"),
        discord.ui.Section(
            discord.ui.TextDisplay(content=f"<@&{VERDANT_ROLE_ID}>"),
            accessory=RoleButton(
                label="🌱 Verdant",
                role_id=VERDANT_ROLE_ID,
                apply_text=f":white_check_mark: Added role <@&{VERDANT_ROLE_ID}>",
                remove_text=f":negative_squared_cross_mark: Removed role <@&{VERDANT_ROLE_ID}>",
            ),
        ),
        discord.ui.Section(
            discord.ui.TextDisplay(content=f"<@&{CRIMSON_FLAME_ROLE_ID}>"),
            accessory=RoleButton(
                label="🔥 Crimson Flame",
                role_id=CRIMSON_FLAME_ROLE_ID,
                apply_text=f":white_check_mark: Added role <@&{CRIMSON_FLAME_ROLE_ID}>",
                remove_text=f":negative_squared_cross_mark: Removed role <@&{CRIMSON_FLAME_ROLE_ID}>",
            ),
        ),
        discord.ui.Section(
            discord.ui.TextDisplay(content=f"<@&{VOID_ROLE_ID}>"),
            accessory=RoleButton(
                label="🌌 Void",
                role_id=VOID_ROLE_ID,
                apply_text=f":white_check_mark: Added role <@&{VOID_ROLE_ID}>",
                remove_text=f":negative_squared_cross_mark: Removed role <@&{VOID_ROLE_ID}>",
            ),
        ),
        discord.ui.Section(
            discord.ui.TextDisplay(content=f"<@&{CELESTIAL_ROLE_ID}>"),
            accessory=RoleButton(
                label="👼 Celestial",
                role_id=CELESTIAL_ROLE_ID,
                apply_text=f":white_check_mark: Added role <@&{CELESTIAL_ROLE_ID}>",
                remove_text=f":negative_squared_cross_mark: Removed role <@&{CELESTIAL_ROLE_ID}>",
            ),
        ),
    )