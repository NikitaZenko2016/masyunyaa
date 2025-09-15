import disnake
from disnake.ext import commands, tasks
from src.bot import bot
import src.generator as gen
import time
import random

ALLOWED_ROLE = "Любимец Масюни"
last_message = None
last_message_author = None
last_message_time = None
logger = gen.Logger('messages.txt')
gen.initialization(logger.read_logs()) 

@bot.command()
async def button(ctx):
        view = disnake.ui.View()
        button = disnake.ui.Button(
            label="Нажми чтобы приманить масюню",
            style=disnake.ButtonStyle.link,
            url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%2Fid%2FOIP.yuahPioUQIlzrFiIR8xpnQAAAA%3Fpid%3DApi&f=1&ipt=61b2605d7a976d2c7efd13ed3c2dc9a04e1b0ecc228f9fad82fb2d38749cbb13&ipo=images"
        )
        view.add_item(button)
        await ctx.send("Тут будет Мася. ТОК ТССС, никому больше.", view=view)

@bot.command(description="Говорит факт о данном пользователе.")
async def fact(ctx, person='@1010653340931207308'):
    if gen.id_from_ping(person):
        txt = gen.choice(int(person[2:-1]))
        await ctx.channel.send(f"{person}, {txt}")
    else:
        print("/fact не сработал чето")
        return
    
@bot.command()
async def echo(ctx, *, text):
    if disnake.utils.get(ctx.author.roles, name=ALLOWED_ROLE) is not None or gen.author_is_cool():
        channel = bot.get_channel(1078030588692398091)
        await channel.send(f'{text}')
        print(f'Масюня написала: {text}')

@tasks.loop(minutes=15)
async def change_activity():
    anime = gen.anime()
    activity = disnake.Activity(type=disnake.ActivityType.watching, name=anime)
    await bot.change_presence(activity=activity)
    print('Смотрит - ', anime, '    ', time.strftime("%H:%M:%S", time.localtime()))
    
@tasks.loop(minutes=5)
async def regular_task():
    channel = bot.get_channel(1399330008157130753)
    if channel:
        await channel.send(gen.generate_chain())

@bot.event
async def on_ready():
    print(f"Бот запущен как {bot.user}")
    try:
        regular_task.start()
        change_activity.start()
    except:
        print('Повторный запуск регулярных задач.')

@bot.listen("on_button_click")
async def on_button(inter: disnake.MessageInteraction):
    if inter.component.custom_id not in ["yes", "no"]:
        return
    if inter.component.custom_id == "yes":
        await inter.response.send_message("ну факт")
    elif inter.component.custom_id == "no":
        await inter.response.send_message("ты не прав.")

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.guild.id != 1065221749706334269 or message.author.id == 1279846051393572884:
        return
    
    id = message.author.id
    text = gen.choice(id)

    if gen.author_is_cool(id):
        for content in message.content.lower().split():
            if content in ["грустно", "грущу", "грусчу", "грустчу", "(", '😓', '😥', '😔', '😭', '😢']:
                await message.add_reaction(random.choice(['😓','😥','😔','😭']))
                await message.channel.send(f"<@{id}>, это так грустно")
                return
        if random.randint(1, 8) == 2:
            await message.add_reaction(random.choice(['😍', '🥰','🤩','😘']))
        if random.randint(1, 10) == 1:
            await message.channel.send(f"<@{id}>, {text}")
    elif not gen.author_is_cool(id):
        await message.add_reaction("🤡")
        await message.channel.send(f"<@{id}>, {text}")
    else:
        return
    
    
    global last_message_author
    global last_message
    global last_message_time
    if message.content.startswith(bot.command_prefix):
        await bot.process_commands(message)
        return
    if message.author.id == 1279846051393572884:
        return
    if message.content.startswith('<@1279846051393572884>'):
        await message.channel.send(gen.generate_chain())
        return
    if random.randint(1, 7) == 2:
        await message.channel.send(gen.generate_chain())
    if  last_message_time != None and time.time()-last_message_time<=10 and last_message_author == message.author.id:
        message.content = last_message + ' ' + message.content
    logger.log(message.content)
    gen.process_message(message.content)
    last_message = message.content
    last_message_time = time.time()
    last_message_author = message.author.id