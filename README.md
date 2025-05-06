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

### Activating virtual env
After doing the above two steps, launch the virtual environment shell with
```
pipenv shell
```
in order to do standard Django management. For example, do this before trying to run the dev server with `python3 manage.py runserver`, or trying to create an admin superuser with `python3 manage.py createsuperuser`, and so on.

## Build
All of the files for a static site can be generated using django-distill. Run
```
python3 manage.py distill-local --collectstatic target_directory
```
where `target_directory` is the path to the directory you want the files to go to.
