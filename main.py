from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from telegram.error import BadRequest
from keep_alive import keep_alive

keep_alive()  # فعال‌سازی سرور برای Railway

# ✅ توکن نهایی ربات
TOKEN = '7667773860:AAEetZ2E-slC8GN3cwJI60rI1P4CgWo27V0'

# 🟥 کلمات توهین‌آمیز
banned_words = [
    'نفهم', 'احمق', 'احمق!', 'بی‌ادب', 'بیشعور', 'خر', 'گاو', 'کثافت', 'بی‌شعور', 'عوضی',
    'خاک‌برسر', 'لعنتی', 'کونی', 'ناموس‌فروش', 'نامرد', 'بی‌ناموس', 'نفرین', 'دیوث', 'حرومزاده',
    'حرومزاده‌ای', 'دلقک', 'کرم', 'گوه', 'جاکش', 'مادرجنده', 'کسخل', 'جنده', 'کیر', 'کصکش',
    'کسکش', 'کص', 'کثیف', 'بی‌همه‌چیز'
]

# 🟧 جملات توهین‌آمیز
banned_phrases = [
    'بیشعور هستی', 'خیلی بیشعوری', 'تو آدم نیستی', 'برو بمیر', 'دهن‌تو ببند', 'خفه شو',
    'تو عقل نداری', 'برای تو متاسفم', 'خیلی عقده‌ای هستی', 'چه پخی هستی', 'تو زیادی حرف می‌زنی',
    'چقدر بدبختی تو', 'تو اصلاً شعور نداری', 'اگه من جات بودم خجالت می‌کشیدم', 'زر نزن',
    'حرف مفت نزن', 'خیلی خری', 'تو چقدر پستی', 'چه آدم عوضی‌ای هستی', 'برو گم شو',
    'تو نمی‌فهمی', 'باید بری دکتر روانی', 'حالم ازت به‌هم می‌خوره', 'تو یه آشغال به تمام معنا هستی',
    'خفه شو لطفاً', 'هیچی نمی‌فهمی', 'من جات بودم زنده نمی‌موندم', 'بیشعوری در حد تیم ملی'
]

# ✂️ حذف پیام‌های حاوی توهین
async def delete_bad_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        text = update.message.text.lower()
        user = update.message.from_user.full_name

        if any(word in text for word in banned_words) or any(phrase in text for phrase in banned_phrases):
            try:
                await update.message.delete()
                print(f"🚫 پیام حاوی توهین از {user} حذف شد.")
            except BadRequest as e:
                print(f"❌ خطا در حذف پیام از {user}: {e}")
        else:
            print(f"✅ پیام سالم از {user}: {text}")

# ⚙️ اجرای ربات
async def main():
    application = ApplicationBuilder().token(TOKEN).build()
    await application.bot.delete_webhook(drop_pending_updates=True)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, delete_bad_messages))

    print("🤖 ربات با موفقیت راه‌اندازی شد و آماده‌ی دریافت پیام است.")
    await application.run_polling()

# 🧠 اجرای تابع اصلی
if __name__ == '__main__':
    import asyncio
    asyncio.run(main())