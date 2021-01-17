#! python3
# functional_tests.py

import csv
import logging
import os
import re
import threading
import time
import tkinter
import tkinter.filedialog
import unittest

import psutil
import pyautogui

from attendance_organizer import AttendanceOrganizer

logging.basicConfig(
    level=logging.DEBUG,
    format=' %(asctime)s - %(levelname)s - %(message)')

class TestOrganizeAttendance(unittest.TestCase):

    def setUp(self):
        #User opens attendance organizer application
        self.organizer = AttendanceOrganizer()

    def tearDown(self):
        #User clicks button and the attendance organizer application closes
        self.organizer.end_task_button.invoke()

        #Delete produced file
        os.remove(os.path.join('.', 'tests', 'new_sample_attendance.csv'))

    def automate_file_dialogue(self, filepath):
        while "explorer.exe" not in [p.name() for p in psutil.process_iter()]:
            continue
        directory, filename = os.path.split(filepath)
        pyautogui.hotkey('alt', 'd')
        pyautogui.typewrite(directory)
        pyautogui.hotkey('enter')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        pyautogui.hotkey('alt', 'n')
        pyautogui.typewrite(filename)
        pyautogui.hotkey('enter')
        
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

        #User clicks button and select path to upload
        filepath = os.path.abspath(
            os.path.join('tests', 'sample_attendance.csv'))
        upload_thread = threading.Thread(
            target=self.automate_file_dialogue, args=(filepath,))
        upload_thread.start()
        self.assertTrue(os.path.exists(filepath))
        self.organizer.upload_file_button.invoke()
        self.assertIn(
            "explorer.exe", [p.name() for p in psutil.process_iter()])
        upload_thread.join()

        #User notices path to file in an entry widget
        self.assertEqual(
            os.path.normpath(filepath),
            os.path.normpath(self.organizer.upload_var.get()))

        #User notices 'Organize Data' button is not disabled
        self.assertEqual(
            self.organizer.upload_file_button['state'], 'normal')

        #User clicks button and file starts to organize
        self.organizer.organize_data_button.invoke()

        #User notices 'Download Data' button appear
        self.assertEqual(
            self.organizer.download_file_button['state'], 'normal')

        #User clicks button and selects path to download
        filepath = os.path.abspath(
            os.path.join('tests', 'new_sample_attendance'))
        download_thread = threading.Thread(
            target=self.automate_file_dialogue, args=(filepath,))
        download_thread.start()
        self.assertFalse(os.path.exists(filepath))
        self.organizer.download_file_button.invoke()
        self.assertIn(
            "explorer.exe", [p.name() for p in psutil.process_iter()])
        download_thread.join()

        #User notices 'Reset' button
        self.assertEqual(
            self.organizer.reset_button['state'], 'normal')

        #User clicks button and notices window is reset
        self.organizer.reset_button.invoke()
        self.assertEqual(
            self.organizer.status_var.get(), '')
        self.assertEqual(
            self.organizer.details_var.get(), '')
        self.assertEqual(
            self.organizer.upload_file_button['state'], 'normal')
        self.assertEqual(
            self.organizer.upload_var.get(), '')
        self.assertEqual(
            self.organizer.organize_data_button['state'], 'disabled')
        self.assertEqual(
            self.organizer.download_file_button['state'], 'disabled')
        self.assertEqual(
            self.organizer.download_var.get(), '')
        
        #User notices 'End Task' button
        self.assertEqual(
            self.organizer.end_task_button['state'], 'normal')

if __name__ == '__main__':
    unittest.main()
