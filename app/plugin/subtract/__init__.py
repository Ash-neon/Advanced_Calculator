import logging
from app.command import Command
from calculator.operations import subtract
from history.history_manager import HistoryManager  
import multiprocessing

class SubtractCommand(Command):
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, a=None, b=None):
        if a is None or b is None:
            logging.error("Usage: subtract <minuend> <subtrahend>")
            return

        def execute_subtraction(a, b):
            result = subtract(a, b)
            print(f"The result of subtracting {b} from {a} is {result}")
            logging.info(f"The result of subtracting {b} from {a} is {result}")
            # Record the operation in history
            self.history_manager.add_record(a, b, "subtract", result)

        # Create a process for executing the subtraction operation
        process = multiprocessing.Process(target=execute_subtraction, args=(a, b))
        process.start()
        process.join()
