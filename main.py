#!/usr/bin/env python
# pylint: disable=C0116
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
from time import gmtime, strftime
from telegram import Update, ForceReply, InlineKeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from googletrans import Translator  #pip install googletrans==3.1.0a0


# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
def start(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hi {user.mention_markdown_v2()}\!',
        
    )
    update.message.reply_text("Send me text in any language and I will translate and send this in Hindi with pronunciation.😌😎",
        reply_markup=ForceReply(selective=True)
    )

    update.message.reply_text("Please visit my Youtube channel and Subscirbe it.!!😚\nhttps://t.ly/2PrB")


def time_cmd(update: Update, _: CallbackContext) -> None:
    """Send a current time when the command /time is issued."""
    
    c_time = strftime("%H:%M:%S", gmtime())
    t_date = strftime("%d-%m-%Y",gmtime())
    update.message.reply_text(f"Today's Date📅 : {t_date}\nCurrent Time⏲ : {c_time}")

def stop(update: Update, _:CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text("Hey dude!\nWhy are you stopping this bot?\nThis is so useful bot.🤓😉")

def help_command(update: Update, _: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text("Contact me at💬: @mr_vaibhavmaheshwari_chatbot")

def contact(update, context):
    """Send a message when the command /contact is issued."""
    update.message.reply_text("Contact me at💬: @mr_vaibhavmaheshwari_chatbot \nOr \nClick Here: /help")


def translate_cmd(update: Update, _: CallbackContext) -> None:

    """Echo the user message."""
    language_1 = update.message.text
    cl = "hi"
    tr = Translator()
    output = tr.translate(language_1, dest=cl)
    msg_out = output.text
    proun = output.pronunciation
    if proun == None:
        prounc = "Not Available!!"
    else:
        prounc = proun

    update.message.reply_text(f"From : English\nTo : Hindi \nText : {language_1}\nTranslate : {msg_out}\nProunciation : {prounc}")
    update.message.reply_text("Keep Smiling, Be Happy!!😇😇")


def main() -> None:
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    api_token = "Paste your Api token here" #Go to botfather and get your api.
    updater = Updater(api_token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("contact",contact))
    dispatcher.add_handler(CommandHandler("stop",stop))
    dispatcher.add_handler(CommandHandler("time",time_cmd))

    # on non command i.e message - translate the message on Telegram
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_cmd))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
