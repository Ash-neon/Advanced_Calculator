import logging
from app.command import Command
from calculator.operations import add
import multiprocessing



class AddCommand(Command):
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, a=None, b=None):
        if a is None or b is None:
            logging.error("Usage: add <number1> <number2>")
            return

        def execute_addition(a, b):
            result = add(a, b)
            print(f"The result of adding {b} from {a} is {result}")
            logging.info(f"The result of adding {b} from {a} is {result}")
            # Record the operation in history
            self.history_manager.add_record(a, b, "add", result)

        # Create a process for executing the addition operation
        process = multiprocessing.Process(target=execute_addition, args=(a, b))
        process.start()
        process.join()
