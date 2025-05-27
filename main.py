from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from telegram.error import BadRequest
from keep_alive import keep_alive

# فعال‌سازی برای Railway
keep_alive()

# توکن ربات (جایگزین شده)
TOKEN = '7667773860:AAEetZ2E-slC8GN3cwJI60rI1P4CgWo27V0'

# لیست کلمات توهین‌آمیز
banned_words = [
    'نفهم', 'احمق', 'احمقی', 'خر', 'بیشعور', 'بی‌شعور', 'کثافت', 'گاو', 'عوضی', 'پدرسگ',
    'ریدم', 'ریدم‌تو', 'کونی', 'بی‌ناموس', 'جنده', 'کسخل', 'پدرسگ', 'کسکش',
    'کثیف', 'گوهی', 'کونی', 'کونی‌تر', 'عنتر', 'ننه‌ات', 'ننتو', 'خاک‌برسر',
    'تخم‌حروم', 'عوضیا', 'عنتر', 'پفیوز', 'بی‌ناموس', 'فاک', 'fuck',
    'کسافت', 'گوه', 'ریدم', 'چرت', 'بی‌سواد', 'نفهم‌ها', 'کس‌ننه‌ت', 'بی‌ادب',
    'حیوان', 'خراب', 'یابو', 'یابوی', 'نجس', 'سوسک', 'گوزو', 'شاشو'
]

# لیست جملات توهین‌آمیز
banned_phrases = [
    'بخور بمیر', 'تخم حرومی', 'خاک‌بر سرت', 'آدم نیستی', 'کونی مادر', 'تو هیچی نیستی',
    'ریدم تو وجودت', 'عقل نداری', 'اگه آدم بودی', 'بیشعور بیشعور', 'تف به روت', 'توی بیشعور',
    'خر فرضت کردم', 'ننتو باید', 'چته تو', 'ساکت شو', 'حرومزاده', 'بی‌شعور', 'بی‌تربیت', 'دهنتو ببند',
    'گوه نخور', 'پفیوز', 'بی‌شخصیت', 'کس‌ننه‌ت', 'کس‌کش', 'لعنتی', 'پدر سگ', 'عوضی'
]

# حذف پیام‌های توهین‌آمیز
async def delete_bad_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        text = update.message.text.lower()
        user = update.message.from_user.full_name
        chat_id = update.message.chat_id

        for word in banned_words:
            if word in text:
                try:
                    await context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
                    print(f"❌ پیام حاوی کلمه توهین‌آمیز حذف شد از طرف {user}")
                    return
                except BadRequest as e:
                    print(f"خطا در حذف پیام: {e}")

        for phrase in banned_phrases:
            if phrase in text:
                try:
                    await context.bot.delete_message(chat_id=chat_id, message_id=update.message.message_id)
                    print(f"❌ پیام حاوی جمله توهین‌آمیز حذف شد از طرف {user}")
                    return
                except BadRequest as e:
                    print(f"خطا در حذف پیام: {e}")

# اجرای ربات
async def main():
    app = ApplicationBuilder().token(TOKEN).build()

    # 🚨 حذف Webhook برای جلوگیری از Conflict
    await app.bot.delete_webhook(drop_pending_updates=True)

    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), delete_bad_messages))
    print("🤖 ربات با موفقیت راه‌اندازی شد و آماده دریافت پیام است.")
    await app.run_polling()

# اجرای main
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())