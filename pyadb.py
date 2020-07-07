from PyInquirer import prompt
from utils import *
import json

global SERIAL


def display_cli_menu():
    f = open("adb_commands.json")
    command_map = json.load(f)
    stop_it = False
    while not stop_it:
        questions = [
            {
                'type': 'list',
                'name': 'command',
                'message': 'Adb Command',
                'choices': command_map.keys(),
            }
        ]
        answers = prompt(questions)
        command_to_exec = command_map[answers["command"]]
        SERIAL = device_serial()
        launch_adb(command_to_exec, SERIAL)
        stop_it = ask_user()


def ask_user():
    questions = [
        {
            'type': 'confirm',
            'name': 'stopIt',
            'message': 'Continue?',
            'default': True,
        }
    ]
    answers = prompt(questions)
    return not answers["stopIt"]


def device_serial():
    devices = list_devices()
    questions = [
        {
            'type': 'list',
            'name': 'selected_dev',
            'message': 'Which device?',
            'choices': devices
        }
    ]
    answers = prompt(questions)
    return answers["selected_dev"].split(" ")[0]


if __name__ == '__main__':
    display_cli_menu()
