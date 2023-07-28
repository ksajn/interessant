import discord
from discord import app_commands
from discord.ext import commands

class guild(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name = "guild", description = "sends info about the guild")
    async def guild(self, interaction: discord.Interaction):
        guild = interaction.guild
        embed = discord.Embed(
            title = guild.name,
            color=0x2b2d31
        )
        if interaction.guild.icon:
            embed.set_thumbnail(url=interaction.guild.icon.url)
        if interaction.guild.banner:
            embed.set_image(url=interaction.guild.banner.url)
        
        embed.add_field(name = "server name:", value = f"{guild.name}", inline = False)
        embed.add_field(name = "role count:", value = f"{len(guild.roles)}", inline = False)
        embed.add_field(name = "emoji count:", value = f"{len(guild.emojis)}", inline = False)
        embed.add_field(name = "owner:", value = f"<@{interaction.guild.owner_id}>", inline = False)
        embed.add_field(name = "guild created:", value = f"<t:{int(interaction.guild.created_at.timestamp())}:R>", inline = False)
        embed.add_field(name = "members:", value = interaction.guild.member_count, inline = False),
        embed.add_field(name = "server id:", value = interaction.guild.id, inline = False)
        if len(interaction.guild.features) > 0:
            features = ""
            for feature in interaction.guild.features:
                features = f"{features}\n{feature.lower().replace('_', ' ')}"
            embed.add_field(name = "guild features:", value = features, inline = False)
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(guild(bot))