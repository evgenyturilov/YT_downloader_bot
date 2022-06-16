from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *


app = ApplicationBuilder().token("5400201806:AAHsMHlC5ctvmhivc8RK2hcwmVsSRYrpoYY").build()

print('server active')

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("download", dwnld))

app.run_polling()