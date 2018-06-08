import discord
import random
from discord.ext.commands import Bot
from discord.ext import commands
import os
import json




bot = discord.Client()
bot_prefix="e!"
bot = commands.Bot(command_prefix=bot_prefix)

@bot.event
async def on_ready() :
    print("Bot çevrimiçi!")
    print("İsim : {}".format(bot.user.name))
    print("ID : {}".format(bot.user.id))
    print(str(len(bot.servers)) + " tane serverda çalışıyor!")
    print(str(len(set(bot.get_all_members()))) + " tane kullanıcaya erişiyor!")
    await bot.change_presence(game=discord.Game(name=str(len(set(bot.get_all_members()))) + " tane kullanıcaya erişiyor!"))
    
    
@bot.event
async def on_message(message):

    if message.content.lower().startswith('e!lvl'):
        await bot.send_message(message.channel, "Tam tamına `{}` Levelsin!".format(lvl(message.author.id)))
    if message.content.lower().startswith('e!exp'):
        await bot.send_message(message.channel, "Tam tamına `{}` XP!".format(exp(message.author.id)))
    dnme(message.author.id)

def dnme (usr: int):
    with open('data.json') as data_file:
        data2 = json.load(data_file)
    
    try:
        with open('data.json') as data_file:
            data2 = json.load(data_file)
        exp = data2[usr][0]["exp"]
        texp = int(exp) + 7
        level = data2[usr][0]["level"]
        if level == 0:
            texp = int(exp) + 7
        if level == 1:
            texp = int(exp) + 6
        if level == 2:
            texp = int(exp) + 5
        if level == 3:
            texp = int(exp) + 4
        if level == 4:
            texp = int(exp) + 3
        if level == 5:
            texp = int(exp) + 2

        if exp >= 148 and level == 0:
            tlvl = int(level) + 1
        if exp >= 352 and level == 1:
            tlvl = int(level) + 1
        if exp >= 789 and level == 2:
            tlvl = int(level) + 1
        if exp >= 1088 and level == 3:
            tlvl = int(level) + 1
        if exp >= 1876 and level == 4:
            tlvl = int(level) + 1
        if exp >= 3152 and level == 5:
            tlvl = int(level) + 1
        else:
            tlvl = level
        

    except KeyError:
        data=data2
        data[usr] = []
        data[usr].append({
        'exp': 2,
        'level': '0'
        })

        with open('data.json', 'w') as outfile:  
            json.dump(data, outfile)
   
    data=data2
    data[usr] = []
    data[usr].append({
    'exp': texp ,
    'level': tlvl
    })

    with open('data.json', 'w') as outfile:  
        json.dump(data, outfile)
    
def exp (usr: int):
    with open('data.json') as data_file:
        data = json.load(data_file)

    return data[usr][0]["exp"]

def lvl (usr: int):
    with open('data.json') as data_file:
        data = json.load(data_file)

    return data[usr][0]["level"]

@bot.command(pass_context=True)
async def hadibakim(ctx) :
    await bot.say("Birileri demiş öldü şimdi yazsınlar KRAL geri döndü!")

@bot.command(pass_context=True)
async def öp(ctx, member:discord.Member) :
   urll = ["http://24.media.tumblr.com/tumblr_m8yxnswMgE1rc0fd6o1_r5_500.gif" , 
   "https://pa1.narvii.com/5823/a1ff3fbec588fdde66dd24293f2220233ce42076_hq.gif" , 
   "https://media1.tenor.com/images/0de1905e4a8b2bb465d04a1f96df7f85/tenor.gif" , 
   "https://media.giphy.com/media/Gj8bn4pgTocog/giphy.gif" , 
   "http://24.media.tumblr.com/8d6a96407131c70a80c91544cddd8260/tumblr_mvaj4jBG0D1r60ay5o1_500.gif" , 
   "https://media1.giphy.com/media/G3va31oEEnIkM/giphy.gif" , 
   "https://media.giphy.com/media/FqBTvSNjNzeZG/giphy.gif" , 
   "https://media0.giphy.com/media/bGm9FuBCGg4SY/200.gif"]
   embed = discord.Embed(title=ctx.message.author.name + " seni öpüyor " + member.name)
   embed.set_image(url=random.choice(urll))
   await bot.say(embed = embed)

