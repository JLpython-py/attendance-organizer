#! python3
# tests.py

"""
Unit tests for attendance_organizer module
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

import csv
import datetime
import os
import re
import unittest


class TestUploadFiled(unittest.TestCase):

    def test_file_properties(self):
        sample_file = os.path.join('tests', 'sample.csv')
        self.assertEqual(
            os.path.splitext(sample_file)[-1],
            '.csv')

    def test_file_contents_exist(self):
        sample_file = os.path.join('tests', 'sample.csv')
        with open(sample_file, encoding='utf-16') as file:
            data = list(csv.reader(file, delimiter='\t'))
            headers = data.pop(0)
        self.assertTrue(data)
        self.assertEqual(headers, ["Full Name", "User Action", "Timestamp"])


class TestOrganizeData(unittest.TestCase):

    def setUp(self):
        self.open_file()

    def open_file(self):
        with open(os.path.join('tests', 'sample.csv'), encoding='utf-16') as file:
            self.values = list(csv.reader(file, delimiter='\t'))
            del self.values[0]

    def test_name_regular_expression(self):
        regex = re.compile(r'([A-Z][A-Za-z]+) ([A-Z][A-Za-z]+)')
        for row in self.values:
            self.assertTrue(regex.search(row[0]))

    def test_action_regular_expression(self):
        regex = re.compile(r'(Joined|Left)')
        for row in self.values:
            self.assertTrue(regex.search(row[1]))

    def test_datetime_format(self):
        form = '%m/%d/%Y, %I:%M:%S %p'
        for row in self.values:
            self.assertTrue(datetime.datetime.strptime(row[2], form))


if __name__ == '__main__':
    unittest.main()
