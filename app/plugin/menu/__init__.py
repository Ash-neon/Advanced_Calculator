#import logging
from app.command import Command

class MenuCommand(Command):
    def __init__(self, commands):
        self.commands = commands

    def execute(self):
        print("Menu")
        #logging.info("Displaying menu options")
        for command_name in self.commands:
            print(f"- {command_name}")
            #logging.info(f"Command available: {command_name}")
