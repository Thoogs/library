# Library terminal app
## Made by Teemu "Thoogs" Mahlamäki

This application is a simple database handler and terminal UI, that allows the user to add books into the database, as well as print it out in a nice acsii table format.

### Using the app

#### Disclaimer for windows

The app has been developed on Linux, and no windows testing has been done, but it should technically work on any OS.

#### How to run

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

### Design choices

As the app is part of a code exam, I explicitly decided to not use libraries such as pandas or csv for the data handling and printing, as the assumption is that most of the code should be self written.

Technically the book.py and db_handler.py should be light enough to use that they can be used as libraries on other applications and the UI could be written in some kind of framework. I pondered using Textual or curses libraries for the UI, but as I am not familiar with Textual I deemed it too risky to go for it.

### Known issues:

- If the length of the fields is longer than expected, the table might be ill aligned.
- User can put invalid ISBN or year into the app, which will result in int casting failing when we create book objects.
- db_handler has no unittests so there could be some bugs there.
