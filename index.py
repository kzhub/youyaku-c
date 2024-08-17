from chathandler import ChatHandler

parse_site_url = 'SITE_URL'

chat_handler = ChatHandler(parse_site_url)
if not chat_handler.confirm_question():
    exit()
chat_handler.ask_question()
chat_handler.handle_follow_up()
