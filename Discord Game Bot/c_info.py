import a_setup
import discord as dc


@a_setup.client.slash_command(description="Learn more about the rarities of items", guild_ids=a_setup.guild_ids)
async def rarities(ctx):
    kk = a_setup.kk

    description = f"**Common :white_circle:**\n " \
                  f"You can sell them for **40** {kk} to the bank. The probability to pull one is **45%**.\n\n " \
                  f"**Uncommon :green_circle:**\n" \
                  f"You can sell them for **60** {kk} to the bank. The probability to pull one is **25%**.\n\n " \
                  f"**Rare :blue_circle:**\n" \
                  f"You can sell them for **90** {kk} to the bank. The probability to pull one is **20%**.\n\n " \
                  f"**Epic :purple_circle:**\n" \
                  f"You can sell them for **220** {kk} to the bank. The probability to pull one is **7.5%**.\n\n " \
                  f"**Kjell Crowns {kk}**\n" \
                  f"With a chance of **2%** you will get **600** Kjell Crowns instead of an item.\n\n" \
                  f"**Legendary :star:**\n" \
                  f"You can sell them for **800** {kk} to the bank. The probability to pull one is **0.5%**.\n\n " \
                  f"**Specialrank :secret:**\n" \
                  f"You **can't sell** them to the bank. You **can't receive them by gambling**, only during events. " \
                  f"Each of them **should only be once in the game**."

    embed = dc.Embed(title="Information about rarities", colour=dc.Colour(0x6d3619), description=description)
    await ctx.respond(embed=embed)


@a_setup.client.slash_command(name="help", description="The bots basics", guild_ids=a_setup.guild_ids)
async def help_bot(ctx):
    kk = a_setup.kk

    description = f"This bot was created by **github.com/onishrimp**.\n\n" \
                  f"**Features**\n" \
                  f"This bot features a gacha system. Each day, you can claim so called 'Kjell Crowns' {kk} with " \
                  f"**/daily**. With **/gamble** you can gamble for dinosaurs and then collect and trade them with " \
                  f"others.\n\n" \
                  f"**It's commands**\n" \
                  f"If you type / in the bot chat and click on the bots icon you will get an overview with simple " \
                  f"descriptions of the bots commands. Then just chose a command and if required give it the needed " \
                  f"parameters. Easier than it sounds." \

    embed = dc.Embed(title="The Discord Game Bot", colour=dc.Colour(0x6d3619), description=description)

    icon = "https://cdn.discordapp.com/attachments/912362937077891132/914146351548338216/KK_real.png"
    embed.set_thumbnail(url=icon)

    await ctx.respond(embed=embed)


# @a_setup.client.slash_command(name="admin-help", description="Information for administrators",
#                               guild_ids=a_setup.guild_ids)
# async def admin_help(ctx):
#     message_author = ctx.author.mention.replace("!", "")
#
#     if message_author not in a_setup.bot_owners:
#         await ctx.respond(content=f"**YOU ARE NOT MY MASTER 👺**", ephemeral=True)
#         return
#
#     kk = a_setup.kk
#
#     description = f"This is a small document meant for **the admins** of the bot.\n\n" \
#                   f"**General**\n" \
#                   f"As you probably know, in the **a_setup.py** document you can set a list of administrators that " \
#                   f"are able to use the admin_x commands. They are the only ones that can use these and because they " \
#                   f"have the **power to break the game**, an admin should use them wisely.\n\n" \
#                   f"**/admin_give**\n" \
#                   f"With this command you can either give someone **crowns** if an integer is used, or give someone " \
#                   f"an item if one of the names of **a_items.yaml** is used. As you maybe found out when you went to " \
#                   f"the bottom of the document, there are **specialrank** items listed that you cannot get from " \
#                   f"gambling, or any normal way in the game. With the admin_give command it is possible to give " \
#                   f"these items to people. Try to only have each of them **once** in the game. Maybe you could put " \
#                   f"one for **1000** {kk} when releasing the bot into the bazaar?"
#
#     embed = dc.Embed(title="Admin Help", colour=dc.Colour(0x6d3619), description=description)
#
#     icon = "https://cdn.discordapp.com/attachments/912362937077891132/914146351548338216/KK_real.png"
#     embed.set_thumbnail(url=icon)
#
#     await ctx.respond(embed=embed, ephemeral=True)
