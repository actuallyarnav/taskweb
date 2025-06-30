## Introduction
This is a basic tasks/to-do list manager app, made in Flask. It uses SQLite as its database.

## Functionality
1. Create tasks
2. Update the contents of the task
3. Delete a task

## How to install
### Using Python

Prerequisites: python3, pip

`git clone https://github.com/actuallyarnav/taskweb.git`

`cd taskweb`

`python3 app.py`

Then, open `localhost:5050` on a web browser.

### Using Docker

Prerequisites: Docker set up on your machine

`git clone https://github.com/actuallyarnav/taskweb.git`

`cd taskweb`

`docker build -t flask-tasks .`

`docker run -p 5000:5000 flask-tasks`

Then, open `localhost:5050` on a web browser.

Warning: The SQLite database file that you create will be deleted when the container is stopped. Consider using a Docker volume if you wish to prevent that.
