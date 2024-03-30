import sys
from calculator import Calculator
from decimal import Decimal, InvalidOperation
from app import App
from history.history_manager import HistoryManager
import os

def calculate_and_print(a, b, operation_name, history_manager):
    operation_mappings = {
        'add': Calculator.add,
        'subtract': Calculator.subtract,
        'multiply': Calculator.multiply,
        'divide': Calculator.divide
    }

    try:
        a_decimal, b_decimal = map(Decimal, [a, b])
        result = operation_mappings.get(operation_name)
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_decimal, b_decimal)}")
            history_manager.add_record(a, b, operation_name, result(a_decimal, b_decimal))  # Save to history
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except ZeroDivisionError:
        print("Error: Division by zero.")
    except Exception as e:  # Catch-all for unexpected errors
        print(f"An error occurred: {e}")

def main():
    # Calculate absolute and relative file paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(current_dir, 'data')

    # Create 'data' directory if it doesn't exist
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)
        print(f"The directory '{data_dir}' is created")

    # Join the data directory path with the name of the history file to get the absolute file path for the history file
    history_file = os.path.join(data_dir, 'history.csv')
    
    # Instantiate history manager with the absolute file path
    history_manager = HistoryManager(history_file)

    # Check if correct number of arguments provided
    if len(sys.argv) != 4:
        print("Usage: python calculator_main.py <number1> <number2> <operation>")
        sys.exit(1)

    _, a, b, operation = sys.argv
    calculate_and_print(a, b, operation, history_manager)

    # Save history when the program ends
    history_manager.save_history()

if __name__ == '__main__':
    App().start()
    # main()
