bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "8636158499:AAE9tAAUSbROKfipRbdiBKeV2pZGF6dxKu0"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    text = """
🚀 ORDERPRO — Центр приёма заказов

Добро пожаловать!

Вы подключены к системе приёма задач OrderPro.
Я цифровой ассистент, который помогает быстро оформить заказ и передать его специалисту.

📌 Как это работает:

1️⃣ Вы отправляете описание задачи
2️⃣ Система регистрирует и анализирует заказ
3️⃣ Специалист связывается с вами

Чтобы начать, отправьте одним сообщением:

🛠 Что нужно сделать
💰 Примерный бюджет
⏳ Срок выполнения

Пример заказа:

Создать Telegram-бота для интернет-магазина
Бюджет: 5000
Срок: 3 дня

⚡ Обычно ответ специалиста занимает 5–10 минут.
🔒 Все заявки автоматически фиксируются в системе.
"""

    await update.message.reply_text(text)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    await update.message.reply_text("✅ Заказ получен. Специалист изучит его и скоро свяжется с вами.")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("OrderPro бот запущен")

app.run_polling()
