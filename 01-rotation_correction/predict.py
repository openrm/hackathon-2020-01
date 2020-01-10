import os
import sys
import csv
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--image_dir',
                        type=str)
    parser.add_argument('-o', '--output',
                        type=argparse.FileType('w'),
                        default=sys.stdout)

    args = parser.parse_args()

    files =  [
        filename for filename in os.listdir(args.image_dir)
        if os.path.splitext(filename)[-1].lower() in ['.jpg', '.png']
    ]

    writer = csv.writer(args.output)
    for filename in files:
        writer.writerow([filename, -1])
