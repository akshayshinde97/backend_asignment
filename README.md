# backend_asignment
## Summary:
The REST APIs are built using Python Flask framework. Docker containers are used for development environment.

It contains the below mentioned endpoints:
- a GET '/api/videos'

 I have used app based approach for this task.

## Project Structure (App Based):
```bash
FlaskProject/
├── Dockerfile
├── Makefile
├── README.md
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── resources.py
│   │   ├── routes.py
│   │   └── schemas.py
│   ├── constants.py
│   ├── db.py
│   ├── settings.py
│   └── utils.py
├── config.py
├── docker-compose.yml
├── entrypoint.sh
├── migrate.py
├── migrations/
│   ├── README
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions
├── .gitignore
├── requirements.txt
└── run.py
```

### Python extensions used:
- **flask** - This is a microframework for Python
- **flask_restful** - This is an extension for Flask that adds support for quickly building of REST APIs.
- **flask_script** - This is an extension that provides support for writing external scripts in Flask.
- **flask_migrate** - This is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.
- **flask_sqlalchemy** - This is an extension for Flask that adds support for SQLAlchemy. It allows to write ORM queries to operate against database.
- **flask_marshmallow** - This is an integration layer for Flask and marshmallow (ORM/ODM/framework-agnostic library for converting complex datatypes, such as objects, to and from native Python datatypes. This is used also to Serializing and Deserializing Objects.) that adds additional features to marshmallow.
- **mysqlclient** - MySQL database connector for Python
- **requests** - This is a python library to make calls to external APIs

### How to start application (using Docker)
- Go into the project directory:
    ```
    cd flask-application
    ```
- Run the application by the following command:
    ```
    make up
    ```

### How to ssh into a Docker containers
- ssh into app container
    ```
    make app-shell
    ```
- ssh into database container
    ```
    make db-shell
    root@e27d5a54fbb8:/# mysql -u root -p
    Enter password: root
    mysql> show databases;
    mysql> use testdb;
    mysql> show tables;
    mysql> select * from video_directory;
    ````
