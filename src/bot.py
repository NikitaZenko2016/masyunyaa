import disnake
from disnake.ext import commands
from src.config.config import TOKEN, config as cfg

bot = commands.Bot(
        command_prefix='!',
        intents=disnake.Intents.all(), 
        test_guilds=cfg.test_guilds,
        activity = disnake.CustomActivity(name='Запускается...')
    )


def run_bot():
    import src.commands
    bot.run(TOKEN)