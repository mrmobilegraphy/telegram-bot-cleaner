
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from telegram.error import BadRequest
from keep_alive import keep_alive
keep_alive()

# توکن ربات
TOKEN = '7667773860:AAEetZ2E-slC8GN3cwJI60rI1P4CgWo27V0'

# لیست کلمات توهین‌آمیز
banned_words = [
    'نفهم', 'احمق', 'احمق!', 'بی‌ادب', 'بیشعور', 'خر', 'گاو', 'کثافت', 'بی‌شعور', 'عوضی',
    'خاک‌برسر', 'لعنتی', 'کونی', 'ناموس‌فروش', 'نامرد', 'بی‌ناموس', 'نفرین', 'دیوث', 'حرومزاده',
    'حرومزاده‌ای', 'دلقک', 'کرم', 'گوه', 'جاکش', 'مادرجنده', 'کسخل', 'جنده', 'کیر', 'کصکش',
    'کسکش', 'کص', 'کثیف', 'بی‌همه‌چیز'
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

# لیست انگلیسی‌های توهین‌آمیز رایج در فارسی
banned_english = [
    'fuck', 'shit', 'bitch', 'asshole', 'dumb', 'idiot', 'retard', 'loser',
    'son of a bitch', 'stfu', 'saket', 'haramzadeh', 'khaye', 'khar', 'koskhol',
    'koskholi', 'koskholha', 'koskholhay', 'kirm', 'konde', 'koni', 'jende'
]

# تابع اصلی برای حذف پیام‌های توهین‌آمیز
async def delete_bad_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        text = update.message.text.lower()
        user = update.message.from_user.full_name

        if any(bad_word in text for bad_word in banned_words) or \
           any(bad_phrase in text for bad_phrase in banned_phrases) or \
           any(bad_eng in text for bad_eng in banned_english):
            try:
                await update.message.delete()
                print(f"❌ پیام از {user} حذف شد: {text}")
            except BadRequest as e:
                print(f"⚠️ خطا در حذف پیام: {e}")
        else:
            print(f"✅ پیام مشکلی نداشت: {text}")

# راه‌اندازی ربات
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, delete_bad_messages))
    print("🤖 ربات با موفقیت راه‌اندازی شد و آماده‌ی دریافت پیام است.")
    app.run_polling()