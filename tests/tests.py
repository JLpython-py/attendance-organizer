#! python3
# tests.py

import csv
import datetime
import os
import re
import unittest

class TestUploadFiled(unittest.TestCase):

    def test_file_properties(self):
        sample_file = os.path.join('tests', 'sample_attendance.csv')
        self.assertEqual(
            os.path.splitext(sample_file)[-1],
            '.csv')

    def test_file_contents_exist(self):
        sample_file = os.path.join('tests', 'sample_attendance.csv')
        with open(sample_file, encoding='utf-16') as file:
            data = list(csv.reader(file, delimiter='\t'))
            headers = data.pop(0)
        self.assertTrue(data)
        self.assertEqual(headers, ["Full Name", "User Action", "Timestamp"])

class TestOrganizeData(unittest.TestCase):

    def open_file(self):
        sample_file = os.path.join('tests', 'sample_attendance.csv')
        with open(sample_file, encoding='utf-16') as file:
            values = list(csv.reader(file, delimiter='\t'))
            del values[0]
        return values
        
    def test_name_regular_expression(self):
        regex = re.compile(r'([A-Z][A-Za-z]+) ([A-Z][A-Za-z]+)')
        values = self.open_file()
        for row in values:
            self.assertTrue(regex.search(row[0]))

    def test_action_regular_expression(self):
        regex = re.compile(r'(Joined|Left)')
        values = self.open_file()
        for row in values:
            self.assertTrue(regex.search(row[1]))

    def test_datetime_format(self):
        form = '%m/%d/%Y, %I:%M:%S %p'
        values = self.open_file()
        for row in values:
            self.assertTrue(datetime.datetime.strptime(row[2], form))

if __name__ == '__main__':
    unittest.main()
