Example of a Flask project using SQLAlchemy and Flask-SQLAlchemy as ORM

Docker-compose is used to deploy a PostgreSQL database and pgadmin.

# Requisites:

- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker-Compose](https://docs.docker.com/compose/install/)

# Optionals:

- [Postman](https://www.postman.com/downloads/)


# How to run the project:

1. Clone the repository:
```bash
git clone https://github.com/pythonglobal/flask-sqlalchemy-example.git
```

2. Access the project folder

3. Deploy docker compose
```bash
docker-compose up
```

4. Create pipenv
```bash
pipenv install
```

5. Activate pipenv
```bash
pipenv shell
```

6. Run the project

Before running the webserver, you need to create the database and tables and example data. To do this, run the following script:

```bash
python create_tables.py
python create_example_data.py
```

Then you can run the webserver with the following command:

```bash
python main.py
```
