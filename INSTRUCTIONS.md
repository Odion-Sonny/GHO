## Set up a development environment

### Open Terminal
Open the terminal on your local machine. On a Mac, you can find the Terminal application in the Utilities folder in your Applications folder. On a Windows machine, you can use Command Prompt or PowerShell.

### Navigate to the Directory Where You Want to Clone the Repository
Navigate to the directory where you want to clone the repository. You can do this by using the `cd` command followed by the directory path. For example, if you want to clone the repository to your Desktop, you would use the following command:


```sh
cd Desktop
```
### Clone the Repository
Use the git clone command followed by the repository URL to clone the repository. You would use the following command:

```sh
git clone https://github.com/HousewareHQ/houseware---data-engineering-octernship-Odion-Sonny.git

```

### Install Python (if not already installed)

To complete this unit, you must have Python 3.6 or later installed on your computer. There's a chance you might already have Python installed, especially if you've already used it. You can confirm whether it's installed by executing one of the following commands:

```sh
python --version
```


### Create a virtual environment

A Python virtual environment isn't necessarily as complex as it sounds. Rather than creating a virtual machine or container, a virtual environment is a folder that contains all of the libraries we need to run our application, including the Python runtime itself. By using a virtual environment, we make our applications modular, allowing us to keep them separate from one another and avoid versioning issues. As a best practice you should always use virtual environments when working with Python.

To use a virtual environment, we'll create and activate it. We create it by using the venv module, which you installed as part of your Python installation instructions earlier. When we activate it, we tell our system to use the folder we created for all of its Python needs.

```
# Windows
# Create the environment
python -m venv venv
# Activate the environment
.\venv\scripts\activate

# macOS or Linux
# Create the environment
python -m venv venv
# Activate the environment
source ./venv/bin/activate
```

### Install dependencies

With our virtual environment created and activated, we can now install the dependencies we need for our website. We'll install them by following a common convention, which is to create a `requirements.txt` file.

The `requirements.txt` file isn't special in and of itself; it's a text file where we list the libraries required for our application. But it's the convention typically used by developers, and makes it easier to manage applications where numerous libraries are dependencies.

- Return to the command or terminal window and perform the installation by using pip to run the following command:

```
pip install -r requirements.txt
```

The command downloads the necessary libraries and their dependencies.
