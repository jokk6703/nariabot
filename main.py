import discord
import os

client = discord.Client()

#프로그램 시작되었을 때 작동하는 코드
@client.event
async def on_ready():
    print("Logged in as ")
    print(client.user.name)
    print(client.user.id)
    print(":)")
    print("명령어는 !나리아 입니다.")
    await client.change_presence(game=discord.Game(name="나리아 봇은 최고이다!!", type=1))

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    id = message.author.id
    channel = message.channel
    
    if message.content.startswith("!나리아 도움"):
        await client.send_message(channel, "아직은 명령어가 없습니다.")
        
@bot.command()
async def 나리아(ctx):
    await ctx.send("안녕하세요! 나리아 봇입니다. 명령어를 알고 싶다면 !나리아 도움이라는 명령어를 사용하시면 됩니다.")

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
