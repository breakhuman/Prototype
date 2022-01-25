# module or another variable, defines list
from urllib import response
from tgkey import id
from telegram import *
from telegram.ext import *
import bornbot as b

# running print
print('동작중....')

#####################################################################

#####################################################################

# def list
def start_command(update, context):
    update.message.reply_text('안녕하세요!\n저는 베타봇 이에요!')
    
def help_command(update, context):
    update.message.reply_text('도움이 필요하다면 @a1dmin9271 에서 아이디를 찾아 연락주세요!')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = b.sample_respornses(text)
    
    update.message.reply_text(response)
    
def error(update, context):
    print(f"Update {update} caused error {context.error}")


# main
def main():
    updater = Updater(id, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)
    
    updater.start_polling()
    updater.idle()

main()


