import discord
from discord import app_commands
from discord.ext import commands
from functions import embedColor
import sqlite3

class create(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='create', description = 'This command is for nitro booster and works only on specified servers.')
    async def create(self, interaction: discord.Interaction, name: str, color: int):
        serverlist = [
            1006924123781472336,
        ]
        finalRoleList = []
        if interaction.guild.id in serverlist:
            if interaction.guild.id == 1006924123781472336: # Strefa Zainteresowan
                roleCount = len(interaction.user.roles)
                for i in range(roleCount):
                    finalRoleList.append(str(interaction.user.roles[i]).lower())
                    
                def isNitroBooster():
                    if '🔧' in finalRoleList:
                        return True
                                                    
                    else:
                        return False
                    
                if isNitroBooster():
                    try:
                            
                            

                            db = sqlite3.connect('db.db')
                            cursor = db.cursor()
                            cursor.execute(f'SELECT user_id FROM nitroboost WHERE user_id = {interaction.user.id}')
                            result = cursor.fetchone()
                            if result == None:
                                rola = await interaction.guild.create_role(name=name, color=color)
                                finalId = rola.id
                                print()
                                finalUserId = interaction.user.id
                                await interaction.user.add_roles(rola)
                                cursor.execute(f'INSERT INTO nitroboost(user_id, role_id, color, name) VALUES({interaction.user.id}, {finalId}, {color}, {name})')

                                await interaction.response.send_message('you successfully created your nitro booster role! \n role name: {name} \n role color: {color} \n role id: {finalId}')

                            
                            else:
                                await interaction.response.send_message('you have already created nitro booster role in this server')
                            cursor.close()
                            db.commit()
                            db.close()

                    except Exception as e:
                        print(e)
                else:
                    pass
    
        else:
            embed = discord.Embed(
                title='interessant',
                description='this server is not specified in list',
                color=embedColor()
            )
            
            await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(create(bot))