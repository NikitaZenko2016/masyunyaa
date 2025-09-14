import disnake
from disnake.ext import commands
import src.config as cfg

bot = commands.Bot(
        command_prefix='!',
        intents=disnake.Intents.all(), 
        test_guilds=cfg.test_guilds,
        activity = disnake.CustomActivity(name='Запускается...')
    )


def run_bot():
    import src.commands
    
    bot.run(cfg.TOKEN)