# from telegram import Update
# from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# from config import TELEGRAM_BOT_TOKEN
# from codeforces_api import get_user_rating
# from problem_selector import get_problem_for_rating

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text("👋 Hello! Use /daily <your_handle> to get a daily Codeforces problem!")

# async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if not context.args:
#         await update.message.reply_text("❗ Please send your Codeforces handle.\nExample: /daily tourist")
#         return

#     handle = context.args[0]
#     rating = get_user_rating(handle)

#     if rating is None:
#         await update.message.reply_text("❌ Couldn't fetch rating. Check the handle.")
#         return

#     problem = get_problem_for_rating(rating)
#     if not problem:
#         await update.message.reply_text("⚠️ No suitable problem found.")
#         return

#     await update.message.reply_text(
#         f"🎯 Problem for you: [{problem['name']}]({problem['url']})",
#         parse_mode='Markdown'
#     )

# def run_bot():
#     app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
#     app.add_handler(CommandHandler("start", start))
#     app.add_handler(CommandHandler("daily", daily))
#     app.run_polling()

# if __name__ == "__main__":
#     run_bot()
# from telegram import Update
# from telegram.ext import (
#     ApplicationBuilder,
#     CommandHandler,
#     ContextTypes,
# )
# from config import TELEGRAM_BOT_TOKEN
# from codeforces_api import get_user_rating
# from problem_selector import get_problem_for_rating
# from database import init_db, add_user, remove_user, get_all_users

# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from apscheduler.triggers.cron import CronTrigger
# import pytz
# import asyncio
# import logging

# # ─────────────────────────── Bot Commands ─────────────────────────── #

# async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text(
#         "👋 Welcome to Codeforces Daily Bot!\n"
#         "Use /register <handle> to receive daily problems.\n"
#         "Use /unregister to stop.\n"
#         "Use /daily <handle> to get one immediately."
#     )

# async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if not context.args:
#         await update.message.reply_text("❗ Usage: /register <codeforces_handle>")
#         return

#     handle = context.args[0]
#     rating = get_user_rating(handle)
#     if rating is None:
#         await update.message.reply_text("❌ Invalid Codeforces handle or network error.")
#         return

#     add_user(update.effective_user.id, handle)
#     await update.message.reply_text(f"✅ Registered! You'll get daily problems for `{handle}`.", parse_mode='Markdown')

# async def unregister(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     remove_user(update.effective_user.id)
#     await update.message.reply_text("❌ You’ve been unregistered from daily problems.")

# async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     if not context.args:
#         await update.message.reply_text("❗ Usage: /daily <handle>")
#         return

#     handle = context.args[0]
#     rating = get_user_rating(handle)
#     if rating is None:
#         await update.message.reply_text("❌ Couldn't fetch your rating. Check your handle.")
#         return

#     problem = get_problem_for_rating(rating)
#     if not problem:
#         await update.message.reply_text("⚠️ No suitable problem found.")
#         return

#     await update.message.reply_text(
#         f"🎯 Problem for you: [{problem['name']}]({problem['url']})",
#         parse_mode='Markdown'
#     )

# # ─────────────────────── Daily Scheduled Sender ───────────────────── #

# async def send_daily_problems(application):
#     users = get_all_users()
#     for telegram_id, handle in users:
#         rating = get_user_rating(handle)
#         if rating is None:
#             continue

#         problem = get_problem_for_rating(rating)
#         if not problem:
#             continue

#         try:
#             await application.bot.send_message(
#                 chat_id=telegram_id,
#                 text=f"📌 Your daily Codeforces problem:\n[{problem['name']}]({problem['url']})",
#                 parse_mode='Markdown'
#             )
#         except Exception as e:
#             print(f"❌ Error sending to {telegram_id}: {e}")

# # ───────────────────────────── Run Bot ────────────────────────────── #

# def run_bot():
#     logging.basicConfig(level=logging.INFO)
#     init_db()  # setup SQLite table

#     async def main():
#         app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

#         # Command Handlers
#         app.add_handler(CommandHandler("start", start))
#         app.add_handler(CommandHandler("register", register))
#         app.add_handler(CommandHandler("unregister", unregister))
#         app.add_handler(CommandHandler("daily", daily))

#         # Scheduler Setup: every day at 9:00 AM IST
#         scheduler = AsyncIOScheduler()
#         scheduler.add_job(
#             send_daily_problems,
#             trigger=CronTrigger(hour=9, minute=0, timezone=pytz.timezone("Asia/Kolkata")),
#             args=[app]
#         )
#         scheduler.start()

#         # Start polling
#         await app.run_polling()

#     asyncio.run(main())

# if __name__ == "__main__":
#     run_bot()
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)
from config import TELEGRAM_BOT_TOKEN
from codeforces_api import get_user_rating
from problem_selector import get_problem_for_rating
from database import init_db, add_user, remove_user, get_all_users

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
import asyncio
import logging

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to Codeforces Daily Bot BY DEV!\n"
        "Use /register <handle> to receive daily problems.\n"
        "Use /unregister to stop.\n"
        "Use /daily <handle> to get one immediately."
    )

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ Usage: /register <codeforces_handle>")
        return

    handle = context.args[0]
    rating = get_user_rating(handle)
    if rating is None:
        await update.message.reply_text("❌ Invalid Codeforces handle or network error.")
        return

    add_user(update.effective_user.id, handle)
    await update.message.reply_text(f"✅ Registered! You'll get daily problems for `{handle}`.", parse_mode='Markdown')

async def unregister(update: Update, context: ContextTypes.DEFAULT_TYPE):
    remove_user(update.effective_user.id)
    await update.message.reply_text("❌ You’ve been unregistered from daily problems.")

async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ Usage: /daily <handle>")
        return

    handle = context.args[0]
    rating = get_user_rating(handle)
    if rating is None:
        await update.message.reply_text("❌ Couldn't fetch your rating. Check your handle.")
        return

    problem = get_problem_for_rating(rating)
    if not problem:
        await update.message.reply_text("⚠️ No suitable problem found.")
        return

    await update.message.reply_text(
        f"🎯 Problem for you: [{problem['name']}]({problem['url']})",
        parse_mode='Markdown'
    )

async def send_daily_problems(application):
    users = get_all_users()
    for telegram_id, handle in users:
        rating = get_user_rating(handle)
        if rating is None:
            continue
        problem = get_problem_for_rating(rating)
        if not problem:
            continue
        try:
            await application.bot.send_message(
                chat_id=telegram_id,
                text=f"📌 Your daily Codeforces problem:\n[{problem['name']}]({problem['url']})",
                parse_mode='Markdown'
            )
        except Exception as e:
            print(f"❌ Error sending to {telegram_id}: {e}")

def run_bot():
    logging.basicConfig(level=logging.INFO)
    init_db()

    async def main():
        app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("register", register))
        app.add_handler(CommandHandler("unregister", unregister))
        app.add_handler(CommandHandler("daily", daily))

        scheduler = AsyncIOScheduler()
        scheduler.add_job(
            send_daily_problems,
            trigger=CronTrigger(hour=9, minute=0, timezone=pytz.timezone("Asia/Kolkata")),
            args=[app]
        )
        scheduler.start()

        await app.run_polling()

    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except RuntimeError:
        import nest_asyncio
        nest_asyncio.apply()
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())

if __name__ == "__main__":
    run_bot()
