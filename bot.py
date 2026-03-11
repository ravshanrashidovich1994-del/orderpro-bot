from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = "8636158499:AAE9tAAUSbROKfipRbdiBKeV2pZGF6dxKu0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
🚀 ORDERPRO — Центр приёма заказов

Добро пожаловать!

Вы подключены к системе приёма задач.

📌 Как это работает:

1️⃣ Вы отправляете описание задачи  
2️⃣ Система фиксирует заявку  
3️⃣ Специалист свяжется с вами  

Отправьте сообщение в формате:

🔧 Что нужно сделать  
💰 Бюджет  
⏳ Срок
"""
    await update.message.reply_text(text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    await update.message.reply_text(
        "✅ Заявка получена!\n\n"
        "Наш специалист скоро свяжется с вами."
    )

    print("НОВЫЙ ЗАКАЗ:")
    print(user_text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен...")

app.run_polling()
