import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# =========================
# إعداد Flask (عشان Render + UptimeRobot)
# =========================
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Bot is running ✅"

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)

# =========================
# إعداد البوت
# =========================

BOT_TOKEN = os.environ.get("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN غير موجود ❌")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت شغال ✅")

def run_bot():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("Bot is running...")
    app.run_polling(close_loop=False)  # ✅ هذا هو الحل المهم

# =========================
# التشغيل
# =========================

if __name__ == "__main__":
    threading.Thread(target=run_flask).start()
    run_bot()
