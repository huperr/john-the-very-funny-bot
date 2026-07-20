import discord
import random
import json
import os
from dotenv import load_dotenv

load_dotenv()

bot = discord.Bot()

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


@bot.event
async def on_ready():
    print(f"{bot.user} is FUCKING ready!")


@bot.slash_command(name="hello", description="say hello to john :)",
integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def hello(ctx: discord.ApplicationContext):
    print("/hello triggered")
    await ctx.respond("yo man")


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


@bot.slash_command(name="randomnumber", description="choose random thing",
integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def randomnumber(ctx: discord.ApplicationContext, min: int, max: int):
    print("/randomnumber triggered")
    await ctx.respond(random.randint(min, max))


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


@bot.slash_command(name="randommoney", description="get free money",
integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def randommoney(ctx: discord.ApplicationContext, min: int, max: int, guess: int):
    print("/randomnumber triggered")
    if (random.randint(min, max)) == guess:
        await ctx.respond(f'yo ur guess is right')
        update_balance(user_id, 5)
    else:
        await ctx.respond(f'wrong number loser')

@bot.slash_command(name="echo", description="force me to say something",
integration_types={
        discord.IntegrationType.guild_install,
        discord.IntegrationType.user_install,
    },)
async def echo(ctx: discord.ApplicationContext, password: int, saywhat: str):
    if password == 6769:
        await ctx.respond(saywhat)
    else:
        await ctx.respond(f"yo wrong password {ctx.author.mention}")

@bot.slash_command(name="gunner",
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


bot.run(os.getenv("TOKEN"))
