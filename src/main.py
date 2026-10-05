from assistant import Assistant

assistant = Assistant()

while True:

    user_input = input("USER: ")

    if user_input.lower() == 'exit':

        break

    print(assistant.process(user_input))