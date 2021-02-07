#! python3
# attendance_organizer/__init__.py

"""
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

    def __init__(self):
        self.upload_path = ""
        self.download_path = ""
        self.values = []
        self.data = {}

    class ImproperFileTypeError(Exception):

        def __init__(self, filepath, process):
            self.filepath = filepath
            self.message = f"Cannot process file: {self.filepath} (On file {process})"
            super().__init__(self.message)

    def upload(self, filepath):
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
                ).strftime('%m.%d%Y %H:%M:%S')
            except (AttributeError, IndexError, ValueError):
                raise self.ImproperFileTypeError(
                    self.upload_path,
                    "organize",
                )
            key = ', '.join([last, first])
            data.setdefault(
                key, {"Last": last, "First": first}
            )
            data[key].setdefault(action, time)
        self.data = {k: data[k] for k in sorted(list(data))}

    def download(self, filepath):
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