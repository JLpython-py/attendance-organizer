#! python3
# functional_tests.py

import csv
import os
import re
import time
import tkinter
import tkinter.filedialog
import unittest

import psutil
import pyautogui

from attendance_organizer import AttendanceOrganizer

class TestOrganizeAttendance(unittest.TestCase):

    def setUp(self):
        #User opens attendance organizer application
        self.organizer = AttendanceOrganizer()

    def tearDown(self):
        #User clicks button and the attendance organizer application closes
        self.organizer.end_task_button.invoke()

        #Delete produced file
        os.remove(os.path.join('.', 'tests', 'new_sample_attendance.csv'))

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

        #User notices 'Organize Data' button which is disabled
        self.assertEqual(
            self.organizer.organize_data_button['state'], 'disabled')

        #User clicks button and their computer's files appear
        self.organizer.upload_file_button.invoke()
        self.assertIn(
            "explorer.exe", [p.name() for p in psutil.process_iter()])

        #User selects a file to be uploaded
        filepath = os.path.abspath(
            os.path.join('.', 'tests', 'sample_attendance.csv'))
        pyautogui.PAUSE = 2.5
        pyautogui.hotkey('alt', 'd')
        pyautogui.typewrite(filepath)
        pyautogui.hotkey('enter')

        #User notices path to file in an entry widget
        self.assertEqual(
            filepath, self.organizer.upload_var.get())

        #User notices 'Organize Data' button is not disabled
        self.assertEqual(
            self.organizer.upload_file_button['state'], 'normal')

        #User clicks button and file starts to organize
        self.organizer.organize_data_button.invoke()

        #User notices 'Download Data' button appear
        self.assertEqual(
            self.organizer.download_file_button['state'], 'normal')

        #User clicks button and their computer's files appear
        self.organizer.download_file_button.invoke()
        self.assertIn(
            "explorer.exe", [p.name() for p in psutil.process_iter()])

        #User submits a path to download the file
        filepath = os.path.abspath(
            os.path.join('.', 'tests', 'new_sample_attendance.csv'))

        #User notices the new file appears in the computer's files
        self.assertTrue(os.path.exists(filepath))

        #User notices 'End Task' button
        self.assertEqual(
            self.organizer.end_task_button['state'], 'normal')

if __name__ == '__main__':
    unittest.main()
