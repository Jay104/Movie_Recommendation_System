import math
from calcFunctions import *

def performCustom(trainData, testData, whichImprov):
    averages = calcAverages(trainData)
    IUFvals = []
    if whichImprov == '1' or whichImprov == '2':
        for i in range(len(trainData[0])):
            denominator = 0
            IUF = 0.0
            for j in range(len(trainData)):
                if trainData[j][i] != 0:
                    denominator += 1
            if denominator == 0:
                denominator += 0.01
            IUF = math.log(200/denominator)
            IUFvals.append(IUF)
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
        weights, itemsToPredict, userAvg = trainWeights(trainData, testData[section], averages, IUFvals)
        weights.sort(reverse=True)
        #print("--------------------")
        #print(weights)
        #print("--------------------")
        if whichImprov == '1' or whichImprov == '3':
            for j, weight in enumerate(weights):
                weights[j][0] = weight[0] * abs(weight[0])**(1.5)
        predictions = predict(userID, trainData, weights, itemsToPredict, userAvg, averages)
        if i < size:
            userID = testData[i][0]
        start = end
        allPredictions += predictions
    #print("-----")
    #print(allPredictions)
    #print("-----")
    return allPredictions

def trainWeights(data, activeUserData, averages, IUFvals):
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
    for count, score in enumerate(userRatings):
        userRatings[count] = userRatings[count] - userAvg
        
    weights = []
    
    # For each inactive user in data
    for count, user in enumerate(data):
        inactiveRatings = []
        activeRatings = []
        
        # For each item the active user has rated
        for itemCount, item in enumerate(userItemList):
        
            # If the inactive user has rated the item, include his/her rating
            if (user[item - 1] != 0):
                elt1 = (user[item - 1] - averages[count])
                elt2 = userRatings[itemCount]
                if len(IUFvals) != 0:
                    elt1 *= IUFvals[item - 1]
                    elt2 *= IUFvals[item - 1]
                inactiveRatings.append(elt1)
                activeRatings.append(elt2)
                
        # If the length of the list is greater than 0, compute cosine similarity
        # Changed the condition from len(inactiveRatings) != 0
        if len(inactiveRatings) > 1:
            weight = cosSimilarity(inactiveRatings, activeRatings)
            weights.append([weight, count + 1])
            
    return weights, itemsToPredict, userAvg

def predict(userID, data, weights, itemsToPredict, userAvg, averages):
    numerator = 0.0
    denominator = 0.0
    predictions = []
    kMAX = 10
    k = 0
    for item in itemsToPredict:
        for user in weights:
            #if (k > kMAX):
                #break
            if (data[user[1] - 1][item - 1] != 0):
                numerator += (user[0] * (data[user[1] - 1][item - 1] - averages[user[1] - 1]))
                denominator += abs(user[0])
            k += 1
        denominator += 0.001
        quotient = numerator / denominator
        quotient += userAvg
        quotient = round(quotient)
        if quotient > 5:
            quotient = 5
        if quotient == 0:
            quotient = 1
        predictions.append([userID, item, quotient])
        
    return predictions
