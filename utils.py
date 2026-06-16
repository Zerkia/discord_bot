import discord

from roles import COLOR_ROLE_DATA

async def handle_role_toggle(
    interaction: discord.Interaction,
    role_id: int,
    apply_text: str,
    remove_text: str,
):
    guild = interaction.guild
    user = interaction.user

    if guild is None or not isinstance(user, discord.Member):
        return

    target_role = guild.get_role(role_id)
    if target_role is None:
        await interaction.response.send_message(
            "Role configuration error. Please contact an admin.",
            ephemeral=True,
        )
        return

    COLOR_ROLE_IDS = [rid for _, rid in COLOR_ROLE_DATA]
    is_color_role = role_id in COLOR_ROLE_IDS

    if target_role in user.roles:
        await user.remove_roles(target_role)
        await interaction.response.send_message(remove_text, ephemeral=True)
        return

    if is_color_role:
        # Only allow one color role at a time
        roles_to_remove = [r for r in user.roles if r.id in COLOR_ROLE_IDS]
        if roles_to_remove:
            await user.remove_roles(*roles_to_remove)
            await user.add_roles(target_role)
            await interaction.response.send_message(
                f":arrows_counterclockwise: Changed role to {target_role.mention}",
                ephemeral=True,
            )
        else:
            await user.add_roles(target_role)
            await interaction.response.send_message(
                apply_text,
                ephemeral=True,
            )
        return
    else:
        # Non-color Roles: just add
        await user.add_roles(target_role)
        await interaction.response.send_message(apply_text, ephemeral=True)