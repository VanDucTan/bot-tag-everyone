import nest_asyncio
nest_asyncio.apply()

from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

TOKEN = '7505319345:AAGtRN9r56_lc-rKJXNzxtzThtBXIA2LxLk'

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Bot đã sẵn sàng!')

async def tag_all(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    members = await context.bot.get_chat_administrators(chat_id)
    
    tags = ' '.join([f'@{member.user.username}' for member in members if member.user.username])
    
    if tags:
        await update.message.reply_text(tags)
    else:
        await update.message.reply_text("Không tìm thấy username cho các thành viên.")

async def tag_all_pin(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    members = await context.bot.get_chat_administrators(chat_id)
    
    tags = ' '.join([f'@{member.user.username}' for member in members if member.user.username])
    
    if tags:
        await update.message.reply_text(tags)
        await context.bot.pin_chat_message(chat_id, update.message.message_id)
    else:
        await update.message.reply_text("Không tìm thấy username cho các thành viên.")

async def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('all', tag_all))
    application.add_handler(CommandHandler('allpin', tag_all_pin))

    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
