#! python3
# widget.py

"""
MIT License

Copyright (c) 2021 Jacob Lee

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import tkinter

from attendance_organizer import Organizer


class Widget(Organizer):

    def __init__(self):
        super().__init__()

        self.root = tkinter.Tk()
        self.root.attributes("-topmost", True)
        self.root.title("Attendance Organizer")

        self.status_var = tkinter.StringVar(self.root)
        self.status_label = tkinter.Label(
            self.root, textvariable=self.status_var
        )

        self.details_var = tkinter.StringVar(self.root)
        self.details_entry = tkinter.Entry(
            self.root, textvariable=self.details_var,
            state="readonly", width=100
        )

        self.upload_button = tkinter.Button(
            self.root, text="Upload File", command=self.upload_file
        )
        self.upload_var = tkinter.StringVar(self.root)
        self.upload_entry = tkinter.Entry(
            self.root, textvariable=self.upload_var,
            state="readonly", width=100
        )

        self.organize_button = tkinter.Button(
            self.root, text="Organize Data",
            state="disabled", command=self.organize
        )

        self.end_task_button = tkinter.Button(
            self.root, text="End Task", command=self.root.destroy
        )

        self.download_button = tkinter.Button(
            self.root, text="Download File",
            state="disabled", command=self.download_file
        )
        self.download_var = tkinter.StringVar(self.root)
        self.download_entry = tkinter.Entry(
            self.root, textvariable=self.download_var,
            state="readonly", width=100
        )

        self.reset_button = tkinter.Button(
            self.root, text="Reset", command=self.reset_widget
        )

    def display(self):
        self.upload_button.grid(row=0, column=0, sticky="w")
        self.upload_entry.grid(row=0, column=1, sticky="w")
        self.end_task_button.grid(row=0, column=2, sticky="e")

        self.organize_button.grid(row=1, column=0, sticky="w")
        self.details_entry.grid(row=1, column=1, sticky="w")
        self.reset_button.grid(row=1, column=2, sticky="e")

        self.download_button.grid(row=2, column=0, sticky="w")
        self.download_entry.grid(row=2, column=1, sticky="w")

        self.root.mainloop()

    def upload_file(self):
        pass

    def download_file(self):
        pass

    def reset_widget(self):
        pass


if __name__ == '__main__':
    widget = Widget()
    widget.display()
