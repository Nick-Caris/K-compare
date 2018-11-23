import csv
import sys
import numpy as np

'''
   convertIntoArray is a function there you put in a file of raw data and get a np array as output.

   Usage:
   clusterplot(X, clusterid)
   clusterplot(X, clusterid, centroids=c_matrix, y=y_matrix)
   clusterplot(X, clusterid, centroids=c_matrix, y=y_matrix, covars=c_tensor)

   Input:
   Filename     The location and name of the file you want to convert to an np array
   lineStart    The line of the file where the actual data starts
   length       The number of rows in the data file
   
   Output:
   array        The data converted to an np array
   '''


def convertIntoArray(filename, lineStart, length):
    array = np.empty([length, 19])

    with open(filename, 'r') as f:
        reader = csv.reader(f)
        try:
            for row in reader:
                if reader.line_num >= lineStart:
                    row.pop(0)
                    array[reader.line_num - lineStart] = np.array(row)
        except csv.Error as e:
            sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
        return array

#
# Two examples with our data set's
#
# print(convertIntoArray('Data/segmentation_data.txt', 6, 210))
#
# print(convertIntoArray('Data/segmentation_test.txt', 6, 2100)[0])
