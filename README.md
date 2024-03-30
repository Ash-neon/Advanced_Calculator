Setup:
Python Virtual Environment:
Install virtualenv if you haven't already:
-> pip install virtualenv
-> virtualenv venv
-> source venv/bin/activate

Manage Dependencies:
Install necessary packages using pip:
-> pip install pytest pylint coverage pandas faker
-> pip freeze > requirements.txt

Configure Pytest:
Create a test directory and write test cases using the pytest framework.
Run pytest:
-> pytest

Git Commands
Initialize a Git repository if you haven't already:
-> git init
-> git add .
-> git commit -m "Initial commit"
-> git push origin main
Design Patterns Used: 
Command Pattern: 
The Command pattern is one of the patterns I used, and it is essential for processing user commands in a scalable and adaptable way. This approach can be seen in the development of the application's plugin system, which includes concrete implementations of the Command abstract base class like AddCommand and SubtractCommand.

Used In: This approach is directly implemented by the Command and CommandHandler 
classes found in app/command/__init__.py. The CommandHandler is in charge of carrying out these instructions in response to user input. Each command is an encapsulation of an action and its arguments.

Plugin Pattern:
I used the Plugin pattern technique to increase the functionality of the program without changing its core code. This approach offers a great degree of flexibility and extensibility by enabling the dynamic loading of more commands or features during runtime.

Used In:  The load_plugins function of the App class in app/__init__.py is where this approach is mostly used. Plugins are dynamically found and loaded in this manner, enabling new features to be easily added to the program as independent modules.

Factory Method pattern:
The process by which command objects are created and controlled by the CommandHandler is similar to the Factory Method design, even though it isn't called that officially. As the subclasses will choose which class to instantiate despite an interface being defined for object creation.

Used In: The CommandHandler in app/command/__init__.py acts as a factory-like function, generating instances of command objects according to the command name.

Singleton Pattern:
Though the program does not fully use the Singleton pattern, but it does indicate that the App and CommandHandler classes to only be used once. Having a single instance of these classes fits the Singleton pattern, which limits the number of objects that may be instantiated for a class.

Used In: A Singleton-like use is shown by the App class's instantiation and the creation of a single CommandHandler in app/__init__.py. 

Using Environment Variables:
I used environment variables to control the setups of my applications in real-time. This method is particularly helpful for differentiating between development and production environments since it enables behavior modification of the program without requiring changes to the code. For example, I used the load_dotenv() method in the App class constructor within app/__init__.py to load the environment variables from the a.env file. Afterwards, I put these variables in the self. settings dictionary so that the program could access configuration options from one place.

Logging:
I included logs throughout the program to make debugging easier and to keep an eye on its operating status. I made sure that helpful messages, warnings, and failures are continuously logged at the application's beginning, which helps with debugging. I specifically set logging to collect and record multiple events at different severity levels (info, warning, error) in both the App class in app/__init__.py and the command processing logic in app/command/__init__.py. This is helpful not just in finding problems in the development process but also in tracking the behavior of the application in production so that errors can be quickly fixed.

Exception Handling: LBYL and EAFP:
I have used both LBYL and EAFP methods of exception handling, depending on the situation.
LBYL: This method involves checking conditions before to carrying out a potential error. The CommandHandler.execute_command function in app/command/__init__.py is where I have used this function. As it verifies that a command name is in the commands dictionary before attempting to execute it. 
EAFP: This method attempts to carry out a task directly while managing any exceptions that may occur. It is used in the execute_command method of the CommandHandler where it handles the conversion of user input to decimal. In this case, I try the conversion and raise the InvalidOperation exception if the input is invalid rather than immediately verifying if the user input is a valid integer. When there is a high probability of success and a low probability of exceptions, this function is helpful.
