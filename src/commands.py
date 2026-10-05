def execute(command):

    match command:

        case "/history":
            return ("show history")

        case "/clear":
            return ("history cleard!")

        case _:
            return ("no command found")