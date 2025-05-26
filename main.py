
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from telegram.error import BadRequest
from keep_alive import keep_alive

# فعال نگه داشتن سرور (برای Railway)
keep_alive()

# توکن ربات
TOKEN = '7667773860:AAEetZ2E-slC8GN3cwJI60rI1P4CgWo27V0'

# لیست کلمات ممنوعه
banned_words = [
    'نفهم', 'بی‌ادب', 'احمق', 'خر', 'کثافت', 'پفیوز', 'جاکش', 'جنده',
    'بی‌شعور', 'بی شعور', 'گاو', 'عوضی', 'بیشعور', 'کونی', 'حرومزاده', 'لعنتی',
    'بی‌تربیت', 'کصشر', 'چرت نگو', 'زر نزن', 'زرزر', 'خفه شو', 'دهنتو ببند',
    'پدرسگ', 'خنگ', 'نکبت', 'خایه', 'تخم', 'تُف', 'چوس', 'عن', 'کوفت',
    'کیر', 'کص', 'کصافط', 'گوه', 'کون', 'اوباش'
]

# لیست جملات توهین‌آمیز
banned_phrases = [
    'شعور نداری', 'تو آدم نیستی', 'برو بمیر', 'خفه شو',
    'زر نزن', 'خیلی خری', 'تو عقده‌ای هستی', 'تو نمی‌فهمی',
    'گوه نخور', 'کیرت رو جمع کن', 'دهنت بوی گه میده', 'تو ادب نداری'
]

# هندلر اصلی پاک‌کننده پیام‌های بد
async def delete_bad_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        text = update.message.text.lower()
        user = update.message.from_user.full_name
        chat_id = update.effective_chat.id

        print(f"📩 دریافت پیام: {text} از طرف {user} (chat_id: {chat_id})")

        # بررسی کلمات ممنوعه
        if any(bad_word in text for bad_word in banned_words + banned_phrases):
            await update.message.delete()
            await context.bot.send_message(
                chat_id=chat_id,
                text=f"⚠️ {user} عزیز، لطفاً رعایت ادب رو داشته باشید. پیام شما حذف شد."
            )
            print(f"🚨 پیام حاوی توهین حذف شد: {text}")
        else:
            print("✅ پیام مشکلی نداشت.")

# هندلر برای لاگ‌کردن خطاها
async def handle_errors(update: object, context: ContextTypes.DEFAULT_TYPE):
    try:
        raise context.error
    except BadRequest as e:
        print(f"❌ BadRequest: {e}")
    except Exception as e:
        print(f"❗ Exception: {e}")

# اجرای اپلیکیشن
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, delete_bad_messages))
app.add_error_handler(handle_errors)

print("🤖 ربات با موفقیت راه‌اندازی شد و آماده دریافت پیام است.")
app.run_polling()