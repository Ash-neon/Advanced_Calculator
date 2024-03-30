import os
import pkgutil
import importlib
from app.command import CommandHandler, Command  # Make sure this import matches your project structure
from history.history_manager import HistoryManager
from app.Plugin.add import AddCommand
from app.Plugin.subtract import SubtractCommand
from app.Plugin.multiply import MultiplyCommand
from app.Plugin.divide import DivideCommand
from app.Plugin.menu import MenuCommand
from app.Plugin.history import HistoryCommand
from dotenv import load_dotenv
import logging
import logging.config

class App:
    def __init__(self):
        # Ensure the logs directory exists relative to the current file, not the current working directory
        self.base_dir = os.path.dirname(__file__)
        logs_dir = os.path.join(self.base_dir, 'logs')
        os.makedirs(logs_dir, exist_ok=True)
        
        self.configure_logging()
        load_dotenv()  # Load environment variables from .env file
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')  # Default to 'PRODUCTION' if not set
        self.command_handler = CommandHandler()

    def configure_logging(self):
        logging_conf_path = os.path.join(self.base_dir, 'logging.conf')
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            # Fallback logging configuration if logging.conf is not found
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded.")
        return settings

    def load_plugins(self):
        plugins_package = 'app.Plugin'
        plugins_path = os.path.join(self.base_dir, '..', plugins_package.replace('.', os.sep))
        if not os.path.exists(plugins_path):
            logging.warning(f"Plugins directory '{plugins_path}' not found.")
            return
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                continue  # This example assumes plugins are not in sub-packages
            try:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                self.register_plugin_commands(plugin_module, plugin_name)
            except ImportError as e:
                logging.error(f"Error importing plugin {plugin_name}: {e}")

    def register_plugin_commands(self, plugin_module, plugin_name):
        for item_name in dir(plugin_module):
            item = getattr(plugin_module, item_name)
            if isinstance(item, type) and issubclass(item, Command) and item is not Command:
                self.command_handler.register_command(plugin_name, item())
                logging.info(f"Command '{plugin_name}' from plugin '{plugin_name}' registered.")

    
    def start(self):
        self.load_plugins()
        logging.info("Application started. Type 'exit' to exit.")
        logging.info("Type 'menu' for MENU.")
        
        history_manager = HistoryManager()

        # Instantiate HistoryCommand with the history_manager argument
        history_command = HistoryCommand(history_manager)

        # Register the HistoryCommand
        self.command_handler.register_command("history", history_command)
         
        # Pass HistoryManager instance to commands that require it
        self.command_handler.register_command("add", AddCommand(history_manager))
        self.command_handler.register_command("subtract", SubtractCommand(history_manager))
        self.command_handler.register_command("multiply", MultiplyCommand(history_manager))
        self.command_handler.register_command("divide", DivideCommand(history_manager))
        self.command_handler.register_command("history", HistoryCommand(history_manager))

        menu_command = MenuCommand(self.command_handler.get_command_names())
        self.command_handler.register_command("menu", menu_command)
        
        while True:
            user_input = input(">>> ").strip()
            if user_input == 'exit':
                logging.info("Exiting the program. Goodbye!")
                return True  # Return True when the 'exit' command is processed
            elif user_input in self.command_handler.get_command_names():
                self.command_handler.execute_command(user_input)
            else:
                logging.error(f"No such command: {user_input}")

if __name__ == "__main__":
    app = App()
    app.start()
