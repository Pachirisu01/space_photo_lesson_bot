import os, random, telegram
from dotenv import load_dotenv

load_dotenv()


TOKEN = os.getenv("TOKEN")

bot = telegram.Bot(token=TOKEN)

chat_id = os.getenv("CHAT_ID")

images  = os.listdir("images")

bot.send_message(chat_id=chat_id, text="This is our cosmo channel!")