class MessageArray:
    def __init__(self):
        self.messages_array = []

    def add_question_message(self, content_string):
        self.messages_array.append({'role': 'user', 'content': f'{content_string}'})

    def add_res_message(self, content_string):
        self.messages_array.append({'role': 'assistant', 'content': f'{content_string}'})

    def to_list(self):
        return self.messages_array 
