import argparse
import csv
import os
from unittest.mock import patch

from faker import Faker

from question2 import generate_random_data
from question2 import main

def test_generate_random_data():
    fake = Faker()
    length = fake.pyint()
    result = generate_random_data(length)
    assert len(list(result)) == length
    for row in result:
        assert len(row) == 2
        assert isinstance(row[0], int)
        assert isinstance(row[1], str)

def test_main():
    fake = Faker()
    filename = os.path.join('.',fake.file_path(extension='csv', depth=0).replace('/',''))    
    rows = fake.pyint()
    
    with patch('question2.argparse.ArgumentParser.parse_args', 
                return_value=argparse.Namespace(filename=filename, rows=rows)):
        main()

    assert os.path.exists(filename)
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        data = list(csv_reader)
        assert len(data) == rows
        for row in data:
            assert len(row) == 2
            assert row[0].isnumeric()
            assert isinstance(row[1], str)

    os.remove(filename)