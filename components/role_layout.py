import discord

from .role_button import RoleButton

class RoleLayout(discord.ui.LayoutView):
    def __init__(self, title: str, description: str, role_data: list[tuple[str, int]]):
        super().__init__()

        container = discord.ui.Container(
            discord.ui.TextDisplay(content=title),
            discord.ui.TextDisplay(content=description),
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
                for label, role_id in role_data
            ],
        )

        self.add_item(container)