#Question3+Bonus2
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
        help='Character to be used as delimiter.'
    )
    parser.add_argument(
        '--quote',
        help='Character to be used as quote.'
    )
    args = parser.parse_args()

    with open(args.filename, 'r') as f:
        if not args.delimiter and not args.quote:
            dialect = csv.Sniffer().sniff(f.read(1024))
            f.seek(0)
            reader = csv.reader(f, dialect)
        elif not args.delimiter:
            delimiter = '|'
            reader = csv.reader(f, delimiter=delimiter,
                                quotechar=args.quote)
        elif not args.quote:
            quote = '"'
            reader = csv.reader(f, delimiter=args.delimiter,
                                quotechar=quote)
        else:
            reader = csv.reader(f, delimiter=args.delimiter,
                                quotechar=args.quote)
        rows = [row for row in reader]
        
    with open(f'output_{args.filename}', 'w') as f2:
        writer = csv.writer(f2, delimiter=',', quotechar=args.quote)
        writer.writerows(rows)

if __name__ == '__main__':
    main()