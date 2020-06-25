# AirBnB_clone:



<p align="center">
  <img src="https://i.imgur.com/JOhaZ5m.png">
</p>


The AirBnB clone project begin from now until the end of the first year and as an ultime goal of the project is to deploy on our server a simple copy of the AirBnB website.

The project won’t implement all the features, only some of them to cover all fundamental concepts of the higher level programming track.

After 4 months, it will be a complete web application composed by:

- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).
- A website (the front-end) that shows the final product to everybody: static and dynamic.
- A database or files that store data (data = objects).
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them).


## Final product:

<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/8-index.png">
</p>


# 0x00. AirBnB clone - The console:


## Background Context:


### First step: Write a command interpreter to manage your AirBnB objects.


This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances.
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file.
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel.
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine.



### What’s a command interpreter?


Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place).
- Retrieve an object from a file, a database etc… .
- Do operations on objects (count, compute stats, etc…).
- Update attributes of an object.
- Destroy an object.


### Resources

#### Read or watch:

- [cmd module](https://docs.python.org/3.4/library/cmd.html)
- [packages](https://intranet.hbtn.io/concepts/66)
- [uuid module](https://docs.python.org/3.4/library/uuid.html)
- [datetime](https://docs.python.org/3.4/library/datetime.html)
- [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- [args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)
- [Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)


## Learning Objectives

### General


- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function



## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7 or more)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')


### Python Unit Tests

- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case




<p align="center">
  <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/8-index.png">
</p>

