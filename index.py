import os
import requests
from bs4 import BeautifulSoup
from openai import OpenAI

def send_to_chatgpt(propmpt):
    client = OpenAI()
    client.api_key = os.getenv("OPENAI_API_KEY")
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{'role': 'user', 'content': propmpt}]
    )
    return 

# URLを指定
url = 'https://example.com/'

# ページを取得
response = requests.get(url)

if response.status_code == 200:
  # BeautifulSoupでHTMLを解析
  soup = BeautifulSoup(response.text, 'html.parser')
  content = soup.get_text()  # 本文を取得
  print(f'ページの本文: {content}')
  
  # ユーザーに確認
  user_input = input('このページの内容を質問しますか (y/n): ')
  if user_input.lower() == 'y':
      question = input('質問内容を入力してください: ')
      response_from_chatgpt = send_to_chatgpt(f'{content}に対するユーザーの以下の質問に答えて: {question}')
      
      # レスポンスを表示
      print(f'ChatGPTのレスポンス: {response_from_chatgpt}')
      
  else:
      print('処理を終了します。')