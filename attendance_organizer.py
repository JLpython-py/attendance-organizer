#! python3
# attendance_organizer.py

import csv
import datetime
import os
import re
import tkinter
import tkinter.filedialog

class AttendanceOrganizer:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.attributes("-topmost", True)
        self.root.title("Attendance Organizer")

        self.status_var = tkinter.StringVar(self.root)
        self.status_label = tkinter.Label(
            self.root, textvariable=self.status_var)

        self.details_var = tkinter.StringVar(self.root)
        self.details_entry = tkinter.Entry(
            self.root, textvariable=self.details_var, state='readonly',
            width=100)

        self.upload_file_button = tkinter.Button(
            self.root, text="Upload File", command=self.upload_file)
        self.upload_var = tkinter.StringVar(self.root)
        self.upload_path = tkinter.Entry(
            self.root, textvariable=self.upload_var, state='readonly',
            width=100)

        self.organize_data_button = tkinter.Button(
            self.root, text="Organize Data", state='disabled',
            command=self.organize_data)

        self.end_task_button = tkinter.Button(
            self.root, text="End Task", command=self.end_task)

        self.download_file_button = tkinter.Button(
            self.root, text="Download File", state='disabled',
            command=self.download_file)
        self.download_var = tkinter.StringVar(self.root)
        self.download_path = tkinter.Entry(
            self.root, textvariable=self.download_var, state='readonly',
            width=100)

        self.reset_button = tkinter.Button(
            self.root, text="Reset", command=self.reset)

    def display(self):
        self.upload_file_button.grid(row=0, column=0)
        self.upload_path.grid(row=0, column=1, sticky='w')

        self.end_task_button.grid(row=0, column=2)

        self.organize_data_button.grid(row=1, column=0)

        self.details_entry.grid(row=1, column=1, sticky='w')

        self.download_file_button.grid(row=2, column=0)
        self.download_path.grid(row=2, column=1, sticky='w')

        self.reset_button.grid(row=1, column=2)

        self.root.mainloop()

    def upload_file(self):
        self.details_var.set(
            value="Select a file to upload")
        filetypes = [('Comma Separated Values', '.csv')]
        filepath = tkinter.filedialog.askopenfilename(
            parent=self.root, filetypes=filetypes, initialdir=os.getcwd())
        if not (filepath and os.path.splitext(filepath)[-1] == '.csv'):
            return
        self.upload_var.set(value=filepath)
        self.details_var.set(
            value="File Uploaded {}".format(
                self.details_var.get()))
        with open(filepath, encoding='utf-16') as file:
            self.values = list(csv.reader(file, delimiter='\t'))
            del self.values[0]
        self.organize_data_button.config(state='normal')

    def organize_data(self):
        self.organize_data_button.config(state='disabled')
        name_regex = re.compile(r'([A-Z][A-Za-z]+) ([A-Z][A-Za-z]+)')
        action_regex = re.compile(r'(Joined|Left)')
        datetime_format = '%m/%d/%Y, %I:%M:%S %p'
        data = {}
        for row in self.values:
            full_name = name_regex.search(row[0])
            action_name = action_regex.search(row[1])
            try:
                first, last = full_name.group(1), full_name.group(2)
                action = action_name.group(1).title()
                time = datetime.datetime.strptime(
                    row[2], datetime_format).strftime('%m.%d%Y %H:%M:%S')
            except (AttributeError, ValueError):
                self.data = {}
                self.details_var.set(
                    value="An error occurred while processing the data. "
                    "Please make sure the correct file was uploaded.")
            try:
                first, last = full_name.group(1), full_name.group(2)
                action = action_name.group(1).title()
            except AttributeError:
                self.data = {}
                return
            try:
                dt_obj = datetime.datetime.strptime(row[2], datetime_format)
                time = dt_obj.strftime('%m.%d.%Y %H:%M:%S')
            except ValueError:
                self.data = {}
                return
            key = ', '.join([first, last])
            data.setdefault(key, {"Last": last, "First": first})
            data[key].setdefault(action, time)
        self.data = {k: data[k] for k in sorted(data)}
        self.details_var.set(
            value="Data Organized\t{}".format(
                self.details_var.get()))
        self.download_file_button.config(state='normal')

    def download_file(self):
        self.details_var.set(
            value="Select a location to save file\t{}".format(
                self.details_var.get()))
        filetypes = [('Comma Separated Values', '.csv')]
        filepath = tkinter.filedialog.asksaveasfilename(
            parent=self.root, filetypes=filetypes, initialdir=os.getcwd())
        self.download_var.set(value=filepath)
        filename = "{}.csv".format(filepath)
        with open(filename, 'w', encoding='utf-16', newline='') as file:
            fieldnames = ["Last", "First", "Joined", "Left"]
            writer = csv.DictWriter(
                file, fieldnames=fieldnames, delimiter='\t')
            writer.writeheader()
            for item in self.data:
                writer.writerow(self.data[item])
        self.details_var.set(
            value="File Downloaded\t{}".format(
                self.details_var.get()))

    def end_task(self):
        self.root.destroy()

    def reset(self):
        self.status_var.set('')
        self.details_var.set('')
        self.upload_file_button.config(state='normal')
        self.upload_var.set('')
        self.organize_data_button.config(state='disabled')
        self.download_file_button.config(state='disabled')
        self.download_var.set('')

def main():
    organizer = AttendanceOrganizer()
    organizer.display()

if __name__ == '__main__':
    main()
