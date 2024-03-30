import logging
from app.command import Command
from history.history_manager import HistoryManager

# Configure logging for this module
logger = logging.getLogger(__name__)

class HistoryCommand(Command):
    def __init__(self, history_manager):
        self.history_manager = history_manager

    def execute(self):
        user_input = input("Choose history action (load, save, clear, delete, print): ").lower()
        parts = user_input.split()
        action = parts[0]

        try:
            if action == 'load':
                # Optionally, prompt the user for a file name, or set a specific file name
                file_name = input("Enter the file name to load from the 'data' folder: ")
                file_path = os.path.join('data', file_name)  # Construct the full path

                self.history_manager.load_history(file_path=file_path)  # Pass the path to load_history
                logger.info("History loaded successfully from " + file_path)
            elif action == 'save':
                self.history_manager.save_history()
                self.history_manager.load_history()  # Reload history DataFrame
                logger.info("History saved successfully.")
            elif action == 'clear':
                self.history_manager.clear_history()
                logger.info("History cleared successfully.")
            elif action == 'delete':
                record_id = self._get_validated_record_id()
                if record_id is not None:  # Ensure record_id is valid before attempting deletion
                    self.history_manager.delete_record(record_id)
                    logger.info(f"Record {record_id} deleted successfully.")
            elif action == 'print':
                history_df = self.history_manager.get_history()
                if not history_df.empty:
                    print("Current History DataFrame:")
                    print(history_df.to_string(index=False))  # Print DataFrame without index
                    logger.info("History printed successfully.")
                else:
                    logger.info("History is empty.")
            else:
                self._handle_invalid_action()
        except Exception as e:
            logger.error(f"An error occurred during '{action}' action: {e}")

    def print_history(self):  # Define the print_history method
        try:
            history_df = self.history_manager.get_history()
            if not history_df.empty:
                # Printing DataFrame with index
                print("Current History DataFrame:")
                print(history_df.to_string(index=True))
                logger.info("History printed successfully.")
            else:
                logger.info("History is empty.")
        except Exception as e:
            logger.error(f"Error printing history: {e}")

    def _get_validated_record_id(self):
        try:
            record_id = int(input("Enter Index Num to delete: "))
            return record_id
        except ValueError:
            logger.error("Invalid input for Index Num. Please enter a numeric value.")
            return None

    def _handle_invalid_action(self):
        valid_actions = ['load', 'save', 'clear', 'delete', 'print']
        logger.error(f"Invalid history action attempted. Valid actions are: {', '.join(valid_actions)}")
