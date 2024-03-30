import logging
from history.history_manager import HistoryManager

# Configure logging
logging.basicConfig(level=logging.INFO)

# Create a HistoryManager instance
history_manager = HistoryManager()

# Test adding records
history_manager.add_record(4, 5, 'add', 9)
history_manager.add_record(5, 6, 'add', 11)

# Test saving history
history_manager.save_history()

# Test loading history
loaded_history = history_manager.load_history()
print("Loaded History:")
print(loaded_history)