

def getCountUniqueValues(dataToRead, key):
    keyValueCount = {}
    for dataRow in dataToRead:
        keyValue = dataRow[key]
        if keyValue not in keyValueCount:
            keyValueCount[keyValue] = 1
        else:
            keyValueCount[keyValue] += 1
    return keyValueCount

def filterOutUncommonValue(dataToFilter : list, key, threshold):
    keyValueCount = getCountUniqueValues(dataToFilter, key)
    # keyValueCount = {}
    # for dataRow in dataToFilter:
    #     keyValue = dataRow[key]
    #     if keyValue not in keyValueCount:
    #         keyValueCount[keyValue] = 1
    #     else:
    #         keyValueCount[keyValue] += 1
    filteredData = []
    for dataRow in dataToFilter:
        keyValue = dataRow[key]
        if keyValueCount[keyValue] >= threshold:
            filteredData.append(dataRow)
    return filteredData

def getAllUniqueValues(dataToRead, key):
    uniqueValues = []
    for dataRow in dataToRead:
        thisValue = dataRow[key]
        if thisValue not in uniqueValues:
            uniqueValues.append(thisValue)
    return uniqueValues



def getMatrixExpansion(listRef, values):
    listSize = len(listRef)
    expansion = [0] * listSize
    for value in values:
        thisIndex = listRef.index(value)
        expansion[thisIndex] = 1
    return expansion






