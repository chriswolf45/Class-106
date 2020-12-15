import csv 
import numpy as np
def getDataSoucre(data_path):
    sizeOfTv = []
    averageTimeSpent = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sizeOfTv.append(float(row["Size of TV"]))
            averageTimeSpent.append(float(row["\tAverage time spent watching TV in a week (hours)"]))
    return{"x":sizeOfTv,"y":averageTimeSpent}
def findCorrelation(dataSoucre):
    correlation = np.corrcoef(dataSoucre["x"],dataSoucre["y"])
    print("correlation is",correlation[0,1])
def setup():
    data_path = "./TV.csv"
    datasoucre = getDataSoucre(data_path)
    findCorrelation(datasoucre)
setup()