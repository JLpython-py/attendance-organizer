#! python3
# attendance_organizer.py

import csv
import datetime
import logging
import os
import re
import tkinter
import tkinter.filedialog

logging.basicConfig(
    level=logging.DEBUG,
    format=' %(asctime)s - %(levelname)s - %(message)s')
class AttendanceOrganizer:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.attributes("-topmost", True)
        self.root.title("Attendance Organizer")
        self.upload_file_button = tkinter.Button(
            self.root, text="Upload File", command=self.upload_file)
        self.organize_data_button = tkinter.Button(
            self.root, text="Organize Data", command=self.organize_data)
        self.end_task_button = tkinter.Button(
            self.root, text="End Task", command=self.end_task)

    def display(self):
        self.upload_file_button.grid(row=1, column=0)
        self.organize_data_button.grid(row=1, column=2)
        self.end_task_button.grid(row=1, column=3)
        self.root.mainloop()

    def upload_file(self):
        filepath = tkinter.filedialog.askopenfilename(
            parent=self.root, title="Select a file to open")
        if not (filepath and os.path.splitext(filepath)[-1] == '.csv'):
            return
        with open(filepath, encoding='utf-16') as file:
            self.values = list(csv.reader(file, delimiter='\t'))
            del self.values[0]

    def organize_data(self):
        name_regex = re.compile(r'([A-Z][A-Za-z]+) ([A-Z][A-Za-z]+)')
        action_regex = re.compile(r'(Joined|Left)')
        self.data = {}
        for row in self.values:
            full_name = name_regex.search(row[0])
            action_name = action_regex.search(row[1])
            try:
                first, last = full_name.group(1), full_name.group(2)
                action = action_name.group(1).title()
            except AttributeError:
                self.data = {}
                return
            try:
                dt_obj = datetime.datetime.strptime(
                    row[2], '%m/%d/%Y, %I:%M:%S %p')
            except ValueError:
                self.data = {}
                return
            time = dt_obj.strftime('%m.%d.%Y %H:%M:%S')
            key = f"{last}, {first}"
            self.data.setdefault(key, {"Last": last, "First": first})
            self.data[key].setdefault(action, time)

    def convert_data(self):
        pass

    def end_task(self):
        self.root.destroy()

def main():
    organizer = AttendanceOrganizer()
    organizer.display()

if __name__ == '__main__':
    main()
