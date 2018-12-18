# CS152 LBA
Python 2

(These instructions are for a MacOS system)

# Running Django App

## Prerequisites

- Install **SWI-Prolog** if you do not have it: http://www.swi-prolog.org/Download.html

- `git clone` this repository onto your machine

- Create virtual environment in the same directory as the cloned repository and install dependencies:
```
python3 -m venv .venv
source .venv/bin/activate
cd cs152lba
pip install -r requirements.txt
```

- Replace the `pyswip` package in the virtual environment with the folder from the cloned repository

Go back to `.venv/lib/python3.7/site-packages/pyswip` and swap out the pyswip folder with the one in the home directory of the cloned repository

- To make sure `swipl` is executable on the `PATH`, enter the following in terminal:

```
export PATH=$PATH:/Applications/SWI-Prolog.app/Contents/swipl/bin/x86_64-darwin15.6.0
export DYLD_FALLBACK_LIBRARY_PATH=/Applications/SWI-Prolog.app/Contents/swipl/lib/x86_64-darwin15.6.0
```
## Run app

- Navigate to the `cs152lba` and enter the following into terminal:

`python manage.py runserver`

# Running Python program
