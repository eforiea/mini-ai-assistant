from llm import ask_ai
from commands import execute
from rag import rag

class Assistant:

    history = []

    def process(self, user_input):

        if user_input[0] == '/':

            return execute(user_input)

        elif user_input[0] == '?':

            return rag(user_input)

        else:

             return ask_ai(user_input)