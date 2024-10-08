from message import Message
from modules import send_to_chatgpt, parse_html

class ChatHandler:
    def __init__(self, url):
        self._content = parse_html(url)
        self._messages = Message()

    def confirm_question(self):
        print(self._content)
        user_input = input('このページの内容を質問しますか (y/n): ')
        return user_input.lower() == 'y'

    def ask_question(self):
        question = input('質問内容を入力してください: ')
        self._messages.add_question_message(f'{self._content}に対するユーザーの以下の質問に答えて: {question}')
        response = send_to_chatgpt(self._messages.array)
        _handle_chatgpt_response(response)

    def handle_follow_up(self):
        while True:
            follow_up = input('追加の質問をしますか (y/n): ')
            if follow_up.lower() == 'y':
                follow_up_question = input('質問内容を入力してください: ')
                self._messages.add_question_message(f'{follow_up_question}')
                response = send_to_chatgpt(self._messages.array)
                _handle_chatgpt_response(response)
            else:
                print('処理を終了します。')
                break

    def _handle_chatgpt_response(response):
        print(f'ChatGPTのレスポンス: {response}')
        self._messages.add_res_message(f'{response}')