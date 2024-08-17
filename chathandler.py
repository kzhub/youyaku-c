from message import Message
from modules import send_to_chatgpt, parse_html, handle_chatgpt_response

class ChatHandler:
    def __init__(self, url):
        self._content = parse_html(url)
        self._messages = Message()

    def ask_question(self):
        question = input('質問内容を入力してください: ')
        self._messages.add_question_message(f'{self._content}に対するユーザーの以下の質問に答えて: {question}')
        response = send_to_chatgpt(self._messages.array)
        handle_chatgpt_response(response, self._messages)

    def handle_follow_up(self):
        while True:
            follow_up = input('追加の質問をしますか (y/n): ')
            if follow_up.lower() == 'y':
                follow_up_question = input('質問内容を入力してください: ')
                self._messages.add_question_message(f'{follow_up_question}')
                response = send_to_chatgpt(self._messages.array)
                handle_chatgpt_response(response, self._messages)
            else:
                print('処理を終了します。')
                break