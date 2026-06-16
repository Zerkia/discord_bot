import discord

from roles import COLOR_ROLE_DATA
from components.role_button import RoleButton

class ColorRolesLayout(discord.ui.LayoutView):
    container1 = discord.ui.Container(
        discord.ui.TextDisplay(content="**Choose Your Color Role**"),
        discord.ui.TextDisplay(
            content="All Oath members can claim one of these base colors to make your name stand out:"
        ),
        *[
            discord.ui.Section(
                discord.ui.TextDisplay(content=f"<@&{role_id}>"),
                accessory=RoleButton(
                    label=label,
                    role_id=role_id,
                    apply_text=f":white_check_mark: Added role <@&{role_id}>",
                    remove_text=f":negative_squared_cross_mark: Removed role <@&{role_id}>",
                ),
            )
            for label, role_id in COLOR_ROLE_DATA
        ],
    )