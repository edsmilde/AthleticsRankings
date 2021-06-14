from numpy import loadtxt

from keras.models import Sequential
from keras.layers import Dense

import csv




def loadColumnFromFile(filename):
    newArray = []
    with open(filename) as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
        for row in csvReader:
            newItem = row[0]
            newArray.append(newItem)
    return newArray


print("Loading athlete and location indices...")

athleteIndexFilename = "data/index_athlete_1500.csv"
locationIndexFilename = "data/index_location_1500.csv"

athletes = loadColumnFromFile(athleteIndexFilename)
locations = loadColumnFromFile(locationIndexFilename)

FIXED_COLUMNS = 6

athleteColumns = 2*len(athletes)
locationColumns = len(locations)


print("Loading dataset...")

positionMatrixFilename = "data/matrix_position_1500.csv"
dataset = loadtxt(positionMatrixFilename, delimiter=',')

inputWidth = athleteColumns

X = dataset[:,FIXED_COLUMNS:FIXED_COLUMNS+inputWidth]
y = dataset[:,2]

print("Creating model...")

model = Sequential()
model.add(Dense(inputWidth, input_dim=inputWidth, activation='sigmoid'))
model.add(Dense(inputWidth, activation='sigmoid'))
model.add(Dense(100, activation='sigmoid'))
model.add(Dense(20, activation='sigmoid'))
model.add(Dense(1, activation='relu'))

# compile the keras model
print("Compiling model...")
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# fit the keras model on the dataset
print("Fitting model...")
model.fit(X, y, epochs=30, batch_size=10, verbose=1)
# evaluate the keras model
_, accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))
# make class predictions with the model
predictions = model.predict_classes(X)
# summarize the first 5 cases
# for i in range(5):
# 	print('%s => %d (expected %d)' % (X[i].tolist(), predictions[i], y[i]))


print("Saving model...")

positionModelFilename = "model/model_position_1500.json"
model_json = model.to_json()
with open(positionModelFilename, "w") as jsonFile:
    jsonFile.write(model_json)

positionWeightsFilename = "model/weights_position_1500.h5"
model.save_weights(positionWeightsFilename)



