from chathandler import ChatHandler

parse_site_url = 'https://toylog.vercel.app/'
user_input = input('このページの内容を質問しますか (y/n): ')

if user_input.lower() == 'y':
    chat_handler = ChatHandler(parse_site_url)
    chat_handler.ask_question()
    chat_handler.handle_follow_up()
else:
    print('処理を終了します。')