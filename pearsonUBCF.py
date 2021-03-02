import math
from calcFunctions import *

def trainPearsonWeights(data, activeUserData):
    
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
    
    for i in range(len(userRatings)):
        userRatings[i] = userRatings[i] - userAvg
    print(userRatings)
    
    weights = []
    num = 0
    allAverages = []
    

    
            
    return weights, itemsToPredict, userAvg

def sub(n, userAvg):
    return n - userAvg
