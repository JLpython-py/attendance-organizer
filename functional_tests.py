#! python3
# functional_tests.py

import csv
import os
import psutil
import pyautogui
import re
import time
import tkinter
import tkinter.filedialog
import unittest

from attendance_organizer import AttendanceOrganizer

class TestOrganizeAttendance(unittest.TestCase):

    def setUp(self):
        #User opens attendance organizer application
        self.organizer = AttendanceOrganizer()

    def tearDown(self):
        #User closes attendance organizer application
        self.organizer.end_task_button.invoke()

    def verify_file_properties(self):
        pass

    def test_attendance_organizer_window_operation(self):
        #User notices new tkinter window
        self.assertEqual(
            self.organizer.root.state(), 'normal')

        #User notices window title
        self.assertEqual(
            self.organizer.root.title(), "Attendance Organizer")

        #User notices 'Upload File' button
        self.assertEqual(
            self.organizer.upload_file_button['state'], 'normal')

        #User clicks button and their computer's files appear
        self.organizer.upload_file_button.invoke()
        filepath = os.path.abspath(
            os.path.join('tests', 'sample_attendance.csv'))
        time.sleep(1)
        pyautogui.typewrite(filepath)
        print(filepath)
        pyautogui.press('enter')
        self.assertIn(
            "explorer.exe", [p.name() for p in psutil.process_iter()])

        #User selects a file to be uploaded
        #Verify file properties

        #Verification fails as user uploaded wrong file
        #User selects the correct file to be uploaded
        #Verify file properties

        #Verification passes and file is uploaded
        #User notices path to file in an entry widget
        #User notices 'Organize Attendance' button
        #User clicks button and file starts to organize
        #User notices loading bar, which increases as process continues
        #When organization is completed, notification pops up
        #User notices new path to file in an entry widget
        #User notices 'Download File' button
        #User clicks button and the file downloads
        #User notices 'End Task' button
        self.assertEqual(
            self.organizer.end_task_button['state'], 'normal')

if __name__ == '__main__':
    unittest.main()
