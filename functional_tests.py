#! python3
# functional_tests.py

import os
import unittest

from attendance_organizer import Organizer


class TestAttendanceOrganizer(unittest.TestCase):

    def setUp(self):
        self.organizer = Organizer()

    def tearDown(self):
        if os.path.exists("tests/result.csv"):
            os.remove("tests/result.csv")

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
        self.organizer.download("tests/result.csv")


if __name__ == '__main__':
    unittest.main()
