# attendance-organizer

![attendance-organizer Logo](https://user-images.githubusercontent.com/72679601/104869490-0478e700-58fb-11eb-9c0c-5e9401d5d33e.png)

In Microsoft Teams meetings, hosts can download the attendance as a CSV. However, the CSV layout is somewhat messy and is in order of attendee first name, as opposed to the commonly used last name. The script, `attendance_organizer.py`, rewrites the data into a cleaner CSV file.

<h1>Installation</h1>

[Download the Latest Release](https://github.com/JLpython-py/attendance-organizer/releases)

An executable file for `attendance_organizer.py` is available in the _dist/_ directory of the repository. Currently, only Windows is supported for a standalone application for this script.

![Script Executable](https://user-images.githubusercontent.com/72679601/104860422-56604380-58e0-11eb-9776-86a051c65fa5.png)

<h1>Requirements</h1>

- Python 3.2+

<h1>Usage</h1>

![tkinter Window](https://user-images.githubusercontent.com/72679601/104860197-1351a080-58df-11eb-8bc8-5c3b71bf90d3.png)

`attendance_organizer.py` allows the user to interact with a `tkinter` GUI window to execute various functions.

- **Upload File**: Opens a file dialogue, prompting the user to select a file to process
- **Organize Data**: Parses the CSV file and rewrites the data in a cleaner format
- **Download File**: Writes the organized data to a CSV file and prompts the user to select a path to save the file to
- **End Task**: Quits the application
- **Reset**: Resets the window and all its widgets to its original state

And in-depth tutorial for working with this application can be found in the repository's Wiki
