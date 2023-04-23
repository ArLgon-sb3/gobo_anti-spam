from dotenv import load_dotenv
import discord
import re
import os
from datetime import timedelta
client = discord.Client(intents=discord.Intents.all())
load_dotenv()
TOKEN = os.getenv('TOKEN')
timeout_time = os.getenv('timeout_time')
delta = timedelta(minutes=int(timeout_time))
@client.event
async def on_message(message):
    if message.author.guild_permissions.administrator:
        return
    if re.search('(?i)[a-z0-9_-]{23,28}\.[a-z0-9_-]{6,7}\.[a-z0-9_-]{27}',message.content):
        print("トークン")
        embed=discord.Embed(description="トークンを検知しました", color=discord.Colour.red())
        embed.add_field(name="トークンは人に教えなきゃいけないシチュエーションないだろ！！！",value=urllib.parse.unquote("https://sites.google.com/view/arlgonuploder/token"))
        await message.delete()
        await message.channel.send(embed=embed)
        return
    words = ['https://discord.gg/',"あほ","アホ","ガイジ","がいじ","ばか","バカ",'きもい','キモイ','基地外','きちがい','死ね','糞','無能','ﾀﾋね','共栄圏','荒らし連合国']
    for word in words:
        if re.search(word,message.content):
            embed=discord.Embed(description="スパムフィルターによって送信がブロックされました", color=discord.Colour.red())
            await message.delete()
            await message.author.edit(timed_out_until=delta,reason=f"スパムフィルター({word})")
            await message.author.send(embed=embed)
            return
client.run(TOKEN)
