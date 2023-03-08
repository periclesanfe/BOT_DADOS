import random

import discord
from discord import app_commands

id_do_servidor = 'id_do_servidor'


class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        # Nós usamos isso para o bot não sincronizar os comandos mais de uma vez
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced:  # Checar se os comandos slash foram sincronizados
            # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            await tree.sync(guild=discord.Object(id=id_do_servidor))
            self.synced = True
        print(f"Entramos como {self.user}.")


aclient = client()
tree = app_commands.CommandTree(aclient)

# TESTE


# Comando específico para seu servidor
@tree.command(guild=discord.Object(id=id_do_servidor), name='teste', description='Testando')
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Estou funcionando!", ephemeral=False)
# D6


# Comando específico para seu servidor
@tree.command(guild=discord.Object(id=id_do_servidor), name='d6', description='Roda um dado de 6 lados')
async def slash3(interaction: discord.Interaction):
    numero = random.randint(1, 6)
    await interaction.response.send_message(f"{numero}", ephemeral=False)
# D8


# Comando específico para seu servidor
@tree.command(guild=discord.Object(id=id_do_servidor), name='d8', description='Roda um dado de 8 lados')
async def slash3(interaction: discord.Interaction):
    numero = random.randint(1, 8)
    await interaction.response.send_message(f"{numero}", ephemeral=False)
# D10


# Comando específico para seu servidor
@tree.command(guild=discord.Object(id=id_do_servidor), name='d10', description='Roda um dado de 10 lados')
async def slash4(interaction: discord.Interaction):
    numero = random.randint(1, 10)
    await interaction.response.send_message(f"{numero}", ephemeral=False)
# D12


# Comando específico para seu servidor
@tree.command(guild=discord.Object(id=id_do_servidor), name='d12', description='Roda um dado de 12 lados')
async def slash3(interaction: discord.Interaction):
    numero = random.randint(1, 12)
    await interaction.response.send_message(f"{numero}", ephemeral=False)
# D20


# Comando específico para seu servidor
@tree.command(guild=discord.Object(id=id_do_servidor), name='d20', description='Roda um dado de 20 lados')
async def slash3(interaction: discord.Interaction):
    numero = random.randint(1, 20)
    if numero >= 15:
        numero = random.randint(1, 20)
    await interaction.response.send_message(f"{numero}", ephemeral=False)


aclient.run(
    'bot_key')
