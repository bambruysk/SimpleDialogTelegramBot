from telegram.ext import Updater
import os
token = os.environ.get("TG_BOT_TOKEN", "")


updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

