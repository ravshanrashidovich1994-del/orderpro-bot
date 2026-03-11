from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8636158499:AAE9tAAUSbROKfipRbdiBKeV2pZGF6dxKu0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 ORDERPRO — Центр приёма заказов\n\n"
        "Напишите описание задачи.\n"
        "Укажите бюджет и срок."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    await update.message.reply_text(
        "✅ Заявка получена.\n"
        "Мы скоро свяжемся с вами."
    )

    print("НОВЫЙ ЗАКАЗ:", user_text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("BOT STARTED")

app.run_polling()
