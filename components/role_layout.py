import discord
from .role_button import RoleButton


class RoleLayout(discord.ui.LayoutView):
    def __init__(
        self,
        title: str,
        description: str,
        role_data: list[tuple[str, int]],
        subtitle: str | None = None,
    ):
        super().__init__()

        components = [
            discord.ui.TextDisplay(content=title),
        ]

        # optional subtitle
        if subtitle is not None:
            components.append(
                discord.ui.TextDisplay(content=subtitle)
            )

        components.append(
            discord.ui.TextDisplay(content=description)
        )

        components.extend(
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
        )

        container = discord.ui.Container(*components)
        self.add_item(container)