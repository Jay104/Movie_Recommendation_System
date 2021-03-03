from fileHandling import *
from basicUBCF import *
from pearsonUBCF import *


whichMethod = input("Which method would you like to use? (pick a number):\n1. basicUBCF\n2. pearsonUBCF\n")
whichFile = input("Which file to you want to test on? (pick a number):\n1. test5.txt\n2. test10.txt\n3. test20.txt\n")
    
if whichMethod == '1':
    print("Using basicUBCF")
else:
    print("Using pearsonUBCF")

if whichFile == '1':
    filename = "test5.txt"
    resultFilename = "result5.txt"
    print("Testing on test5.txt")
elif whichFile == '2':
    filename = "test10.txt"
    resultFilename = "result10.txt"
    print("Testing on test10.txt")
else:
    filename = "test20.txt"
    resultFilename = "result20.txt"
    print("Testing on test20.txt")

# Get the train data set
trainData = readData("train.txt")

# Get the test dataset
testData = readData(filename)

# Variables to set up loop
start = 0
end = 0
userID = testData[start][0]
i = 0
size = len(testData)
allPredictions = []

# Calculate average ratings of inactive users
averages = []
for user in trainData:
    average = 0.0
    count = 0
    for elt in user:
        if elt != 0:
            average += elt
            count += 1
    average /= count
    average += 0.001    # Form of add-one smoothing
    averages.append(average)

# Begin to iterate through the training data
while start < size:

    # Find the range of indeces for 'userID'
    while (i < size) and (userID == testData[i][0]):
        i += 1
    end = i

    # Create slice of data to pass to function
    section = slice(start, end)
    
    if whichMethod == 1:
        weights, itemsToPredict = trainBasicWeights(trainData, testData[section])
        
        # Sort list such that the highest weights (biggest similarity) are first
        weights.sort(reverse=True)
        predictions = predictBasicUBCF(userID,
                                       trainData,
                                       weights,
                                       itemsToPredict)
    
    else:
        weights, itemsToPredict, userAvg = trainPearsonWeights(trainData, testData[section], averages)

        # Sort list such that the highest weights (biggest similarity) are first
        weights.sort(reverse=True)
        predictions = predictPearsonUBCF(userID,
                                         trainData,
                                         weights,
                                         itemsToPredict,
                                         userAvg,
                                         averages)

    # Get the next userID
    if (i < size):
        userID = testData[i][0]
    start = end
    allPredictions += predictions


# Save predictions in a file
writeToFile(allPredictions, resultFilename)


