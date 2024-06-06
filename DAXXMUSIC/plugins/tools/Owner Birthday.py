import datetime
import pyogram
from DAXXMUSIC import app
import config

# Initialize Pyogram
pyo = pyogram.Pyogram()

# Bot token and owner's chat ID
TOKEN = 'your_bot_token'
OWNER_CHAT_ID = 'your_owner_chat_id'

# Initialize the Telegram bot
bot = telebot.TeleBot(TOKEN)

# Function to check if today is the owner's birthday
def is_birthday_today():
    # Get today's date
    today = datetime.date.today()
    
    # Owner's birthday (replace with actual birthday)
    owner_birthday = datetime.date(2004,06, 08)  # <-- Replace YYYY, MM, DD with birthday
    
    # Check if today is the owner's birthday
    return today.month == owner_birthday.month and today.day == owner_birthday.day

# Function to send birthday announcement
def send_birthday_announcement():
    if is_birthday_today():
        # Generate birthday cake ASCII art
        cake = pyo.generate(['Birthday'])
        
        # Send birthday announcement to owner
        bot.send_message(OWNER_ID, f"🎉 Happy Birthday! 🎂\n\n{cake}")

