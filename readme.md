# Welcome to SpotyQL

Welcome! This is our ultimate SQL project.

## Insights

We've decided to add a frontend interface, trying to merge all teachings we've gotten so far.

This project assembles together teachings from:
- introduction to CS (shoutout Alessio Martino)
- digital skills lab
- Databases & Big Data

## How to execute

There is no need to install dependencies or initialize virtual environments.

To execute the project, just load the 'startup.py' script as follows:

<code>python startup.py .env</code>

This command will
1. Initialize the venv inside folder '.env' (you can also specify any other name)
2. Install dependencies from application/requirements.txt
3. Load application

## Additional commentaries

Inside the root of this project, we've set up a configuration file.

This file presents a set of parameters that can be altered, in order to change the program's behaviour.

For performance purposes, the project has been initally created with sqlite3.
There is, in any case, an option to change such behaviour.

Inside configuration.json, look for "database". Inside such object, you'll find a parameter called "type".
Simply change this option to "mysql" and add the relative parameters (i.e. username, password and connection url) and run the application. This should alter the execution and load the database inside the given MySQL server.

## Navigating the frontend

