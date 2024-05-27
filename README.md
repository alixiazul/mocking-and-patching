# Mocking and patching

Mocks are essential in testing because they allow you to simulate the behaviour of real objects or dependencies. 
They help isolate the component under test, ensuring that its behavior isn't affected by external factors. 
Mocks provide controlled behavior, speed up testing, and make tests more consistent and reproducible.

## Installation and Set Up

- At least Python 3.10.6.
- Create a virtual environment.
- Activate the environment and run pip install -r requirements.txt.
- Ensure that you can access the cruncher classes in the REPL.

## Troubleshooting Pytest

- Deactivate your virtual environment, delete your venv folder and follow the setup steps again to recreate it and install the requirements.
- Close you terminal session and reopen it. Set the PYTHONPATH environment variable and try running pytest again.
- When you're inside the virtual environment, check where the pytest command is located. You can do this by running the command which pytest. It should give you the path to your local Venv directory.
- If the pytest command is not located in your local venv, then you may have installed Python globally on your machine. If that is the case, then deactivate your venv and uninstall the global pytest by running pip uninstall pytest. Reactivate your virtual environment and re-run the pytest command.

## Skills

- Understand what a mock is
- Understand how mocks can be used for testing purposes
- Test code with dependency injection
- Test code with patching