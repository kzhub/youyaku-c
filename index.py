import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

def send_to_chatgpt(messages_array):
    client = OpenAI()
    client.api_key = os.getenv("OPENAI_API_KEY")
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages_array
    )
    return response.choices[0].message.content


# URLを指定
url = 'https://toylog.vercel.app/'

# ページを取得
response = requests.get(url)

message_array = []

if response.status_code == 200:
    # BeautifulSoupでHTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()  # 本文を取得
    print(f'ページの本文: {content}')

    # ユーザーに確認
    user_input = input('このページの内容を質問しますか (y/n): ')
    if user_input.lower() == 'y':
        question = input('質問内容を入力してください: ')
        intquestion = {'role': 'user', 'content': f'{content}に対するユーザーの以下の質問に答えて: {question}'}
        message_array.append(intquestion)
        response_from_chatgpt = send_to_chatgpt(message_array)
        
        print(f'ChatGPTのレスポンス: {response_from_chatgpt}')

        message_array.append({'role': 'assistant', 'content': f'{response_from_chatgpt}'}) 
        
        while True:
            follow_up = input('追加の質問をしますか (y/n): ')
            if follow_up.lower() == 'y':
                follow_up_question = input('質問内容を入力してください: ')
                message_array.append({'role': 'user', 'content': f'{follow_up_question}'})
                follow_up_res =  send_to_chatgpt(message_array)
                print(f'ChatGPTのレスポンス: {follow_up_res}')
                message_array.append({'role': 'assistant', 'content': f'{follow_up_res}'}) 
            else:
                print('処理を終了します。')
                break
    else:
        print('処理を終了します。')