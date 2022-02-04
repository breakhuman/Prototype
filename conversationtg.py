def start(update, context):
    update.message.reply_text("""
안녕하세요! 저는 덕덕이의 봇 이에요.
b16, b32, b64, b85, crc32, uuid1, uuid3, uuid4, uuid5, bsecret, hsecret, usecret 암호문을 변환 할 수 있습니다.
모든 죄를 저에게 덮어 씌우세요!!
사용법을 모르시겠다면 /help 명령어를 사용하여 사용법을 확인해주세요.
""")

def help(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text="Commands:\n\n"
                                  "BASE64로 암호화 할시: /b64e <code>코드</code>\n"
                                  "BASE64 해독 할시: /b64d <code>코드</code>",
                             parse_mode=ParseMode.HTML)