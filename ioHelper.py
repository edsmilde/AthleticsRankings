import csv
from numpy import loadtxt


def getMatrixFilename(matrixName, eventName):
    return "data/matrix_" + matrixName + "_" + eventName + ".csv"


def getIndexFileName(indexName, eventName):
    return "data/index_" + indexName + "_" + eventName + ".csv"


def loadColumnFromFile(filename):
    newArray = []
    with open(filename) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            newItem = row[0]
            newArray.append(newItem)
    return newArray


def loadListFromTextFile(filename):
    file = open(filename)
    lines = file.readlines()
    # Strip newlines
    linesStripped = []
    for line in lines:
        lineStripped = line.strip()
        if len(lineStripped) > 0:
            linesStripped.append(lineStripped)
    return linesStripped

def writeListToTextFile(filename, listToWrite):
    file = open(filename, "w")
    for item in listToWrite:
        file.write(item + "\n")


def writeListByName(indexName, eventName, listToWrite):
    indexFilename = getIndexFileName(indexName, eventName)
    writeListToTextFile(indexFilename, listToWrite)

def loadListByName(indexName, eventName):
    indexFilename = getIndexFileName(indexName, eventName)
    return loadListFromTextFile(indexFilename)

def loadIndexByName(indexName, eventName):
    indexFilename = getIndexFileName(indexName, eventName)
    return loadColumnFromFile(indexFilename)

def loadMatrixByName(matrixName, eventName):
    matrixFilename = getMatrixFilename(matrixName, eventName)
    return loadtxt(matrixFilename, delimiter=',')

def loadCsvWithoutHeaders(filename):
    data = []
    with open(filename) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            data.append(row)
    return data

def loadProcessedDataByEvent(eventName):
    filename = "data/processed_" + eventName + ".csv"
    return loadCsvWithoutHeaders(filename)

def writeArrayToCsv(filename, arrayToWrite):
    with open(filename, "w") as csvFile:
        csvWriter = csv.writer(csvFile, delimiter=",")
        for row in arrayToWrite:
            csvWriter.writerow(row)



def writeMatrixByName(matrixName, eventName, arrayToWrite):
    matrixFilename = getMatrixFilename(matrixName, eventName)
    writeArrayToCsv(matrixFilename, arrayToWrite)

