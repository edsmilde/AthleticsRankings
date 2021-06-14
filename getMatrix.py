import csv

import ioHelper, dataHelper


INDEX_MARK = 0
INDEX_RACE = 1
INDEX_ATHLETE = 2
INDEX_LOCATION = 7
INDEX_RANK = 11

MIN_ATHLETE = 5
MIN_RACE = 5
MIN_ATHLETE_SECOND = 3

data = ioHelper.loadProcessedDataByEvent("1500")

print("Before filter: " + str(len(data)))

data = dataHelper.filterOutUncommonValue(data, INDEX_ATHLETE, MIN_ATHLETE)
data = dataHelper.filterOutUncommonValue(data, INDEX_RACE, MIN_RACE)
data = dataHelper.filterOutUncommonValue(data, INDEX_ATHLETE, MIN_ATHLETE_SECOND)

## Map values to IDs

allAthletes = dataHelper.getAllUniqueValues(data, INDEX_ATHLETE)
allRaces = dataHelper.getAllUniqueValues(data, INDEX_RACE)
allLocaitons = dataHelper.getAllUniqueValues(data, INDEX_LOCATION)

athleteCounts = dataHelper.getCountUniqueValues(data, INDEX_ATHLETE)
locationCounts = dataHelper.getCountUniqueValues(data, INDEX_LOCATION)

print("After filter: results=" + str(len(data)) + ", athletes=" + str(len(allAthletes)))


## Get race-athlete mapping

athleteRankByRace = {}

for dataRow in data:
    race = dataRow[INDEX_RACE]
    athlete = dataRow[INDEX_ATHLETE]
    rank = dataRow[INDEX_RANK]
    if race not in athleteRankByRace:
        athleteRankByRace[race] = {}
    athleteRankByRace[race][athlete] = rank

athleteFilteredRankByRace = {}

for race in athleteRankByRace:
    if race not in athleteFilteredRankByRace:
        athleteFilteredRankByRace[race] = {}
    for athlete in athleteRankByRace[race]:
        thisAthleteFilteredRank = 1
        for otherAthlete in athleteRankByRace[race]:
            if athlete != otherAthlete:
                if athleteRankByRace[race][athlete] > athleteRankByRace[race][otherAthlete]:
                    thisAthleteFilteredRank += 1
        athleteFilteredRankByRace[race][athlete] = thisAthleteFilteredRank

## Build matrix
matrix = []

for dataRow in data:
    mark = dataRow[INDEX_MARK]
    race = dataRow[INDEX_RACE]
    athlete = dataRow[INDEX_ATHLETE]
    location = dataRow[INDEX_LOCATION]
    filteredRank = athleteFilteredRankByRace[race][athlete]
    otherAthletes = list(athleteFilteredRankByRace[race].keys())
    otherAthletes.remove(athlete)
    matrixRow = []
    athleteExpansion = dataHelper.getMatrixExpansion(allAthletes, [athlete])
    otherAthleteExpansion = dataHelper.getMatrixExpansion(allAthletes, otherAthletes)
    locationExpansion = dataHelper.getMatrixExpansion(allLocaitons, location)
    athleteCount = athleteCounts[athlete]
    locationCount = locationCounts[location]
    matrixRow = [filteredRank, athleteCount, locationCount, mark] + athleteExpansion + otherAthleteExpansion
    matrix.append(matrixRow)


ioHelper.writeListByName("athlete", "1500", allAthletes)
ioHelper.writeListByName("location", "1500", allLocaitons)
ioHelper.writeListByName("race", "1500", allRaces)

ioHelper.writeMatrixByName("position", "1500", matrix)
