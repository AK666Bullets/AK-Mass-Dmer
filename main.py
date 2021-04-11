import discord

client = discord.Client()

@client.event
async def on_connect():
  for user in client.user.friends:
    try:
      await user.send('Put Message Here')
      print(f"messaged: {user.name}")
    except:
       print(f"couldnt message: {user.name}")

client.run('Put Token Here', bot=False)
