import discord
from discord import app_commands
from discord.ui import Select, View
from modal import mail
from file import savejson,savetxt,loadjson,loadtxt
import os

       

class gradeselect(View):
   @discord.ui.select(
       cls=Select,
       placeholder="学年",
       options=[
           discord.SelectOption(label="1年",value="1",description="中学1年生"),
           discord.SelectOption(label="2年",value="2",description="中学2年生"),
           discord.SelectOption(label="3年",value="3",description="中学3年生"),
           discord.SelectOption(label="4年",value="4",description="高校1年生"),
           discord.SelectOption(label="5年",value="5",description="高校2年生"),
           discord.SelectOption(label="6年",value="6",description="高校3年生"),
           discord.SelectOption(label="OB",value="OB",description="卒業生"),
       ]
   )
   async def gradeselect(self, interaction: discord.Interaction, select: Select):         
       select.disabled = True
       await interaction.response.edit_message(view=self)
       #await interaction.followup.send(f"{select.values}")
       #savetxt(f"./renew/{interaction.user.id}grade.txt",select.values[0])
       data = dict(loadjson(f"./renew/{interaction.user.id}.json"))
       key = "grade"
       data[key] = select.values[0]
       savejson(f"./renew/{interaction.user.id}.json",data)
       await codecheck(interaction)

class classselect(View):
   @discord.ui.select(
       cls=Select,
       placeholder="クラス",
       options=[
           discord.SelectOption(label="1組",value="1"),
           discord.SelectOption(label="2組",value="2"),
           discord.SelectOption(label="3組",value="3"),
           discord.SelectOption(label="4組",value="4"),
           discord.SelectOption(label="5組",value="5"),
           discord.SelectOption(label="6組",value="6"),
           discord.SelectOption(label="7組",value="7"),
           discord.SelectOption(label="8組",value="8"),
       ]
   )
   async def classselect(self, interaction: discord.Interaction, select: Select):         
       select.disabled = True
       await interaction.response.edit_message(view=self)
       #await interaction.followup.send(f"{select.values}")
       #savetxt(f"./renew/{interaction.user.id}class.txt",select.values[0])
       data = dict(loadjson(f"./renew/{interaction.user.id}.json"))
       key = "class"
       data[key] = select.values[0]
       savejson(f"./renew/{interaction.user.id}.json",data)
       await codecheck(interaction)

class numberselect1(View):
   @discord.ui.select(
       cls=Select,
       placeholder="番号1",
       options=[
           discord.SelectOption(label="0",value="0"),
           discord.SelectOption(label="1",value="1"),
           discord.SelectOption(label="2",value="2"),
           discord.SelectOption(label="3",value="3"),
           discord.SelectOption(label="4",value="4")
       ]
   )
   async def numberselect1(self, interaction: discord.Interaction, select: Select):         
       select.disabled = True
       await interaction.response.edit_message(view=self)
       #await interaction.followup.send(f"{select.values}")
       #savetxt(f"./renew/{interaction.user.id}code1.txt",select.values[0])
       data = dict(loadjson(f"./renew/{interaction.user.id}.json"))
       key = "code1"
       data[key] = select.values[0]
       savejson(f"./renew/{interaction.user.id}.json",data)
       await codecheck(interaction)

class numberselect2(View):
   @discord.ui.select(
       cls=Select,
       placeholder="番号2",
       options=[
           discord.SelectOption(label="0",value="0"),
           discord.SelectOption(label="1",value="1"),
           discord.SelectOption(label="2",value="2"),
           discord.SelectOption(label="3",value="3"),
           discord.SelectOption(label="4",value="4"),
           discord.SelectOption(label="5",value="5"),
           discord.SelectOption(label="6",value="6"),
           discord.SelectOption(label="7",value="7"),
           discord.SelectOption(label="8",value="8"),
           discord.SelectOption(label="9",value="9"),
       ]
   )
   async def numberselect2(self, interaction: discord.Interaction, select: Select):         
       select.disabled = True
       await interaction.response.edit_message(view=self)
       #await interaction.followup.send(f"{select.values}")
       #savetxt(f"./renew/{interaction.user.id}code2.txt",select.values[0])
       data = dict(loadjson(f"./renew/{interaction.user.id}.json"))
       key = "code2"
       data[key] = select.values[0]
       savejson(f"./renew/{interaction.user.id}.json",data)
       await codecheck(interaction)

async def codecheck(interaction: discord.Interaction):
  jsondata=loadjson(f"./renew/{interaction.user.id}.json")
  if not len(jsondata)==4:
     return
  await interaction.followup.send("入力された番号:"+jsondata["grade"]+jsondata["class"]+jsondata["code1"]+jsondata["code2"])
  view3 = discord.ui.View()
  button5 = discord.ui.Button(style=discord.ButtonStyle.danger, label="やり直す", custom_id="delete_ticket")
  view3.add_item(button5)
  await interaction.followup.send("番号選択をやり直すには最初からやり直してください", view=view3)
  button = discord.ui.Button(label="学籍番号を入力する", style=discord.ButtonStyle.success, custom_id="rngakuseki")
  view = discord.ui.View()
  view.add_item(button)
  await interaction.followup.send(view=view)
  

class clubselect(View):
   @discord.ui.select(
       cls=Select,
       placeholder="部活",
       options=[
           discord.SelectOption(label="野球部",value="1224959136681168927",description="(中高どちらも)"),
           discord.SelectOption(label="サッカー部",value="1224959616551485500",description=""),
           discord.SelectOption(label="陸上部",value="1224971831572955206",description="中学3年生"),
           discord.SelectOption(label="4年",value="4",description="高校1年生"),
           discord.SelectOption(label="5年",value="5",description="高校2年生"),
           discord.SelectOption(label="6年",value="6",description="高校3年生"),
           discord.SelectOption(label="OB",value="OB",description="卒業生"),
       ]
   )
   async def gradeselect(self, interaction: discord.Interaction, select: Select):         
       select.disabled = True
       await interaction.response.edit_message(view=self)
       #await interaction.followup.send(f"{select.values}")
       #savetxt(f"./renew/{interaction.user.id}grade.txt",select.values[0])
       data = dict(loadjson(f"./renew/{interaction.user.id}.json"))
       key = "grade"
       data[key] = select.values[0]
       savejson(f"./renew/{interaction.user.id}.json",data)
       await codecheck(interaction)