import math
from calcFunctions import *

def trainPearsonWeights(data, activeUserData, averages):
    # List of items the active user as rated
    userItemList = [elt[1] for elt in activeUserData if elt[2] != 0]
    # List of active user's ratings
    userRatings = [elt[2] for elt in activeUserData if elt[2] != 0]
    # List of items to predict
    itemsToPredict = [elt[1] for elt in activeUserData if elt[2] == 0]
    # Calculate the average rating of the active user
    userAvg = 0.0
    for elt in userRatings:
        userAvg += elt
    userAvg /= len(userRatings)
    userAvg += 0.001    # Form of add-one smoothing
    # Normalize the ratings of the active user to the average rating
    for i in range(len(userRatings)):
        userRatings[i] = userRatings[i] - userAvg
    weights = []
    num = 0
    for user in data:
        inactiveRatings = []
        activeRatings = []
        num += 1
        itemNum = 0
        for item in userItemList:
            if (user[item - 1] != 0):
                inactiveRatings.append(user[item - 1] - averages[num - 1])
                activeRatings.append(userRatings[itemNum])
            itemNum += 1
        if len(inactiveRatings) != 0:
            weight = cosSimilarity(inactiveRatings, activeRatings)
            weights.append([weight, num])
    return weights, itemsToPredict, userAvg

def predictPearsonUBCF(userID, data, weights, itemsToPredict, userAvg, averages):
    numerator = 0.0
    denominator = 0.0
    predictions = []
    for item in itemsToPredict:
        for user in weights:
            if (data[user[1] - 1][item - 1] != 0):
                numerator += (user[0] * (data[user[1] - 1][item - 1] - averages[user[1] - 1]))
                denominator += abs(user[0])
        quotient = numerator / denominator
        predictions.append([userID, item, round(userAvg + quotient)])
        
    return predictions
