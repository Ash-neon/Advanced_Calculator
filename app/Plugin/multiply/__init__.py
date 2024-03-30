import logging
from app.command import Command
from calculator.operations import multiply
from decimal import Decimal
import multiprocessing

class MultiplyCommand(Command):
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self, a=None, b=None):
        if a is None or b is None:
            logging.error("Usage: multiply <factor1> <factor2>")
            return

        def execute_multiplication(a, b):
            result = multiply(a, b)
            logging.info(f"The result of multiplying {a} and {b} is {result}")
            print(f"The result of multiplying {a} and {b} is {result}")
            # Record the operation in history
            self.history_manager.add_record(a, b, "multiply", result)

        # Create a process for executing the multiplication operation
        process = multiprocessing.Process(target=execute_multiplication, args=(Decimal(a), Decimal(b)))
        process.start()
        process.join()  # Wait for the process to finish
