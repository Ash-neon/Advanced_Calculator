import sys
from io import StringIO
from contextlib import redirect_stdout
from calculator import Calculator
from decimal import Decimal, InvalidOperation
from main import calculate_and_print, HistoryManager

def test_calculate_and_print_add(capfd):
    history_manager = HistoryManager()
    calculate_and_print('5', '3', 'add', history_manager)
    out, _ = capfd.readouterr()
    assert "The result of 5 add 3 is equal to 8" in out

def test_calculate_and_print_subtract(capfd):
    history_manager = HistoryManager()
    calculate_and_print('10', '2', 'subtract', history_manager)
    out, _ = capfd.readouterr()
    assert "The result of 10 subtract 2 is equal to 8" in out

def test_calculate_and_print_multiply(capfd):
    history_manager = HistoryManager()
    calculate_and_print('4', '5', 'multiply', history_manager)
    out, _ = capfd.readouterr()
    assert "The result of 4 multiply 5 is equal to 20" in out

def test_calculate_and_print_divide(capfd):
    history_manager = HistoryManager()
    calculate_and_print('20', '4', 'divide', history_manager)
    out, _ = capfd.readouterr()
    assert "The result of 20 divide 4 is equal to 5" in out

def test_calculate_and_print_divide_by_zero(capfd):
    history_manager = HistoryManager()
    calculate_and_print('1', '0', 'divide', history_manager)
    out, _ = capfd.readouterr()
    assert "Cannot divide by zero" in out

def test_calculate_and_print_unknown_operation(capfd):
    history_manager = HistoryManager()
    calculate_and_print('9', '3', 'unknown', history_manager)
    out, _ = capfd.readouterr()
    assert "Unknown operation: unknown" in out

def test_calculate_and_print_invalid_input(capfd):
    history_manager = HistoryManager()
    calculate_and_print('5', 'b', 'add', history_manager)
    out, _ = capfd.readouterr()
    assert "Invalid number input: 5 or b is not a valid number." in out
