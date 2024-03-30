import logging
from abc import ABC, abstractmethod
from decimal import Decimal, InvalidOperation
import sys

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        if command_name == "exit":
            print("Exiting the program. Goodbye!")
            sys.exit(0)
        try:
            command = self.commands[command_name]
            if command_name in ['add', 'subtract', 'multiply', 'divide']:
                a = Decimal(input("Enter first number: "))
                b = Decimal(input("Enter second number: "))
                command.execute(a, b)
            elif command_name == 'history':
                command.execute()
            else:
                command.execute()

        except KeyError:
            print(f"No such command: {command_name}")
            logger.error(f"No such command: {command_name}")
        except InvalidOperation:
            print("Invalid input. Please enter a valid number.")
            logger.error("Invalid input. Please enter a valid number.")
    
    def get_command_names(self):
        """Return a list of registered command names."""
        return list(self.commands.keys())
