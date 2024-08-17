class Message:
    def __init__(self):
        self.__array = []

    @property
    def array(self):
        return self.__array

    def add_question_message(self, content_string):
        self.__array.append({'role': 'user', 'content': f'{content_string}'})

    def add_res_message(self, content_string):
        self.__array.append({'role': 'assistant', 'content': f'{content_string}'})