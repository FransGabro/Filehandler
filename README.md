# Filserver

**Version 1.0.0**

Fileserver is a filehandler for your computer that communicates through socketprogramming where multiple clients can connect and handle files in chosen directory.
There are 4 commands you can use for now:

ls = List all files in directory.
size = Print the size of a file.
rm = Remove a file.
quit = To disconnect from server.

---

## Setup

1. Create a virtual environment
2. Install requirements

### Virtual environment (venv)

see <https://docs.python.org/3/library/venv.html>

Linux / OSX

```sh
python -m venv .venv  # could also be python3
source .venv/bin/activate
```

Windows - cmd.exe

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

Windows - PowerShell

```PowerShell
# On Microsoft Windows, it may be required to enable the Activate.ps1 script by setting the execution policy for the user. You can do this by issuing the following PowerShell command:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

py -m venv .venv
.\.venv\Scripts\Activate.ps1

```

### Install requirements.txt

```bat
pip install -r requirements.txt
```
---
###Test
To test the functions through unittest you have to be in the folder "slutuppgift" and write -> python -m unittest test_file_handler.py <- in the terminal.

## Contributors

- Frans Gabro <Frans.Gabro93@gmail.com>

---
