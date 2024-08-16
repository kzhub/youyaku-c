import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

def send_to_chatgpt(messages_array):
    client = OpenAI()
    client.api_key = os.getenv("OPENAI_API_KEY")
    messages_list = messages_array.to_list() 
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages_list
    )
    return response.choices[0].message.content

def parse_html(url):
    response = requests.get(url)
    if response.status_code != 200:
        print('ページの取得に失敗しました。ステータスコード:', response.status_code)
        exit()

    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.get_text()  # 本文を取得
    print(f'ページの本文: {content}')
    return content

def handle_chatgpt_response(response, message_history):
    print(f'ChatGPTのレスポンス: {response}')
    message_history.add_res_message(f'{response}')