#! python3
# attendance_organizer.py

import csv
import re
import tkinter

class AttendanceOrganizer:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.attributes("-topmost", True)
        self.root.title("Attendance Organizer")
        self.upload_file = tkinter.Button(
            self.root, text="Upload File", command=lambda: self.UploadFile)
        self.display()

    def display(self):
        self.upload_file.grid(row=1, column=0)
        self.root.mainloop()

    def UploadFile(self):
        pass

def main():
    organizer = AttendanceOrganizer()

if __name__ == '__main__':
    main()
