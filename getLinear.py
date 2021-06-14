import numpy
import csv
import linear
import ioHelper


def getLinearModelForAthlete(eventName):
    athletes = ioHelper.loadListByName("athlete", eventName)
    numAthletes = len(athletes)
    locations = ioHelper.loadListByName("locations", eventName)
    numLocations = len(locations)
    dataset = ioHelper.loadMatrixByName("position", eventName)
    datasetWidth = len(dataset[0])
    fixedColumns = datasetWidth - 2*numAthletes - numLocations
    X = dataset[:,fixedColumns:fixedColumns+2*numAthletes]
    Y = dataset[:,0]
    athleteCounts = dataset[:,1]
    theta = linear.getCoefficientsAddNormalization(X, Y)
    coefficients = theta[0]
    residuals = theta[3]
    baseVal = coefficients[0]
    athleteVals = coefficients[1:numAthletes+1]
    athleteAsOpponentVals = coefficients[numAthletes+1:2*numAthletes+1]
    model = []
    for i in range(numAthletes):
        athlete = athletes[i]
        athleteCount = athleteCounts[i]
        athleteVal = athleteVals[i]
        athleteAsOpponentVal = athleteAsOpponentVals[i]
        athleteAbsoluteVal = athleteVal + baseVal
        athleteAsOpponentAbsoluteVal = athleteVal + baseVal
        athleteRelativeVal = athleteVal - athleteAsOpponentVal
        outputRow = [athlete, athleteCount, athleteVal,
            athleteAsOpponentVal, athleteAbsoluteVal,
            athleteAsOpponentAbsoluteVal, athleteRelativeVal]
        model.append(outputRow)
    return model


def getLinearModelForLocation(eventName):
    athletes = ioHelper.loadListByName("athlete", eventName)
    locations = ioHelper.loadListByName("location", eventName)
    dataset = ioHelper.loadMatrixByName("position", eventName)

    return


thisModel = getLinearModelForAthlete("1500")

ioHelper.writeArrayToCsv("data/coefficients_position_1500.csv", thisModel)


