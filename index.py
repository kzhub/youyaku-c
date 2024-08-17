from message import Message
from modules import send_to_chatgpt, parse_html, handle_chatgpt_response

parse_site_url = 'https://toylog.vercel.app/'

content = parse_html(parse_site_url)

user_input = input('このページの内容を質問しますか (y/n): ')


if user_input.lower() == 'y':
    messages= Message()
    question = input('質問内容を入力してください: ')
    messages.add_question_message(f'{content}に対するユーザーの以下の質問に答えて: {question}')

    response_from_chatgpt = send_to_chatgpt(messages.array)
    handle_chatgpt_response(response_from_chatgpt, messages)
    
    while True:
        follow_up = input('追加の質問をしますか (y/n): ')
        if follow_up.lower() == 'y':
            follow_up_question = input('質問内容を入力してください: ')
            messages.add_question_message( f'{follow_up_question}')
            
            follow_up_res =  send_to_chatgpt(messages.array)
            handle_chatgpt_response(follow_up_res, messages)
        else:
            print('処理を終了します。')
            break
else:
    print('処理を終了します。')