#Question3+Bonus1
import argparse
import csv

def main():
    parser = argparse.ArgumentParser(
            description='Generates a random data csv file.'
        )
    parser.add_argument(
        'filename',
        help='Name of the csv file to be normalized.',
    )
    parser.add_argument(
        '--delimiter',
        help='Character to be used as delimiter.',
        default='|'
    )
    parser.add_argument(
        '--quote',
        help='Character to be used as quote.',
        default='"'
    )
    args = parser.parse_args()

    with open(args.filename, 'r') as f:
        reader = csv.reader(f, delimiter=args.delimiter, 
                            quotechar=args.quote)
        rows = [row for row in reader]
        
    with open(f'output_{args.filename}', 'w') as f2:
        writer = csv.writer(f2, delimiter=',', quotechar=args.quote)
        writer.writerows(rows)

if __name__ == '__main__':
    main()