import discord

token = "MTM3MTQ2OTYzNDYxNTc3MTE5Ng.GuwHVm.Wzz6_YVthwmYiTvqS4yZxXICu6K0ksy7u-kik8"

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
  print("ready")

client.run(token=token)
