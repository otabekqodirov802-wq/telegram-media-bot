import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("7523835199:AAFohWAN1AK30sGioGrerKbt1HMwbQ5lFi4")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Salom 👋\n"
        "/rasm - rasm yuboradi\n"
        "/video - video yuboradi\n"
        "/fayl - fayl yuboradi"
    )

async def rasm(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo=open("rasm.jpg", "rb")
    )

async def video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_video(
        chat_id=update.effective_chat.id,
        video=open("video.mp4", "rb")
    )

async def fayl(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_document(
        chat_id=update.effective_chat.id,
        document=open("fayl.pdf", "rb")
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("rasm", rasm))
app.add_handler(CommandHandler("video", video))
app.add_handler(CommandHandler("fayl", fayl))

app.run_polling()
