import pandas as pd
import logging
import os
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', stream=sys.stdout)

class HistoryManager:
    def __init__(self, file_name='history.csv'):
        # Ensure the 'data' folder exists; if not, create it
        data_folder = os.path.join(os.getcwd(), 'data')
        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

        self.file_path = os.path.join(data_folder, file_name)
        self.history_df = self.load_history()  # Load history when instantiated

    def load_history(self, file_path=None):
        import os  # Import os module here

        if file_path is None:
            file_path = self.file_path  # Use default if no path is provided

        if not os.path.exists(file_path):
            logging.info(f"CSV file '{file_path}' not found or is empty.")
            return pd.DataFrame(columns=['Operand1', 'Operand2', 'Operation', 'Result'])

        try:
            history_df = pd.read_csv(file_path)
            if history_df.empty:
                logging.info(f"CSV file '{file_path}' is empty.")
            return history_df
        except pd.errors.EmptyDataError:
            logging.info(f"CSV file '{file_path}' is empty.")
            return pd.DataFrame(columns=['Operand1', 'Operand2', 'Operation', 'Result'])

    def save_history(self):
        try:
            # Save the updated DataFrame back to the CSV, ensuring persistence of the new record
            self.history_df.to_csv(self.file_path, index=False)
            logging.info(f"History saved to '{self.file_path}'.")
        except Exception as e:
            logging.error(f"Error saving history: {e}")

    def clear_history(self):
        try:
            # Reset the history DataFrame to an empty state
            self.history_df = pd.DataFrame(columns=['Operand1', 'Operand2', 'Operation', 'Result'])

            # Save the updated empty DataFrame back to the CSV, ensuring that the history is cleared
            self.save_history()

            logging.info("History cleared.")

        except Exception as e:
            # Log any exceptions that occur during the process
            logging.error(f"Error clearing history: {e}")

    def delete_record(self, record_id):
        if record_id in self.history_df.index:
            self.history_df = self.history_df.drop(index=record_id)
            self.save_history()
            logging.info(f"Record ID {record_id} deleted from history.")
        else:
            logging.info("Record ID not found in history.")

    def add_record(self, operand1, operand2, operation, result):
        try:
            # Load the existing history DataFrame
            self.history_df = self.load_history()

            # Add a new row to the DataFrame using loc
            new_index = len(self.history_df)
            self.history_df.loc[new_index] = [operand1, operand2, operation, result]

            logging.info(f"Record added: Operation - {operation}, Operand1 - {operand1}, Operand2 - {operand2}, Result - {result}")
            # Save DataFrame to CSV
            self.save_history()  # Just call save_history without any arguments
        except Exception as e:
            logging.error(f"Error adding record: {e}")

    def get_history(self):
        try:
            # Reload the history DataFrame to ensure it contains the latest data
            self.history_df = self.load_history()
            logging.info("Current History DataFrame:")
            print(self.history_df)
        except Exception as e:
            logging.error(f"Error printing history: {e}")