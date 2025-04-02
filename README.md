# Website

Source for my personal website [I haven't hosted this anywhere yet. Pretend there is a link please.].

## Setup

### Install Dependencies
Assuming one has Python installed already:

Install pipenv via pip (`pip install pipenv`) and then run
```
pipenv install
```
in the project directory.

### Environment
Create a `.env` file in the project directory with the following vars:

- `SECRET_KEY`: Django secret key. Generate your own.
- `DEBUG_STATUS`: One of "True" or "False". Defaults to "True" if not set.

### Activating virtual env and beyond
After doing the above two steps, launch the virtual environment shell with
```
pipenv shell
```
in order to do standard Django management e.g. running the dev server with `python3 manage.py runserver`, creating admin superuser with `python3 manage.py createsuperuser`, etc.
