import pandas as pd
import unittest
from unittest.mock import MagicMock, patch
from app.Plugin.history import HistoryCommand
from unittest.mock import call


# This class tests functionalities of the HistoryCommand class
class TestHistoryCommand(unittest.TestCase):
    def setUp(self):
        self.history_manager_mock = MagicMock()
        self.history_command = HistoryCommand(self.history_manager_mock)

    # Test the 'delete' functionality with input patched to simulate user input
    @patch('builtins.input', return_value='delete')
    @patch('app.Plugin.history.HistoryCommand._get_validated_record_id', return_value=1)
    def test_execute_delete(self, input_mock, validated_record_id_mock):
        self.history_command.execute()
        self.history_manager_mock.delete_record.assert_called_once_with(1)

    # Test the 'load' functionality to ensure history data is loaded as expected
    @patch('builtins.input', return_value='load')
    def test_execute_load(self, input_mock):
        self.history_command.execute()
        self.history_manager_mock.load_history.assert_called_once()

    

    @patch('builtins.input', return_value='print')
    @patch('builtins.print')  # Patching print to verify output
    def test_execute_print(self, print_mock, input_mock):
        self.history_manager_mock.get_history.return_value = pd.DataFrame({
            'Operand1': [1, 2],
            'Operand2': [3, 4],
            'Operation': ['add', 'subtract'],
            'Result': [4, -2]
        })
        self.history_command.execute()

        # Verify the initial announcement call was made
        print_mock.assert_any_call("Current History DataFrame:")

        # Verify data content presence in one of the print calls
        content_checks = ["1", "2", "3", "4", "add", "subtract", "4", "-2"]
        actual_calls = " ".join(call.args[0] for call in print_mock.call_args_list)
        for check in content_checks:
            self.assertIn(check, actual_calls, f"Expected content '{check}' not found in print calls.")


if __name__ == "__main__":
    unittest.main()
