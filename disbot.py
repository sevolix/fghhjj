import discord 
import asyncio
import random


client = discord.Client()

token ="ODAzODQ3NTEzNTA4NDEzNDcw.YBDvVQ.mKFWC0npzZq0ELw2whGUJ4BkNDo"

@client.event
async def on_ready():

    print(client.user.name)
    print('봇성공')
    game = discord.Game('트레이드 가이드')
    await client.change_presence(status=discord.Status.online, activity=game)
    
    
@client.event
async def on_message(message):
	if message.content == ("!help"):
		await message.channel.send(";!포이즌이란?,!리밋거래하는법,!리밋가치보는사이트")
	
	if message.content == ("!포이즌이란?"):

		embed = discord.Embed(title="포이즌이란?", description="포이즌이란 불법적인방법으로 얻은 리밋템을 의미하는데 계정이 정지당할수도 있습니다.", color=0x00ff00)

		embed.set_footer(text="")

		await message.channel.send(embed=embed)

	if message.content == ("!리밋거래하는법"):
			embed = discord.				Embed(title="리밋거래하는법", 		description="리미티드아이템을 거래하려면 로블록스 프리미엄과 1개 이상의 리미티드 아이템이 필요해요", color=0x00ff00)
			embed.set_footer(text="")
			await message.channel.				send(embed=embed)
		
	if message.content == ("!리밋가치보는사이트"):
		await message.channel.send("https://www.rolimons.com/")



client.run(token)