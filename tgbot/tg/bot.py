from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Updater, CallbackQueryHandler, CommandHandler
import os

from tgbot.tg.models import Question

token = '1222979762:AAHIufxAi0tnQlOc-uIS9ckSJQywAuhECTw'
#token = os.environ.get("TG_BOT_TOKEN", "")

updater = Updater(token=token, use_context=True)

dispatcher = updater.dispatcher


class QuestionRelyKeyBoard(InlineKeyboardMarkup):
    def __init__(self,  **kwargs):
        questions = Question.objects.all().get()
        buttons = [InlineKeyboardButton(text=str(q.ask), callback_data="q" + str(q.id)) for q in questions]
        super().__init__([buttons], **kwargs)


def start(update, context):
    update.effective_message.reply_text(reply_markup=QuestionRelyKeyBoard(),text="Привет я бот и я буду отвечать на твои волрпосы")

def show_answer(update, context):
    query = update.callback_query
    query.answer()
    q_id =  int(str(query.data)[1:])
    question = Question.objects.all().get(id=q_id)
    reply_markup = QuestionRelyKeyBoard()
    query.edit_message_text(
        text=question.answer,
        reply_markup=reply_markup
    )

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CallbackQueryHandler(show_answer, pattern=r"^q"))

updater.start_polling()

updater.idle()
