# Twiva

## Prerequisites

[Python](https://www.python.org/) >=3.6  
[PIP](https://pypi.org/project/pip/) >=20  
[Virtualenv](https://virtualenv.pypa.io/en/latest/)

This project depends uses an SQLite database. You might need to check if you have the neccessary drivers [here](https://www.sqlite.org/index.html).

## Installation

Clone this repository to your computer.

```bash
    git clone https://github.com/cephaske254/twiva-moringa.git
```

Enter the project root

```bash
    cd twiva-moringa
```

Create a and activate virtual environment

```bash
    python3 -m virtualenv env

    source env/bin/activate #on Unix/Linux
    ./env/Scripts/activate #on Windows
```

Install the requirements via [pip](https://pypi.org/project/pip/).

```bash
    pip install -r requirements.txt
```

Apply database migrations.

```bash
    python manage.py migrate
```

Start the WSGI server. The server will start on `port 8000` by default.

```bash
    python manage.py runserver
```

## Directory Structure

```
twiva-moringa/
        ├── accounts
        │   ├── migrations
        │   └── templates
        │   └── accounts
        ├── main
        │   ├── migrations
        │   ├── static
        │   │   ├── css
        │   │   ├── images
        │   │   ├── js
        │   │   ├── scss
        │   │   │   └── bootstrap
        │   │   └── svg
        │   └── templates
        │   └── main
        │   └── sections
        ├── migrations
        ├── movies
        │   └── templates
        │   └── movies
        ├── Movies
        ├── staticfiles
        │   ├── admin
        │   ├── css
        │   ├── images
        │   ├── js
        │   ├── scss
        │   │   └── bootstrap
        │   └── svg
        └── utils
        └── requests
        ├── models
```
