import discord
from discord.ext import commands, tasks
import requests

# Define intents for the Discord bot
intents = discord.Intents.default()
intents.message_content = True

# Create the Discord bot client
bot = commands.Bot(command_prefix='!', intents=intents)

# Binance API endpoint for cryptocurrency prices
API_URL = 'https://api.binance.com/api/v3/ticker/price'

# Dictionary to store coin and update frequency information
coin_updates = {}

# Command to set a cryptocurrency for updates
@bot.command()
async def setcoin(ctx, coin):
    coin = coin.upper()
    if coin not in coin_updates:
        coin_updates[coin] = 0
    await ctx.send(f"The coin {coin} has been set for updates.")

# Command to choose the update frequency
@bot.command()
async def frequency(ctx):
    options = [
        "1. Every 15 minutes",
        "2. Every 30 minutes",
        "3. Every 45 minutes",
        "4. Every hour"
    ]
    options_message = "\n".join(options)
    await ctx.send("Choose update frequency:\n" + options_message)

# Command to start updating crypto prices
@bot.command()
async def startupdates(ctx, frequency):
    if frequency not in ['1', '2', '3', '4']:
        await ctx.send("Invalid frequency option. Please choose from 1 to 4.")
        return
    
    if len(coin_updates) == 0:
        await ctx.send("No coin has been set. Please use !setcoin command to set a coin first.")
        return
    
    interval = 0
    if frequency == '1':
        interval = 15
    elif frequency == '2':
        interval = 30
    elif frequency == '3':
        interval = 45
    elif frequency == '4':
        interval = 60
    
    await ctx.send(f"Starting updates every {interval} minutes.")
    await update_prices.start(ctx, interval)

# Scheduled task to update crypto prices
@tasks.loop(minutes=15)
async def update_prices(ctx, interval):
    for coin in coin_updates:
        response = requests.get(API_URL, params={'symbol': f'{coin}USDT'})

        if response.status_code == 200:
            data = response.json()
            if 'price' in data:
                price = data['price']
                await ctx.send(f"The current price of {coin} is ${price}")
            else:
                await ctx.send(f"Could not find price information for {coin}")
        else:
            await ctx.send("Error fetching price information from the API")

# Function executed before starting the update task
@update_prices.before_loop
async def before_update_prices():
    await bot.wait_until_ready()

# Command to retrieve the price of a specific cryptocurrency
@bot.command()
async def price(ctx, coin):
    coin = coin.upper()
    response = requests.get(API_URL, params={'symbol': f'{coin}USDT'})

    if response.status_code == 200:
        data = response.json()
        if 'price' in data:
            price = data['price']
            await ctx.send(f"The current price of {coin} is ${price}")
        else:
            await ctx.send(f"Could not find price information for {coin}")
    else:
        await ctx.send("Error fetching price information from the API")

# Event triggered when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} is now running!')

# Start the Discord bot with the token
bot.run('TOKEN')
