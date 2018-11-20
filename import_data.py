import csv
import sys

filename = 'Data/segmentation_data.txt'
with open(filename, 'r') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
