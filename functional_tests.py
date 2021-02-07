#! python3
# functional_tests.py

"""
Functional tests for attendance_organizer module
==============================================================================
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

import os
import threading
import time
import unittest

import pyautogui

from attendance_organizer import Organizer
import application


class TestAttendanceOrganizer(unittest.TestCase):
    """ Functiona test for attendance_organizer module
"""
    def setUp(self):
        self.organizer = Organizer()

    def tearDown(self):
        if os.path.exists("tests/results.csv"):
            os.remove("tests/results.csv")

    def test_module(self):
        # Uploading nonexistent file throws error
        with self.assertRaises(Organizer.ImproperFileTypeError):
            self.organizer.upload(
                "the/file/path/does/not/exist"
            )

        # Uploading file with improper file type throws error
        with self.assertRaises(Organizer.ImproperFileTypeError):
            self.organizer.upload(
                "tests/improper.txt"
            )

        # Uploading file with improper formatting throws error
        with self.assertRaises(Organizer.ImproperFileTypeError):
            self.organizer.upload(
                "tests/improper.csv"
            )
            self.organizer.organize()

        # Upload proper file
        self.organizer.upload("tests/sample.csv")

        # Organizer data
        self.organizer.organize()

        # Download resultant data as file
        self.organizer.download("tests/results.csv")


def automate_file_dialogue(filepath):
    # Wait for tkinter file dialogue to open
    time.sleep(2)
    directory, filename = os.path.split(filepath)
    # Enter directory into File Explorer adress search bar
    pyautogui.hotkey('alt', 'd')
    pyautogui.typewrite(directory)
    pyautogui.hotkey('enter')
    # Enter filename into filename search bar
    pyautogui.hotkey('alt', 'n')
    pyautogui.typewrite(filename)
    pyautogui.hotkey('enter')


class TestGUI(unittest.TestCase):
    """ Functional test for attendance_organizer GUI wrapper
"""
    def setUp(self):
        self.interface = application.Interface()

    def tearDown(self):
        self.interface.end_task_button.invoke()
        if os.path.exists("tests/results.csv"):
            os.remove("tests/results.csv")

    def test_tkinter_interface(self):
        # tkinter application opens
        self.assertEqual(
            self.interface.root.state(),
            'normal'
        )
        self.assertEqual(
            self.interface.root.title(), "Attendance Organizer"
        )

        # Check original application button states
        self.assertEqual(
            self.interface.upload_button['state'], 'normal'
        )
        self.assertEqual(
            self.interface.organize_button['state'], 'disabled'
        )
        self.assertEqual(
            self.interface.download_button['state'], 'disabled'
        )
        self.assertEqual(
            self.interface.end_task_button['state'], 'normal'
        )
        self.assertEqual(
            self.interface.reset_button['state'], 'normal'
        )

        # Click 'Upload File' button
        filepath = os.path.abspath(
            os.path.join('tests', 'sample.csv')
        )
        upload_thread = threading.Thread(
            target=automate_file_dialogue,
            args=(filepath,)
        )
        upload_thread.start()
        self.assertTrue(os.path.exists(filepath))
        self.interface.upload_button.invoke()
        upload_thread.join()

        # Path to file appears in entry widget
        self.assertEqual(
            os.path.normpath(filepath),
            os.path.normpath(self.interface.upload_var.get())
        )

        # 'Organize Data' button state changes to normal
        self.assertEqual(
            self.interface.organize_button['state'], 'normal'
        )

        # Click 'Organize Data' button
        self.interface.organize_button.invoke()

        # 'Organize Data' button state changes to disabled
        self.assertEqual(
            self.interface.organize_button['state'], 'disabled'
        )

        # 'Download File' button state changes to normal
        self.assertEqual(
            self.interface.download_button['state'], 'normal'
        )

        # Click 'Download File' button
        filepath = os.path.abspath(
            os.path.join('tests', 'results')
        )
        download_thread = threading.Thread(
            target=automate_file_dialogue,
            args=(filepath,)
        )
        download_thread.start()
        self.assertFalse(os.path.exists(filepath))
        self.interface.download_button.invoke()
        download_thread.join()

        # Click 'Reset' button
        self.interface.reset_button.invoke()
        self.assertEqual(
            self.interface.upload_button['state'], 'normal'
        )
        self.assertEqual(
            self.interface.organize_button['state'], 'disabled'
        )
        self.assertEqual(
            self.interface.download_button['state'], 'disabled'
        )
        self.assertEqual(
            self.interface.end_task_button['state'], 'normal'
        )
        self.assertEqual(
            self.interface.reset_button['state'], 'normal'
        )
        self.assertEqual(
            self.interface.status_var.get(), ''
        )
        self.assertEqual(
            self.interface.details_var.get(), ''
        )
        self.assertEqual(
            self.interface.upload_var.get(), ''
        )
        self.assertEqual(
            self.interface.download_var.get(), ''
        )


if __name__ == '__main__':
    unittest.main()