@bot.command(pass_context=True)
async def sik(ctx, member:discord.Member) :
   urll = ["https://static.hentai-gifs.com/upload/20160703/19/36972/1.gif" , 
   "https://78.media.tumblr.com/931125762652e49075f26f954049c0da/tumblr_msvseafYc01sflbiso1_1280.gif" , 
   "https://www.rencontresanslendemain.net/wp-content/uploads/2018/02/gif-sexe-hentai.gif" , 
   "https://78.media.tumblr.com/3acd627d51c3484deb5a1349dba15f61/tumblr_nerlc5vPvU1u3p95io1_500.gif" , 
   "https://68.media.tumblr.com/37320d7ba87cc087713cd5f42ceff0fa/tumblr_ok06xwuKen1v2hfg0o1_500.gif" ,
   "https://78.media.tumblr.com/188f0818225d5f1c579a0eb5010b0c90/tumblr_o5498914Dp1ugdh13o1_500.gif" , 
   "https://78.media.tumblr.com/852fc9eff5caf44be79e92295676fbd1/tumblr_o549fohYOD1ugdh13o8_540.gif" ,
   "https://78.media.tumblr.com/54a670815a39bde673bdaaa35f08a88d/tumblr_o548wwiAhn1ugdh13o1_500.gif" ,
   "https://78.media.tumblr.com/65b0296ed9d5e12e79ac1c02c4502b63/tumblr_o548y9hptR1ugdh13o1_500.gif" , 
   "https://78.media.tumblr.com/916f8497317b49edb5802fa6aa411f47/tumblr_o5492gX7Ir1ugdh13o1_500.gif" ,
   "https://78.media.tumblr.com/de046b1380f663bf05d4833de2ec8078/tumblr_o54939bHby1ugdh13o1_500.gif" ,
   "https://78.media.tumblr.com/9cdba610e7f393539718c12a010c12c1/tumblr_o5493vuIAk1ugdh13o1_500.gif" ,
   "https://78.media.tumblr.com/5a030c57050ce1bcaa4c5efc116ad27a/tumblr_o5496dmxSS1ugdh13o1_500.gif" ,]
   embed = discord.Embed(title=ctx.message.author.name + " seni sikiyor " + member.name)
   embed.set_image(url=random.choice(urll))
   await bot.say(embed = embed)

@bot.command(pass_context=True)
async def sev(ctx, member:discord.Member) :
   urll = ["https://media1.tenor.com/images/73a746bada06751716d3173fbb9e6864/tenor.gif" , 
   "https://media1.tenor.com/images/a4a2b1eaa47fd0d8d0951433bc59ab9a/tenor.gif" , 
   "https://media.giphy.com/media/K1InqndmlQDE4/giphy.gif" , 
   "https://i.pinimg.com/originals/2c/6e/4b/2c6e4bb81e44fe1a0b8c599f292e2be5.gif" , 
   "https://i.pinimg.com/originals/b6/9a/79/b69a790c15ebdc4a4bf9c16aa6dec786.gif" , 
   "https://media.giphy.com/media/lq72vRtxJtpgQ/giphy.gif"]
   embed = discord.Embed(title=ctx.message.author.name + " seni seviyor " + member.name)
   embed.set_image(url=random.choice(urll))
   await bot.say(embed = embed)

@bot.command(pass_context=True)
async def sarıl(ctx, member:discord.Member) :
   urll = ["https://78.media.tumblr.com/2fe074ad467af41a8230b8d9d8e322f1/tumblr_omvj49wYnq1v8tshbo1_500.gif" , 
   "https://media.giphy.com/media/l2QDM9Jnim1YVILXa/giphy.gif" , 
   "https://media1.tenor.com/images/49a21e182fcdfb3e96cc9d9421f8ee3f/tenor.gif" , 
   "https://media.giphy.com/media/3bqtLDeiDtwhq/giphy.gif" , 
   "https://78.media.tumblr.com/b4655e26f615a0e2081b9a6c90076539/tumblr_n13pt9SV4p1r45wgho2_500.gif" , 
   "https://media.giphy.com/media/wnsgren9NtITS/giphy.gif" , 
   "https://i.gifer.com/B7bp.gif",
   "https://cdn.discordapp.com/attachments/357958080224559105/451687910090211338/171021_8687.gif"]
   embed = discord.Embed(title=ctx.message.author.name + " sana sarılıyor " + member.name)
   embed.set_image(url=random.choice(urll))
   await bot.say(embed = embed)


@bot.command(pass_context=True)
async def developer(ctx, member:discord.Member) :
   urll = ["https://media1.tenor.com/images/73a746bada06751716d3173fbb9e6864/tenor.gif"]
   embed = discord.Embed(title=ctx.message.author.name + " seni seviyor " + member.name)
   embed.set_image(url=random.choice(urll))
   await bot.say(embed = embed)

@bot.command(pass_context=True)
async def ahkmd(ctx, member:discord.Member) :
   embed = discord.Embed(title=ctx.message.author.name + " senin anana hükmediyor " + member.name)
   await bot.say(embed = embed)

@bot.command(pass_context=True)
async def sil(ctx, number):
    mgs = [] 
    number = int(number) 
    async for x in bot.logs_from(ctx.message.channel, limit = number):
        mgs.append(x)
    await bot.delete_messages(mgs)

@bot.command(pass_context=True)
async def soyle(ctx):
    msg = ctx.message.content.split("1")
    await bot.delete_message(ctx.message)
    await bot.send_message(ctx.message.channel, msg)
    print(ctx.message.author.name, msg)
    

@bot.command(pass_context=True)
async def kaçcm(ctx):
    x = random.randint(1, 35) 
    await bot.say(ctx.message.author.name + "'nin " + str(x) + " cm yarrağı var")


    
bot.run(os.environ.get('token'))



