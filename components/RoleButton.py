import discord
from utils import handle_role_toggle

class RoleButton(discord.ui.Button):
    def __init__(self, label, role_id, apply_text, remove_text):
        self.role_id = role_id
        self.apply_text = apply_text
        self.remove_text = remove_text
        super().__init__(
            label=label,
            style=discord.ButtonStyle.secondary,
            custom_id=f"role_{role_id}",
        )

    async def callback(self, interaction: discord.Interaction):
        await handle_role_toggle(
            interaction,
            self.role_id,
            self.apply_text,
            self.remove_text
        )