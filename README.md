# IEEE PEDES 2024
This is the official website for IEEE PEDES 2024.

## Steps for setting up
1. Download the Python version mentioned in `.python-version`.
2. It is recommended to use a virtual environment. If you just have Python, you can use `python -m venv venv`. If you are using some other management tool (like pyenv, conda, etc.), please check the documentation for the same.
3. Once activated, install the requirements using `pip install -r requirements.txt`.
4. Setup the Django project by running the following commands
```shell
python manage.py makemigrations // To make migration files.
python manage.py migrate // To migrate to the database.
python manage.py runserver // To run the server.
```
5. The application should be visible on your browser at `http://localhost:8000`.