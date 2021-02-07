<h1>attendance_organizer</h1>

![GitHub repo size](https://img.shields.io/github/repo-size/JLpython-py/attendance-organizer)
![GitHub last commit](https://img.shields.io/github/last-commit/JLpython-py/attendance-organizer)
![GitHub](https://img.shields.io/github/license/JLpython-py/attendance-organizer)

![attendance-organizer Logo](https://user-images.githubusercontent.com/72679601/104869490-0478e700-58fb-11eb-9c0c-5e9401d5d33e.png)

In Microsoft Teams meetings, hosts can download the attendance as a CSV file. 
However, the layout of the CSV makes the file hard to read. 
The `attendance_organizer` module reads the data in these CSV files and rewrites it into a cleaner CSV file.

<h2>Installation</h2>

[Download the Latest Release](https://github.com/JLpython-py/attendance-organizer/releases)

- From the Command Line: Run `pip install -r requirements.txt`

An executable file for `application.py` is available. 
Currently, only Windows is supported for a standalone application for this script.

<h2>Requirements</h2>

- Python 3.6+
- Running **application.exe** is only supported on Windows.

<h2>Usage</h2>

<h3>Import Module</h3>

```python
from attendance_organizer import Organizer
organizer = Organizer()
organizer.upload("path/to/attendance/file.csv")
organizer.organize()
organizer.download("path/to/download/file.csv")
```

<h3>tkinter Application</h3>

```commandline
python application.py
```

<h3>Application Executable</h3>

Launch **application.exe**

<h2>Application View</h2>

![tkinter Window](https://user-images.githubusercontent.com/72679601/107161150-9a7abd00-694f-11eb-8145-0dc6facc1b94.png)

`application.py` allows the user to interact with a `tkinter` GUI window to execute various functions.

- **Upload File**: Opens a file dialogue, prompting the user to select a file to process
- **Organize Data**: Parses the CSV file and rewrites the data in a cleaner format
- **Download File**: Writes the organized data to a CSV file and prompts the user to select a path to save the file to
- **End Task**: Quits the application
- **Reset**: Resets the window and all its widgets to its original state

An in-depth tutorial for working with this application can be found in the repository's Wiki, [here](https://github.com/JLpython-py/attendance-organizer/wiki/Tutorial).
