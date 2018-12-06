import csv
import sys
import numpy as np

'''
   convertIntoArray is a function there you put in a file of raw data and get a np array as output.

   Input:
   Filename     The location and name of the file you want to convert to an np array
   lineStart    The line of the file where the actual data starts
   length       The number of rows in the data file
   
   Output:
   array        The data converted to an np array
 '''


def convertIntoArray(filename, numOfAtt, lineStart, length):
    array = np.empty([length, numOfAtt])

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                if lineStart <= reader.line_num <= length:
                    # row.pop(0)
                    array[reader.line_num - lineStart] = np.array(row)
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
        return array


'''
   This function helps test the row you want to take from USCensus1990.data.txt
   It prints the first 10 value's and prints the label

   Input:
   rowNumber     The row number you want to test

   Output:
   print        The printed row and data
 '''


def testRow(rownNumber):
    print(convertIntoArray('Data/USCensus1990.data.txt', 69, 2, 10)[:, rownNumber])
    with open('Data/USCensus1990.data.txt', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[rownNumber])
            break
