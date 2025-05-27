from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from telegram.error import BadRequest
from keep_alive import keep_alive  # اگر از Railway استفاده می‌کنید، این را حفظ کنید

keep_alive()

# توکن ربات (حتماً توکن صحیح جایگزین شود)
TOKEN = '7667773860:AAEetZ2E-slC8GN3cwJI60rI1P4CgWo27V0'

# کلمات توهین‌آمیز
banned_words = [
    'نفهم', 'احمق', 'احمق!', 'بی‌ادب', 'بیشعور', 'خر', 'گاو', 'کثافت', 'بی‌شعور', 'عوضی',
    'خاک‌برسر', 'لعنتی', 'کونی', 'ناموس‌فروش', 'نامرد', 'بی‌ناموس', 'نفرین', 'دیوث', 'حرومزاده',
    'حرومزاده‌ای', 'دلقک', 'کرم', 'گوه', 'جاکش', 'مادرجنده', 'کسخل', 'جنده', 'کیر', 'کونی', 'کصکش',
    'کسکش', 'خر', 'کص', 'کثیف', 'بی‌همه‌چیز'
]

# جملات توهین‌آمیز
banned_phrases = [
    'بیشعور هستی', 'خیلی بیشعوری', 'تو آدم نیستی', 'برو بمیر', 'دهن‌تو ببند', 'خفه شو',
    'تو عقل نداری', 'برای تو متاسفم', 'خیلی عقده‌ای هستی', 'چه پخی هستی', 'تو زیادی حرف می‌زنی',
    'چقدر بدبختی تو', 'تو اصلاً شعور نداری', 'اگه من جات بودم خجالت می‌کشیدم', 'زر نزن',
    'حرف مفت نزن', 'خیلی خری', 'تو چقدر پستی', 'چه آدم عوضی‌ای هستی', 'برو گم شو',
    'تو نمی‌فهمی', 'باید بری دکتر روانی', 'حالم ازت به‌هم می‌خوره', 'تو یه آشغال به تمام معنا هستی',
    'خفه شو لطفاً', 'هیچی نمی‌فهمی', 'من جات بودم زنده نمی‌موندم', 'بیشعوری در حد تیم ملی'
]

# اجرای چک پیام‌ها و حذف در صورت نیاز
async def delete_bad_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        text = update.message.text.lower()
        user = update.message.from_user.full_name

        # بررسی کلمات ممنوعه
        for word in banned_words:
            if word in text:
                try:
                    await update.message.delete()
                    print(f"❌ پیام حاوی کلمه ممنوعه: '{word}' توسط {user} حذف شد.")
                except BadRequest as e:
                    print(f"⚠️ خطا در حذف پیام: {e}")
                return

        # بررسی عبارات ممنوعه
        for phrase in banned_phrases:
            if phrase in text:
                try:
                    await update.message.delete()
                    print(f"❌ پیام حاوی جمله ممنوعه: '{phrase}' توسط {user} حذف شد.")
                except BadRequest as e:
                    print(f"⚠️ خطا در حذف پیام: {e}")
                return

        print(f"✅ پیام بدون مشکل: {text}")

# راه‌اندازی اپلیکیشن و ثبت هندلر
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, delete_bad_messages))
    print("🤖 ربات با موفقیت راه‌اندازی شد و آماده دریافت پیام است.")
    app.run_polling()