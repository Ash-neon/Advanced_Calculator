from app.Plugin.subtract import SubtractCommand
from app.Plugin.multiply import MultiplyCommand
from app.Plugin.divide import DivideCommand
from history.history_manager import HistoryManager

def test_add_command(capfd):
    history_manager = HistoryManager()
    command = AddCommand(history_manager)
    command.execute(Decimal('5'), Decimal('3'))
    out, err = capfd.readouterr()
    
    expected_result = 8
    assert Decimal(out.strip().split()[-1]) == expected_result, "The AddCommand should calculate the correct result"


def test_subtract_command(capfd):
    history_manager = HistoryManager()
    command = SubtractCommand(history_manager)  # Pass the history_manager instance
    # Assuming execute now takes two parameters, and prints the result
    command.execute(Decimal('5'), Decimal('3'))
    out, err = capfd.readouterr()
    assert out.strip() == "The result of subtracting 3 from 5 is 2", "The SubtractCommand should print the correct result"

def test_multiply_command(capfd):
    history_manager = HistoryManager()
    command = MultiplyCommand(history_manager)  # Pass the history_manager instance
    # Assuming execute now takes two parameters, and prints the result
    command.execute(Decimal('5'), Decimal('3'))
    out, err = capfd.readouterr()
    assert out.strip() == "The result of multiplying 5 and 3 is 15", "The MultiplyCommand should print the correct result"

def test_divide_command(capfd):
    history_manager = HistoryManager()
    command = DivideCommand(history_manager)  # Pass the history_manager instance
    # Assuming execute now takes two parameters, and prints the result
    command.execute(Decimal('6'), Decimal('2'))
    out, err = capfd.readouterr()
    assert out.strip() == "The result of dividing 6 by 2 is 3", "The DivideCommand should print the correct result"

def test_menu_command(capfd, monkeypatch):
    # Set up the application with a mocked input to trigger the 'menu' command, then 'exit'
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    # Register the MenuCommand explicitly for this test
    app.command_handler.register_command("menu", MenuCommand(app.command_handler.get_command_names()))

    app.start()

    out, err = capfd.readouterr()
    # Assert that the menu lists commands; adjust expected output as necessary
    assert "add" in out, "The menu should list the 'add' command"
    assert "subtract" in out, "The menu should list the 'subtract' command"
    assert "multiply" in out, "The menu should list the 'multiply' command"
    assert "divide" in out, "The menu should list the 'divide' command"
    assert "menu" in out, "The menu should list itself"