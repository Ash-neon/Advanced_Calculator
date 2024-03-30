import pytest
from app import App

def test_app_start_exit_command(monkeypatch, capfd):
    app = App()
    monkeypatch.setattr('builtins.input', lambda _: 'exit')  # Mock input to automatically return 'exit'
    assert app.start() == True  # Assert that start() returns True
    # Additional assertions can be made here based on captured output

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    assert app.start() == True  # Assert that start() returns True when exit command is given
