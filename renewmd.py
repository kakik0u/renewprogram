import discord
from mail import authmailsend
from file import savetxt,loadtxt,savejson,loadjson

class mail(discord.ui.Modal, title="学籍番号を入力"):
  number = discord.ui.TextInput(
      style=discord.TextStyle.short,
      label="学籍番号",
      required=True,
      max_length=8,
      placeholder="12710001"
  )

  async def on_submit(self, interaction: discord.Interaction):
      data = dict(loadjson(f"./renew/{interaction.user.id}.json"))
      key = "id"
      data[key] = self.number.value
      savejson(f"./renew/{interaction.user.id}.json",data)
      await interaction.response.send_message('更新を適応しています...')
      grade=data["grade"]
      classnum=data["class"]
      grsetting=loadjson("graderole.json")
      graderole=interaction.guild.get_role(grsetting[grade])
      await interaction.user.add_roles(graderole)
      classrole=discord.utils.get(interaction.guild.roles, name=f"{grade}年{classnum}組")
      await interaction.user.add_roles(classrole)
      verifyrole=interaction.guild.get_role(1079719615443238972)
      await interaction.user.add_roles(verifyrole)
      unverifyrole=interaction.guild.get_role(1224370367406014565)
      await interaction.user.remove_roles(unverifyrole)
      oldname=interaction.user.display_name
      suuzihantei=oldname[0:4]
      suuzitrue=suuzihantei.isdecimal()
      if suuzitrue == True:
         newname=data["grade"]+data["class"]+data["code1"]+data["code2"]+oldname[4:]
      else:
         newname=data["grade"]+data["class"]+data["code1"]+data["code2"]+oldname
      await interaction.user.edit(nick=newname)
      savetxt(f"./renewcache/{interaction.user.id}.txt",oldname)
      view2 = discord.ui.View()
      button6 = discord.ui.Button(style=discord.ButtonStyle.danger, label="名前を戻す", custom_id="undoname")
      view2.add_item(button6)
      await interaction.followup.send(f'更新が完了しました。\nあなたの名前を{newname}に変更しました。元に戻す場合は下のボタンをどうぞ',view=view2)
      view3 = discord.ui.View()
      button5 = discord.ui.Button(style=discord.ButtonStyle.danger, label="更新を完了する", custom_id="delete_ticket")
      view3.add_item(button5)
      await interaction.followup.send("ボタンを押して完了します", view=view3)

  async def on_error(self, interaction: discord.Interaction, error : Exception):
      pass


