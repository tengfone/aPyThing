import requests
from telegram.ext import Updater, CommandHandler
import os

PORT = int(os.environ.get('PORT', 5000))
TOKEN = "XXXX"

data = {}


def where(update, context):
    abb = ' '.join(context.args).upper()
    if abb == '':
        context.bot.send_message(chat_id=update.effective_chat.id, text='Please enter a venue like this (e.g. /where '
                                                                        'T1033) '
                                                                        '\U0001F3E2')
        return
    try:
        venue = data[abb]
        text = "*{}*\n\n{}".format(abb, venue)
    except KeyError:
        text = 'Sorry, there is no such place in SP \U0001F622'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text, parse_mode="MarkdownV2")


def food(update, context):
    food_list = '\U00002023 Food Court 1\n' \
                '\U00002023 Food Court 2\n' \
                '\U00002023 Food Court 3 (Food Paradise)\n' \
                '\U00002023 Food Court 4 (Koufu)\n' \
                '\U00002023 Subway\n' \
                '\U00002023 KFC\n' \
                '\U00002023 Bang Deli\n' \
                '\U00002023 Food Court 6\n' \
                '\U00002023 Café @ Moberly'
    context.bot.send_message(chat_id=update.effective_chat.id, text="SP has a lot of places to eat at, here are a "
                                                                    "few to choose from:\n\n" + food_list)


def get_data():
    url = 'https://spreadsheets.google.com/feeds/cells/XXXXXXXXXXXXXXXXXXXXXXXXXXX/1/public/full?alt=json'
    res = requests.get(url=url).json()
    entries = res['feed']['entry']
    for i in range(0, len(entries), 2):
        abb = entries[i]['gs$cell']['inputValue']
        venue = entries[i + 1]['gs$cell']['inputValue']
        data[abb] = venue


def start(update, context):
    get_data()
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Welcome to SP Maps Assistant (SPAM)! You may ask me a random venue '
                                  'like this (e.g. /where T1033)')


def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("food", food))
    dispatcher.add_handler(CommandHandler("where", where))
    dispatcher.add_handler(CommandHandler("start", start))
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://XXXXXXXXXXXXXXXXXXXX.herokuapp.com/' + TOKEN)
    updater.idle()


if __name__ == '__main__':
    main()
