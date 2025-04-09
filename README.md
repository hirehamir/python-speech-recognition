[![Mypy](https://github.com/hamirmahal/python-speech-to-text/actions/workflows/mypy.yml/badge.svg)](https://github.com/hamirmahal/python-speech-to-text/actions/workflows/mypy.yml)
[![Ruff](https://github.com/hamirmahal/python-speech-to-text/actions/workflows/ruff.yml/badge.svg)](https://github.com/hamirmahal/python-speech-to-text/actions/workflows/ruff.yml)
[![Test](https://github.com/hamirmahal/python-speech-to-text/actions/workflows/test.yml/badge.svg)](https://github.com/hamirmahal/python-speech-to-text/actions/workflows/test.yml)

# Setup

Run

```
python3 -m venv venv/
pip list
pip install ruff
pip list
pip install mypy
pip list
pip freeze > requirements.txt # Ensure we have the latest dependency versions.
```

in your terminal.

Then, restart your terminal or run

```
source env/bin/activate
```

# Installation

Run

```
pip list
pip install -r requirements.txt
pip list
```

in your terminal to install any packages in `requirements.txt`.

To install a new package, run

```
pip list
pip install mypy # replace `mypy` with the package name
pip list
pip freeze > requirements.txt
```

in your terminal.

# Running the Program

Run

```
time python src/main.py
```

in your terminal after activating the virtual environment.

# Testing, Type Checking and Linting

Run

```
time ruff format --check && time ruff check . && time mypy . && python -m unittest src.utils.print_with_time
```
