import discord

TOKEN = 'OTc4NDI2MTA4MzIyMTUyNDU4.GDOZ4G.8fvoznKKvn-97FnKO83OOCly1yGCnkSnVJPCYQ'
client = discord.Client()

@client.event
async def on_ready():
    print('We gottem')

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return
    
    if message.channel.name == 'wow':
        if user_message.lower() == 'sup':
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'Bye ig')
            return



client.run(TOKEN)