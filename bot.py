import discord
import time

client = discord.Client()

channels = ['tomato-commands', '🦄bots-only🦄']
mods = ['Tem1x#0549', '❁Thorny❁#7858']
admins = ['Snekman#2020', 'Nika#0054', 'N1cker#3302', 'EdaK#8418']
members = 0
messages = 0


@client.event
async def on_ready():
    print('Ready to rule my boyz into the battle!')


# def read_token():
#     with open('token.txt', 'r') as f:
#         lines = f.readlines()
#         return lines[0].strip()
try:
    import pyowm

    owm = pyowm.OWM('4454ae5bd023b2b23c4a71a9294d241a')  # API key from weather access

#TODO
    @client.event
    async def on_message(message):
        if message.content.find('t weather') != -1:
            place = 'Tallinn'
            observation = owm.weather_at_place(place)
            w = observation.get_weather()
            temp = w.get_temperature('celsius')['temp']
            windspd = w.get_wind()['speed']
            await message.channel.send(
                'Right now there is ' + str(temp) + (' celsius in ') + place + (' and ') + w.get_detailed_status() + (
                    '.'))
            await message.channel.send("Actually, wind speed is " + str(windspd) + " m/s.")
except Exception:
    pass
    print('Weather module is not working!')


# w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

@client.event
async def on_member_join(member):
    for channel in member.server.channels:
        if str(channel) == '🎉объявления🎉':
            await client.send_message(f'Welcome to the server {member.mention}! You are now my friend!')



@client.event
async def on_message(message):
    id = client.get_guild(448453910143696897)
    if str(message.channel) in channels:
        if message.content.find('t hello') != -1:
            await message.channel.send('Hi, my pal!')
        elif message.content == "t users":
            await message.channel.send(f'Number of members: {id.member_count}')
        elif message.content == "t ping":
            await message.channel.send(f'Pong!')


@client.event
async def on_message(message):
    if str(message.channel) in channels:
        if message.content.find('t time') != -1:
            await message.channel.send(str(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())))


@client.event
async def on_message(message):
    if str(message.author) not in mods or admins:
        print(f"{message.author} tried to use an admin command!")




# token = read_token()
client.run('NTkwMjU0NzU4OTg4NjExNjc1.XuYNkA.aWufw9-TIJCcSVNKIfVc_mcxTzk')