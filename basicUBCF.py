import math
from calcFunctions import *

# --------------------
#   function: performUBCF
#       input(s):
#           - trainData (type - int[n][m]): n x m array where n = # of users and m = # of items
#           - testData (type - int[n][3]): n x 3 array
#               - Column 1: User IDs
#               - Column 2: Item IDs
#               - Column 3: Rating of the item by an active user
#       output(s):
#           - allPredictions (type - int[n][3]): n x 3 array
#               - Column 1: User IDs
#               - Column 2: Item IDs
#               - Column 3: Rating predicted of an item by an active user
# --------------------
def performUBCF(trainData, testData):

    # Variables to set up the loop
    start = 0
    end = 0
    userID = testData[start][0]
    i = 0
    size = len(testData)
    allPredictions = []
    
    while start < size:
    
        # Find the section of the test data for a particular userID
        while (i < size) and (userID == testData[i][0]):
            i += 1
        end = i
        section = slice(start, end)
        
        # Train weights
        weights, itemsToPredict = trainWeights(trainData, testData[section])
        
        # Sort such that the most similar weights are on top
        weights.sort(reverse=True)
        predictions = predict(userID, trainData, weights, itemsToPredict)
        
        # Get next userID
        if i < size:
            userID = testData[i][0]
        start = end
        allPredictions += predictions

    return allPredictions
# --------------------
#   function: predict
#       input(s):
#           - userID (type - int): ID of the current user
#           - data (type -  int[n][m]): n x m array where n = # of users and m = # of items
#           - weights (type - int[m][2]): m x 2 array where m = # of similar users
#               - Column 1: Weight values
#               - Column 2: userIDs
#           - itemsToPredict (type - int[n]): size n array where n = # of items to predict
#       output(s):
#           - predictions (type - int[3][m]): size 3 x m array where m = # of items predicted
#               - Column 1: active userID
#               - Column 2: item ID
#               - Column 3: rating prediction
# --------------------
def predict(userID, data, weights, itemsToPredict):
    numerator = 0.0
    denominator = 0.0
    predictions = []
    
    # For each item to predict
    for item in itemsToPredict:
    
        # For each similar user
        for user in weights:
        
            # If the user has rated the item, include him in the calcuation
            if data[user[1] - 1][item - 1] != 0:
                numerator += (user[0] * data[user[1] - 1][item - 1])
                denominator += user[0]
        
        # Save prediction
        predictions.append([userID, item, round(numerator/denominator)])
        
    return predictions

# --------------------
#   function: trainWeights
#       input(s):
#           - data (type - int[n][m]): n x m array where n = # of users and m = # of items
#           - activeUserData (type - int[3][m]): 3 x m array where m = # of items
#               - Column 1: userID
#               - Column 2: item ID
#               - Column 3: rating
#       output(s):
#           - weights (type - int[2][m]): 2 x m array where m = # of users
#           - itemsToPredict (type - int[n]): size n array where n = # of items to predict
# --------------------
def trainWeights(data, activeUserData):

    # List of items the active user as rated
    userItemList = [elt[1] for elt in activeUserData if elt[2] != 0]
    
    # List of active user's ratings
    userRatings = [elt[2] for elt in activeUserData if elt[2] != 0]
    
    # List of items to predict
    itemsToPredict = [elt[1] for elt in activeUserData if elt[2] == 0]
    
    weights = []
    num = 0
    
    # For each user in the data
    for user in data:
        inactiveRatings = []
        activeRatings = []
        num += 1    # Keep track of userID number
        itemNum = 0 # Keep track of item # in userRatings
        
        # For each item the user has rated
        for item in userItemList:
        
            # If the inactive user has rated the item
            if (user[item - 1] != 0):
                inactiveRatings.append(user[item - 1])
                activeRatings.append(userRatings[itemNum])
            itemNum += 1
        
        # If the # of items in common we found is greater than 0
        if len(inactiveRatings) != 0:
            weight = cosSimilarity(inactiveRatings, activeRatings)
            weights.append([weight, num])
            
    return weights, itemsToPredict
