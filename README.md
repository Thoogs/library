# Library terminal app
## Made by Teemu "Thoogs" Mahlamäki

This application is a simple database handler and terminal UI, that allows the user to add books into the database, as well as print it out in a nice acsii table format.

### Using the app

To run the application, I recommend you setup a virtual environment with
```sh 
python3 -m venv .venv
source .venv/bin/activate
```

After setting up the venv, you can install the app by running
```sh 
pip install .
```

Now we can either run the application with either of these commands:
```sh 
library_app <insert_database_file_here>

# or 

python library/tui.py <insert_database_file_here>
```

### Known issues:

- If the length of the fields is longer than expected, the table might be ill aligned.
-
