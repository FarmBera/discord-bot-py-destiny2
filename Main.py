import requests
import json, csv
from datetime import datetime, timedelta

import discord
from discord.ext import tasks
from discord import app_commands  # , Interaction

from TOKEN import TOKEN_API as TOKEN

log_file_path = "logfile.csv"


def send_log(cmd, time, user, guild, channel):
    log_f = open(log_file_path, "a", encoding="UTF-8", newline="")
    # time = (time).strftime("%Y-%m-%d %H:%M:%S") # for KR Timezone
    time = (time + timedelta(hours=9)).strftime("%Y-%m-%d %H:%M:%S")  # for US Timezone
    wr = csv.writer(log_f)
    wr.writerow([user, time, cmd, guild, channel])
    log_f.close()


class MyClient(discord.Client):
    async def on_ready(self):
        await self.wait_until_ready()
        # await tree.sync()
        await self.change_presence(
            status=discord.Status.online, activity=discord.Game("Ready!")
        )
        # self.auto_send.start()
        print(f"Logged on as {self.user}!")

    # Auto Check New LostArk Notice
    # @tasks.loop(minutes=5.0)
    # async def auto_send(self):

    # on Message imcoming
    # async def on_message(self, message):
    # trim_text = message.content.replace(" ", "")

    # if message.author == self.user: return


# Execute Discord Bot
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
tree = app_commands.CommandTree(client)

client.run(TOKEN)
