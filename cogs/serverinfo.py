import discord
from discord import app_commands
from discord.ext import commands

class serverinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name = "serverinfo", description = "sends info about the server")
    async def serverinfo(self, interaction: discord.Interaction):
        guild = interaction.guild
        embed = discord.Embed(
            title = guild.name,
            color=0x2b2d31
        )
        if interaction.guild.icon.url:
            embed.set_thumbnail(url=interaction.guild.icon.url)
        if interaction.guild.banner.url:
            embed.set_image(url=interaction.guild.banner.url)
        embed.add_field(name = "owner:", value = f"<@{interaction.guild.owner_id}>", inline = False)
        embed.add_field(name = "server created:", value = f"<t:{int(interaction.guild.created_at.timestamp())}:R>", inline = False)
        embed.add_field(name = "members:", value = interaction.guild.member_count, inline = False),
        embed.add_field(name = "server id:", value = interaction.guild.id, inline = False)
        if len(interaction.guild.features) > 0:
            features = ""
            for feature in interaction.guild.features:
                features = f"{features}\n{feature.lower().replace('_', ' ')}"
            embed.add_field(name = "server features:", value = features, inline = False)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(serverinfo(bot))