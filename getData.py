
import csv
import re


# Processing helper functions
#

def processRawMark(rawMark):
    splitMark = re.split(r'\D', rawMark)
    minuteString = splitMark[0]
    secondString = splitMark[1]
    decimalString = splitMark[2]
    mark = int(minuteString)*60 + int(secondString) + int(decimalString)/100
    altitude = 0
    enRoute = 0
    if re.match(r'A', rawMark):
        altitude = 1
    if re.match(r'\+', rawMark):
        enRoute = 1
    return (mark, altitude, enRoute)

MONTH_STRINGS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

def processRawDate(rawDate):
    day = 0
    month = 0
    year = 0
    splitDate = re.split(r' ', rawDate)
    if len(splitDate) == 1:
        year = 2000 # int(splitDate[0])
    if len(splitDate) >= 3:
        day = int(splitDate[0]) - 1
        month = MONTH_STRINGS.index(splitDate[1])
        year = int(splitDate[2])
    return (day, month, year)

def processRawPos(rawPos):
    posParts = re.split(r'\D', rawPos)
    pos = posParts[0]
    if not pos:
        pos = 1
    isPrelim = 0
    if re.match(r'\D', rawPos):
        isPrelim = 1
    return (pos, isPrelim)
    


def processRow(row):
    rawMark = row[0]
    athlete = row[3]
    nationality = row[4]
    rawPos = row[6]
    meeting = row[7]
    location = row[8]
    rawDate = row[9]
    (mark, altitude, enroute) = processRawMark(rawMark)
    (day, month, year) = processRawDate(rawDate)
    (pos, isPrelim) = processRawPos(rawPos)
    raceHashTuple = (location, rawDate)
    raceHash = hash(raceHashTuple)
    processedRowData = [mark, raceHash, athlete, altitude, enroute, nationality, meeting, location, day, month, year, pos, isPrelim]
    return processedRowData




# Process CSV
#

processedData = []

yearsToProcess = range(2010,2022)

for yearToProcess in yearsToProcess:
    rawDataFilename = "data/raw_1500_" + str(yearToProcess) + "_final.txt"
    with open(rawDataFilename) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            processedRow = processRow(row)
            processedData.append(processedRow)

# Get unique athletes
#
INDEX_ATHLETE = 2
INDEX_RACEHASH = 1

allAthletes = []
allRaces = []

for processedDataRow in processedData:
    athlete = processedDataRow[INDEX_ATHLETE]
    if athlete not in allAthletes:
        allAthletes.append(athlete)
    raceHash = processedDataRow[INDEX_RACEHASH]
    if raceHash not in allRaces:
        allRaces.append(raceHash)


processedDataFilename = "data/processed_1500.csv"
with open(processedDataFilename, "w") as csvFile:
    csvWriter = csv.writer(csvFile, delimiter=",")
    for processedDataRow in processedData:
        csvWriter.writerow(processedDataRow)


print("Total athletes found: " + str(len(allAthletes)))
print("Total races found: " + str(len(allRaces)))







