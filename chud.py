import discord
import random
import json #storing shit
import os 
from dotenv import load_dotenv

load_dotenv() # load all the variables from the env file
bot = discord.Bot()

#note: await ctx.respond("thing") -> says something

#thing :D
file = "money.json" #get the json file

#save n load
def load():
    if not os.path.exists(file):
        return {}
    try:
        with open(file, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}
def save(data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

#not illegal at all trust me man
def get_balance(user_id):
    user_id = str(user_id)
    if user_id not in balances: #havent gamble.. yet
        balances[user_id] = 67 #67 is the best number
        save(balances)
    return balances[user_id]
#update money
def update_balance(user_id, amount):
    user_id = str(user_id)
    balances[user_id] = get_balance(user_id) + amount
    save(balances)
#money
balances = load()

@bot.event
async def on_ready():
    print(f"{bot.user} is FUCKING ready!")
#say hello :)
@bot.slash_command(name="hello", description="say hello to john :)")
async def hello(ctx: discord.ApplicationContext):
    await ctx.respond("yo man")
#gamble for kiddo
@bot.slash_command(name="checkmoney", description="see how broke you are :D")
async def checkmoney(ctx: discord.ApplicationContext):
    monei = get_balance(ctx.author.id)
    #this shit is your money boys
    #make the bot more awesome
    #idk
    #fuck
    if monei < 40:
        await ctx.respond(f"yo you have {monei} broke ass")
    elif monei < 80:
        await ctx.respond(f"you currently have {monei} sir :)")
    elif monei < 120:
        await ctx.respond(f"my king... {monei} is your balance...")
    else:
        await ctx.respond(f"how the fuck do you have {monei}$???")
#gamble (for kid (not illegal (trust me (100%))))
@bot.slash_command(name="gamble", description="the most important command ever..")
async def gamble(ctx: discord.ApplicationContext, amount: int): #amount = bet amount :D
    #get our (legal) gambler data:
    user_id = ctx.author.id
    monei = get_balance(user_id)
    #rule thing ig idk
    if amount <= 0:
        await ctx.respond("you bet nothing sir") #lol
        return
    if amount > monei:
        await ctx.respond("look at your wallet broke ass") #im sorry
        return
    #real gamble not rigged at all trust me
    if random.choice([True, False]):
        update_balance(user_id, amount) #win big
        await ctx.respond(f"no way you just won {amount}$!!")
    else:
        update_balance(user_id, -amount) #lose all
        await ctx.respond(f"you lose {amount}$")
bot.run(os.getenv('TOKEN')) # run the bot with the token
