import nest_asyncio
nest_asyncio.apply()

from telegram import Update, ChatMember, ChatMemberUpdated
from telegram.ext import Application, CommandHandler, ChatMemberHandler, CallbackContext

TOKEN = '7505319345:AAGtRN9r56_lc-rKJXNzxtzThtBXIA2LxLk'

# Store members in a simple list for demonstration
# In a production scenario, consider using a persistent storage solution (e.g., a database)
members_list = []

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Bot đã sẵn sàng!')

async def new_member(update: Update, context: CallbackContext) -> None:
    if update.chat_member.new_chat_member.status == 'member':
        username = update.chat_member.new_chat_member.user.username
        if username and username not in members_list:
            members_list.append(username)

async def tag_all(update: Update, context: CallbackContext) -> None:
    if members_list:
        tags = ' '.join([f'@{username}' for username in members_list])
        await update.message.reply_text(tags)
    else:
        await update.message.reply_text("Không tìm thấy username cho các thành viên.")

async def tag_all_pin(update: Update, context: CallbackContext) -> None:
    if members_list:
        tags = ' '.join([f'@{username}' for username in members_list])
        message = await update.message.reply_text(tags)
        await context.bot.pin_chat_message(update.message.chat_id, message.message_id)
    else:
        await update.message.reply_text("Không tìm thấy username cho các thành viên.")

async def main() -> None:
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('all', tag_all))
    application.add_handler(CommandHandler('allpin', tag_all_pin))
    application.add_handler(ChatMemberHandler(new_member, ChatMemberHandler.MY_CHAT_MEMBER))

    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
