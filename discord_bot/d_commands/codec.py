import base64
import binascii

async def decoder(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, embed_color, args, binary):
  if " ".join(args[2:]) == "" or " ".join(args[2:]) == " " or " ".join(args[2:]) == None:
    no_args = discord.Embed(title=localization[1][14][0], description=localization[1][14][8], color=embed_color)
    return await message.channel.send(embed=no_args)
  decoder_content = discord.Embed(title=localization[1][14][0], description=localization[1][14][1] + "\n\n" + localization[1][14][3], color=embed_color)
  msg = await message.channel.send(embed=decoder_content)
  await msg.add_reaction(emoji="1️⃣")
  await msg.add_reaction(emoji="2️⃣")
  await msg.add_reaction(emoji="3️⃣")
  await msg.add_reaction(emoji="4️⃣")
  @bot.event
  async def on_reaction_add(reaction, user):
      channel = reaction.message.channel
      if reaction.emoji == "1️⃣" and user.id != bot.user.id:
        try:
          result = base64.standard_b64decode(" ".join(args[2:]).encode('ascii')).decode('ascii')
        except:
          result = localization[1][14][6]
        decoder_result_content = discord.Embed(title=str(localization[1][14][0]), color=embed_color)
        decoder_result_content.add_field(name=str(localization[1][14][4]), value='```' + str(result) + '```', inline=True)
        await msg.edit(embed=decoder_result_content)
      if reaction.emoji == "2️⃣" and user.id != bot.user.id:
        try:
          result = base64.b32decode(" ".join(args[2:]).encode('ascii')).decode('ascii')
        except:
          result = localization[1][14][6]
        decoder_result_content = discord.Embed(title=localization[1][14][0], color=embed_color)
        decoder_result_content.add_field(name=str(localization[1][14][4]), value='```' + str(result) + '```', inline=True)
        await msg.edit(embed=decoder_result_content)
      if reaction.emoji == "3️⃣" and user.id != bot.user.id:
        try:
          result = base64.b16decode(" ".join(args[2:]).encode('ascii')).decode('ascii')
        except:
          result = localization[1][14][6]
        decoder_result_content = discord.Embed(title=localization[1][14][0], color=embed_color)
        decoder_result_content.add_field(name=str(localization[1][14][4]), value='```' + str(result) + '```', inline=True)
        await msg.edit(embed=decoder_result_content)
      if reaction.emoji == "4️⃣" and user.id != bot.user.id:
        try:
         result = str(binary.decode(" ".join(args[2:])))
        except Exception as e:
          print(e)
          result = localization[1][14][6]
        decoder_result_content = discord.Embed(title=localization[1][14][0], color=embed_color)
        decoder_result_content.add_field(name=str(localization[1][14][4]), value='```' + str(result) + '```', inline=True)
        await msg.edit(embed=decoder_result_content)

async def encoder(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, embed_color, args, binary):
  if " ".join(args[2:]) == "" or " ".join(args[2:]) == " " or " ".join(args[2:]) == None:
    no_args = discord.Embed(title=localization[1][14][0], description=localization[1][14][8], color=embed_color)
    return await message.channel.send(embed=no_args)
  decoder_content = discord.Embed(title=localization[1][14][0], description=localization[1][14][2] + "\n\n" + localization[1][14][3], color=embed_color)
  msg = await message.channel.send(embed=decoder_content)
  await msg.add_reaction(emoji="1️⃣")
  await msg.add_reaction(emoji="2️⃣")
  await msg.add_reaction(emoji="3️⃣")
  await msg.add_reaction(emoji="4️⃣")
  @bot.event
  async def on_reaction_add(reaction, user):
      channel = reaction.message.channel
      if reaction.emoji == "1️⃣" and user.id != bot.user.id:
        try:
          result = base64.standard_b64encode(" ".join(args[2:]).encode('ascii')).decode('ascii')
        except:
          result = localization[1][14][6]
        decoder_result_content = discord.Embed(title=localization[1][14][0], color=embed_color)
        decoder_result_content.add_field(name=str(localization[1][14][4]), value="```" + str(result) + "```", inline=True)
        await msg.edit(embed=decoder_result_content)
      if reaction.emoji == "2️⃣" and user.id != bot.user.id:
        try:
          result = base64.b32encode(" ".join(args[2:]).encode('ascii')).decode('ascii')
        except:
          result = localization[1][14][6]
        decoder_result_content = discord.Embed(title=localization[1][14][0], color=embed_color)
        decoder_result_content.add_field(name=str(localization[1][14][4]), value="```" + str(result) + "```", inline=True)
        await msg.edit(embed=decoder_result_content)
      if reaction.emoji == "3️⃣" and user.id != bot.user.id:
        try:
          result = base64.b16encode(" ".join(args[2:]).encode('ascii')).decode('ascii')
        except:
          result = localization[1][14][6]
        decoder_result_content = discord.Embed(title=localization[1][14][0], color=embed_color)
        decoder_result_content.add_field(name=str(localization[1][14][4]), value="```" + str(result) + "```", inline=True)
        await msg.edit(embed=decoder_result_content)
      if reaction.emoji == "4️⃣" and user.id != bot.user.id:
        try:
          args_str = " ".join(args[2:])
          result = ""
          for letter in list(args_str):
            try:
              result += binary.encode()[letter]
            except Exception as e:
              print(e)
              result += ''
        except Exception as e:
          result = localization[1][14][6]
          print(e)
        try:
          decoder_result_content = discord.Embed(title=localization[1][14][0], color=embed_color)
          decoder_result_content.add_field(name=str(localization[1][14][4]), value='```' + str(result) + '```', inline=True)
          await msg.edit(embed=decoder_result_content)
        except:
          decoder_result_content = discord.Embed(title=localization[1][14][0], color=embed_color)
          decoder_result_content.add_field(name=str(localization[1][14][4]), value=localization[1][14][7], inline=True)
          try:
            await msg.edit(content=str('```' + str(result) + '```'), embed=decoder_result_content)
          except:
            await msg.edit(content='', embed=decoder_result_content)
async def get_help(bot, discord, message, botconfig, os, platform, datetime, one_result, localization, embed_color):
  help_content = discord.Embed(title=localization[1][14][0], description=localization[1][14][5], color=embed_color)
  await message.channel.send(embed=help_content)