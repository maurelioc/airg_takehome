#Question 2
import argparse
import csv

from faker import Faker

def generate_random_data(rows: int) -> None:
    """Method to create rows random data"""
    fake = Faker()
    for _ in range(rows):
        yield [fake.pyint(),f'{fake.name()}']

def main():
  parser = argparse.ArgumentParser(
        description='Generates a random data csv file.'
    )
  parser.add_argument(
      'filename',
      help='A name for the csv file',
  )
  parser.add_argument(
      'rows',
      help='Amount of rows in the file',
  )

  args = parser.parse_args()
  data = generate_random_data(int(args.rows))

  with open(args.filename, 'w') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerows(data)

if __name__ == '__main__':
    main()