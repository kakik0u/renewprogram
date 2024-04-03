from collections import UserDict
import os
import discord
from discord import app_commands, user
from discord.ext import commands
from discord import app_commands as apc
import pickle
from discord.ui import Select, View
from file import loadtxt,loadjson,savejson,savetxt
import renewsm
import renewmd

TOKEN ="とくーん"

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync()
    print("起動したンゴねぇ")
   



@client.event
async def on_interaction(inter:discord.Interaction):
    try:
        if inter.data['component_type'] == 2:
            await on_button_click(inter)
    except KeyError:
        pass
async def on_button_click(inter:discord.Interaction):
  guild = client.get_guild(1197124328525942784)
  custom_id = inter.data["custom_id"]
  if custom_id=="gradeup":
    server = inter.guild
    await inter.response.send_message("Loading...",ephemeral=True)
    category_channel = client.get_channel(1223982998937010327)
    overwrites = {
        server.default_role: discord.PermissionOverwrite(read_messages=False),
        server.me: discord.PermissionOverwrite(read_messages=True),
        inter.user: discord.PermissionOverwrite(read_messages=True)
    }
    channel_name = f"更新-{inter.user.name}"
    channel = await server.create_text_channel(name=channel_name, overwrites=overwrites,category =category_channel)
    gradeselectv=renewsm.gradeselect()
    classselectv=renewsm.classselect()
    numberv=renewsm.numberselect1()
    number2v=renewsm.numberselect2()
    await channel.send("クラス,番号を選択してください\n例:高校2年9組2番の人は学年に５、クラスに９、番号１に０、番号２に９を選択してください")
    await channel.send(view=gradeselectv)
    await channel.send(view=classselectv)
    await channel.send(view=numberv)
    await channel.send(view=number2v)

    ticket_message = f"更新が作成されました！\n{channel.mention}"
    cachejson={}
    savejson(f"./renew/{inter.user.id}.json",cachejson)
    await inter.followup.send(ticket_message, ephemeral=True)
    #ticket2_owners[channel.id] = inter.user.id

"""
@client.event
async def on_message(message):
    button = discord.ui.Button(label="学年情報更新",style=discord.ButtonStyle.success,custom_id="gradeup")
    view = discord.ui.View()
    view.add_item(button)
    await message.channel.send("下のボタンを押して開始してください",view=view)
"""


client.run(TOKEN)
