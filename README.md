# AirBnB_clone
![banner](img/alx-airbnb-clone-banner.png)
![GitHub repo size](https://img.shields.io/github/repo-size/MelakuDemeke/AirBnB_clone)
![GitHub issues](https://img.shields.io/github/issues/MelakuDemeke/AirBnB_clone)
![GitHub Repo stars](https://img.shields.io/github/stars/MelakuDemeke/AirBnB_clone?logo=github&style=flat)
![GitHub forks](https://img.shields.io/github/forks/MelakuDemeke/AirBnB_clone?logo=github&style=falt)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/MelakuDemeke/AirBnB_clone?logo=github)

## Description
This is the console part of the Airbnb clone project for ALX Africa. It allows us to manage objects through the command line, retrieve objects from a file, and store objects in that file. This is a project to learn and understand how a command interpreter works and how to use it to build a functional Airbnb clone.

## The Command Interpreter
The command interpreter provides a way for the user to interact with the objects. The console provides the following functionalities:

### Commands
- `create` - Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.
- `show` - Prints the string representation of an instance based on the class name and id.
- `destroy` - Deletes an instance based on the class name and id (save the change into the JSON file).
- `all` - Prints all string representation of all instances based or not on the class name.
- `update` - Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file).


## Getting Started
### Prerequisites
To run this program, you need to have the following:

- Python 3 installed on your machine
- A code editor or IDE (Integrated Development Environment) such as PyCharm, Visual Studio Code, Sublime Text, or any other text editor
- The following modules installed: `cmd`, `json`, `os`, `datetime`
- You can install the `cmd` module using `pip`, which is the package installer for Python. The `json`, `os`, and `datetime` modules are built-in and come pre-installed with Python 3.

### Installing
You can download the source code of this project by running the following command:
```
git clone https://github.com/MelakuDemeke/AirBnB_clone.git
```
## Usage

To start the console, run the following command:
```
./console.py
```
Once the console has started, you can run any of the above commands followed by the necessary arguments.

Examples:

- Creating an instance of the BaseModel class:
```
(hbnb) create BaseModel
```

- Showing an instance of the BaseModel class with the given id:
```
(hbnb) show BaseModel 1234-1234-1234
```

- Destroying an instance of the BaseModel class with the given id:
```
(hbnb) destroy BaseModel 1234-1234-1234
```

- Showing all instances of the BaseModel class:
```
(hbnb) all BaseModel
```



## contributors
<a href="https://github.com/MelakuDemeke/AirBnB_clone/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=MelakuDemeke/AirBnB_clone" />
</a>
