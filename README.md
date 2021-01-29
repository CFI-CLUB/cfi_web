# CFI

## Steps to run it locally :

- git clone https://github.com/pydevsg/cfi_website

- cd cfi_website

## We will need to create a virtual environment to run this project 

### For **Windows** follow these commands step by step

    > py -m pip install --user virtualenv
    > py -m venv env
    > .\env\Scripts\activate

### For **Linux** use these commands step by step

    > python3 -m pip install --user virtualenv
    > python3 -m venv env
    > source env/bin/activate

### This will create a virtual environment named **_env_** and activate it

    > pip3 install -r requirements.txt  ( This will install all the dependencies from requirements.txt file )

    > py manage.py runserver ( Command to run the program )

This will start the server in http://127.0.0.1:8000/

Switch to http://127.0.0.1:8000/cfi/ for the main website .
