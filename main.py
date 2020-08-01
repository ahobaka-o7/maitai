from bots import TwitterBot
from config import AppConfig

app_config = AppConfig()
bot = TwitterBot(app_config.twitter)
bot.run()
