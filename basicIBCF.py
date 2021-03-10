import math
from calcFunctions import *

def performIBCF(trainData, testData):

    # Calculate the average rating of each user
    averages = []
    for user in trainData:
        average = 0.0
        count = 0
        for elt in user:
            if elt != 0:
                average += elt
                count += 1
        average /= count
        average += 0.001
        averages.append(average)
        
    start = 0
    end = 0
    userID = testData[start][0]
    i = 0
    size = len(testData)
    allPredictions = []
    while start < size:
        while (i < size) and (userID == testData[i][0]):
            i += 1
        end = i
        section = slice(start, end)
        predictions = predict(trainData, testData[section], averages)

        if i < size:
            userID = testData[i][0]
        start = end
        allPredictions += predictions
    
    return allPredictions



def trainWeights(itemID, trainData, activeUserData, averages):

    userItemList = [elt[1] for elt in activeUserData if elt[2] != 0]
    #print("----- Active User Data")
    #print(activeUserData)
    #print("----- User Item List -----")
    #print(userItemList)
    weights = []
    for itemCount, item in enumerate(userItemList):
        iRatings = []
        jRatings = []
        
        
        
        for userCount, user in enumerate(trainData):
            if user[item - 1] != 0 and user[itemID - 1] != 0:
                iRatings.append(user[itemID - 1] - averages[userCount])
                jRatings.append(user[item - 1] - averages[userCount])
        if len(iRatings) != 0:
            weight = cosSimilarity(iRatings, jRatings)
            weights.append([weight, item])
        else:
            weights.append([0.0, item])
            
    return  weights
                


                
def predict(trainData, activeUserData, averages):
    
    # List of items to predict
    itemsToPredict = [elt[1] for elt in activeUserData if elt[2] == 0]
    # List of items the user has
    userRatings = [elt[2] for elt in activeUserData if elt[2] != 0]
    ratedItems = [elt[1] for elt in activeUserData if elt[2] != 0]

    #print("----- Items to Predict -----")
    #print(itemsToPredict)
    #print("----- Rated Items -----")
    #print(ratedItems)
    #print("----- User Ratings -----")
    #print(userRatings)
    
    
    predictions = []
    
    for count, item in enumerate(itemsToPredict):
        weights = trainWeights(item, trainData, activeUserData, averages)
        weightedItems = [elt[1] for elt in weights]
        #print("----- weights -----")
        #print(weights)
        numerator = 0.0
        denominator = 0.0
        for count2, weight in enumerate(weights):
            numerator += weight[0] * userRatings[count2]
            denominator += weight[0]
        denominator += 0.001
        result = round(numerator/denominator)
        
        predictions.append([activeUserData[0][0], item, result])

    return predictions

