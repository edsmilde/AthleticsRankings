from keras.models import model_from_json

import csv

print("Loading model...")

positionModelJsonFilename = "model/model_position_1500.json"
positionModelJsonFile = open(positionModelJsonFilename, "r")
positionModelJson = positionModelJsonFile.read()
positionModelJsonFile.close()

positionModel = model_from_json(positionModelJson)

positionWeightsFilename = "model/weights_position_1500.h5"
positionModel.load_weights(positionWeightsFilename)

print("Compiling model...")
positionModel.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

athletes = []

print("Loading athlete indices...")
athleteIndexFilename = "data/index_athlete_1500.csv"
with open(athleteIndexFilename) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    for row in csvReader:
        athlete = row[0]
        athletes.append(athlete)



inputAthletes = ["Jakob Ingebrigtsen", "Craig Engels", "Sam Prakel", "Matthew Centrowitz", "David Ribich", "Willy Fink", "Timothy Cheruiyot"]
#inputAthletes = ["Jakob Ingebrigtsen", "Timothy Cheruiyot"]
inputAthleteIndices = []

for inputAthlete in inputAthletes:
    inputAthleteIndex = athletes.index(inputAthlete)
    inputAthleteIndices.append(inputAthleteIndex)


inputMatrix = []

#date = [1,7,2019]

date = [1,7,2021]
numAthletes = len(athletes)
fixedRows = len(date)
matrixWidth = fixedRows + numAthletes*2

for inputAthleteIndex in inputAthleteIndices:
    inputMatrixRow = [0] * matrixWidth
    inputMatrixRow[0] = date[0]
    inputMatrixRow[1] = date[1]
    inputMatrixRow[2] = date[2]
    inputMatrixRow[fixedRows + inputAthleteIndex] = 1
    for secondAthleteIndex in inputAthleteIndices:
        if secondAthleteIndex != inputAthleteIndex:
            inputMatrixRow[fixedRows + numAthletes + secondAthleteIndex] = 1
    inputMatrix.append(inputMatrixRow)

prediction = positionModel.predict(inputMatrix)

print(prediction)

