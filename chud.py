import discord
import random
import json
import os
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()

exclusiveId = 1214854217706110998 #hhahahha only i can use this hhahahah

file = "money.json"

# save/load
def load():
    if not os.path.exists(file):
        return {}
    with open(file, "r") as f:
        return json.load(f)

def save(data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)


balances = load()

def get_balance(user_id):
    user_id = str(user_id)
    if user_id not in balances:
        balances[user_id] = 67
        save(balances)
    return balances[user_id]

def update_balance(user_id, amount):
    user_id = str(user_id)
    balances[user_id] = get_balance(user_id) + amount
    save(balances)
#button thingy
class RevealView(discord.ui.View):
    def __init__(self, content: str):
        super().__init__(timeout=60) #just for a minute cuz yes
        self.content = content

    @discord.ui.button(label="reveal", style=discord.ButtonStyle.primary)
    async def reveal_button(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message(self.content, ephemeral=True)

@bot.event
async def on_ready():
    print(f"{bot.user} is FUCKING ready!")
#-------------------------------------------------------------

@bot.slash_command(name="hello", description="say hello to john :)",
integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def hello(ctx: discord.ApplicationContext):
    print("/hello triggered")
    await ctx.respond("yo man")

#-----------------------------------------------------spam lol
@bot.slash_command(name="repeat", description="dont spam plz",
integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def repeat(ctx: discord.ApplicationContext, amount: int, message: str):
    print("/repeat triggered")
    #----------------------
    if ctx.author.id == exclusiveId:
        if amount <= 0:
            await ctx.respond("no u")
            return
        if amount > 25:
            await ctx.respond("yo this guy wanna flood the chat using me")
            return
        await ctx.respond("ok man")
        for _ in range(amount):
            await ctx.respond(message) 
    else:
        await ctx.respond(f"yo you don't have perm {ctx.author.mention}")
#-----------------------------------------------------
@bot.slash_command(name="checkmoney", description="see how broke you are :D",
integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def checkmoney(ctx: discord.ApplicationContext):
    monei = get_balance(ctx.author.id)
    print("/checkmoney triggered")
    if monei < 40:
        await ctx.respond(f"yo you have {monei} broke ass")
    elif monei < 80:
        await ctx.respond(f"you currently have {monei} sir :)")
    elif monei < 120:
        await ctx.respond(f"my king... {monei} is your balance...")
    else:
        await ctx.respond(f"how the fuck do you have {monei}$???")
#--------------------------------------------------

@bot.slash_command(name="gamble", description="the most important command ever..",integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def gamble(ctx: discord.ApplicationContext, amount: int):
    user_id = ctx.author.id
    monei = get_balance(user_id)
    print("/gamble triggered")
    if amount <= 0:
        await ctx.respond("you bet nothing sir")
        return

    if amount > monei:
        await ctx.respond("look at your wallet broke ass")
        return

    if random.choice([True, False]):
        update_balance(user_id, amount)
        await ctx.respond(f"no way you just won {amount}$!!")
    else:
        update_balance(user_id, -amount)
        await ctx.respond(f"you lose {amount}$")
#------------------------------------------------------

@bot.slash_command(name="randomnumber", description="choose random thing",
integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def randomnumber(ctx: discord.ApplicationContext, min: int, max: int):
    print("/randomnumber triggered")
    await ctx.respond(random.randint(min, max))
#-------------------------------------------------------

@bot.slash_command(name="statement",
integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def statement(ctx: discord.ApplicationContext, whar: str):
    print("/statement triggered")
    if random.randint(1, 2) == 1:
        await ctx.respond(f'the statement "{whar}" is true')
    else:
        await ctx.respond(f'the statement "{whar}" is false')
#-------------------------------------------------------------

@bot.slash_command(name="releasedate",
integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def releasedate(ctx: discord.ApplicationContext, thing: str):
    print("/releasedate triggered")
    await ctx.respond(
        f'{thing} will be released in {random.randint(1, 1000)} days'
    )

#--------------------------------------------------------
@bot.slash_command(name="randommoney", description="get free money by guessing number from 1 to 10",
integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def randommoney(ctx: discord.ApplicationContext, guess: int):
    print("/randommoney triggered")
    user_id = ctx.author.id
    if (random.randint(1, 10)) == guess:
        await ctx.respond(f'yo ur guess is right')
        update_balance(user_id, 5)
    else:
        await ctx.respond(f'wrong number loser')
#-------------------------------------------------------
@bot.slash_command(name="echo", description="force me to say something",
integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def echo(ctx: discord.ApplicationContext, saywhat: str):
    print("/echo triggered")
    if ctx.author.id == exclusiveId:
        await ctx.respond(saywhat)
    else:
        await ctx.respond(f"yo you don't have perm {ctx.author.mention}")
#----------------------------------------------------------
@bot.slash_command(name="commit", description="no",
integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def commit(ctx: discord.ApplicationContext, commit: str):
    await ctx.respond(f"{ctx.author.mention} commit {commit}")
#-------------------------------------------------------------
@bot.slash_command(name="gunner", description="shot someone (can be u)",
integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def gunner(ctx: discord.ApplicationContext, user: discord.Member):
    print("/gunner triggered")
    if random.choice([True, False]):
        await ctx.respond(
            f'{ctx.author.mention} tried to shoot {user.mention} but there is no bullet in the gun'
        )
    else:
        await ctx.respond(
            f'{ctx.author.mention} shot {user.mention} {random.randint(1, 100)} times with his gun'
        )
#-------------------------------------------------------------
@bot.slash_command(name="reveal", description="kinda like spoiler but funnier",
                  integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def reveal(
    ctx: discord.ApplicationContext,
    content: discord.Option(str, "spoiler text")
):
    await ctx.respond("press dis for funny", view=RevealView(content))


bot.run(os.getenv("TOKEN"))
