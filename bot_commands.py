from telegram import Update
from telegram.ext import ContextTypes
from pytube import YouTube

def dl(str):
    YouTube(str).streams.get_highest_resolution().download('/home/pi/GB_Dev/PY/YT_downloader_bot/downloads')
    print('video downloaded successfully')


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes) -> None:
    await update.message.reply_text(f'/download + YouTube link for downloading video to server in highest quality')

async def dwnld(update: Update, context: ContextTypes) -> None:
    global lnk
    msg = update.message.text
    items = msg.split()
    lnk = items[1]
    print(lnk)
    dl(lnk)
    await update.message.reply_text(f'Video downloaded successfully!')