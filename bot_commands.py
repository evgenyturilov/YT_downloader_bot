from telegram import Update
from telegram.ext import ContextTypes
from pytube import YouTube

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes) -> None:
    await update.message.reply_text(f'/hello\n/help\n/link\n/res 720\n/res 480\n/res highest\n/download')

def link(update: Update, context: ContextTypes) -> None:
    global lnk
    lnk = update.message
    update.message.reply_text('OK')

def download(update: Update, context: ContextTypes) -> None:
    yt = YouTube(lnk)
    yt.streams.get_by_resolution('720').download('/home/pi/GB_Dev/PY/YT_downloader_bot/downloads')
