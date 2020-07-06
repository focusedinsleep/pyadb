from PyInquirer import prompt

# using PyInquirer, a choice menu
def display_cli_menu(command_map):
    stop_it = False
    while not stop_it:
        questions = [
            {
                'type': 'list',
                'name': 'command',
                'message': 'Adb Command',
                'choices': command_map,
            }
        ]
        answers = prompt(questions)
        print(answers["command"])
        launch_adb(answers["command"])
        questions = [
            {
                'type': 'confirm',
                'name': 'stopIt',
                'message': 'Terminate Program?',
                'default': False,
            }
        ]
        answers = prompt(questions)
        if answers["stopIt"] is True:
            stop_it = True
