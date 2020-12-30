#! python3
# functional_tests.py

import csv
import re
import tkinter
import unittest

class TestOrganizeAttendance(unittest.TestCase):

    def setUp(self):
        self.root = tkinter.Tk()
        self.root.attributes("-topmost", True)
        self.root.title("Attendance Organizer")

    def tearDown(self):
        self.root.destroy()

    def verify_file_properties(self):
        pass

    def test_file_upload_organize_and_download(self):
        #User notices new tkinter window
        self.assertEqual(self.root.state(), 'normal')

        #User notices window title
        self.assertEqual(self.root.title(), "Attendance Organizer")

        #User notices 'Upload File' button
        #User clicks button and their computer's files appear
        #User selects a file to be uploaded
        #Verify file properties
        self.verify_file_properties()

        #Verification fails as user uploaded wrong file
        #User selects the correct file to be uploaded
        #Verify file properties
        self.verify_file_properties()

        #Verification passes and file is uploaded
        #User notices path to file in an entry widget
        #User notices 'Organize Attendance' button
        #User clicks button and file starts to organize
        #User notices loading bar, which increases as process continues
        #When organization is completed, notification pops up
        #User notices new path to file in an entry widget
        #User notices 'Download File' button
        #User clicks button and the file downloads

if __name__ == '__main__':
    unittest.main()
