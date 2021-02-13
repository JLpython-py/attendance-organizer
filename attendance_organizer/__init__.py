#! python3
# attendance_organizer/__init__.py

"""
Rewrites Microsoft TEAMS attendance CSV files
    - Person names are changed from "First Last" to "Last, First"
        - Organized alphabetically
    - Separate rows for actions are replaced by a column for each action
        - Time of action is listed in column of corresponding action
    - Edit time format
==============================================================================
Example Rewritten Data: (Data is taken from tests/sample.csv)
Last	First	Joined	Left
Five	Member	12.08.2020 12:17:37	12.08.2020 12:43:55
Four	Member	12.08.2020 12:17:37	12.08.2020 12:39:52
One	Member	12.08.2020 12:17:37	12.08.2020 12:40:27
Owner	Meeting	12.08.2020 12:17:37
Three	Member	12.08.2020 12:17:37	12.08.2020 12:47:16
Two	Member	12.08.2020 12:17:37	12.08.2020 12:44:02
Zero	Member	12.08.2020 12:17:37	12.08.2020 12:48:51
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


class Organizer:
    """ Reorganize data contained in Microsoft TEAMS attendance CSV file
"""
    def __init__(self):
        self.upload_path = ""
        self.download_path = ""
        self.values = []
        self.data = {}

    class ImproperFileTypeError(Exception):
        """ Raised when the file provided cannot be re-written

        Arguments:
            filepath -- The path to the file which caused the error
            process -- The process which the program attempted to run
"""
        def __init__(self, filepath, process):
            self.filepath = filepath
            self.message = f"Cannot process file: {self.filepath} (On file {process})"
            super().__init__(self.message)

    def upload(self, filepath):
        """ Read store data contained in CSV file
"""
        if not (
            filepath and os.path.splitext(filepath)[-1] == '.csv'
        ):
            raise self.ImproperFileTypeError(
                filepath,
                process="upload"
            )
        self.upload_path = filepath
        with open(self.upload_path, encoding="utf-16") as file:
            self.values = list(csv.reader(file, delimiter='\t'))
            del self.values[0]

    def organize(self):
        """ Reorganize data stored in the original CSV file
"""
        name_regex = re.compile(r'([A-Z][A-Za-z]+) ([A-Z][A-Za-z]+)')
        action_regex = re.compile(r'(Joined|Left)')
        dt_format = '%m/%d/%Y, %I:%M:%S %p'
        data = {}
        for row in self.values:
            try:
                raw_name = name_regex.search(row[0])
                raw_action = action_regex.search(row[1])
                first, last = raw_name.group(1), raw_name.group(2)
                action = raw_action.group(1).title()
                time = datetime.datetime.strptime(
                    row[2], dt_format
                ).strftime('%m.%d.%Y %H:%M:%S')
            except (AttributeError, IndexError, ValueError) as error:
                raise self.ImproperFileTypeError(
                    self.upload_path,
                    "organize",
                ) from error
            key = ', '.join([last, first])
            data.setdefault(
                key, {"Last": last, "First": first}
            )
            data[key].setdefault(action, time)
        self.data = {k: data[k] for k in sorted(list(data))}

    def download(self, filepath):
        """ Write reorganized data to a CSV file
"""
        if not (
            os.path.splitext(filepath)[-1] == '.csv'
        ):
            raise self.ImproperFileTypeError(
                filepath,
                process="download"
            )
        self.download_path = filepath
        with open(self.download_path, "w", encoding="utf-16", newline="") as file:
            fieldnames = ["Last", "First", "Joined", "Left"]
            writer = csv.DictWriter(
                file, fieldnames=fieldnames, delimiter='\t'
            )
            writer.writeheader()
            for item in self.data:
                writer.writerow(self.data[item])
