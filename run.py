from fileHandling import *
from basicUBCF import *
from pearsonUBCF import *

# Get the train data set
trainData = readData("train.txt")

# Get the test dataset
filename = "test20.txt"
testData = readData(filename)

# Variables to set up loop
start = 0
end = 0
userID = testData[start][0]
i = 0
size = len(testData)
allPredictions = []

# Begin to iterate through the training data
while start < size:

    # Find the range of indeces for 'userID'
    while (i < size) and (userID == testData[i][0]):
        i += 1
    end = i

    # Create slice of data to pass to function
    section = slice(start, end)
    weights, itemsToPredict = trainBasicWeights(trainData, testData[section])

    
    # Sort list such that the highest weights (biggest similarity) are first
    weights.sort(reverse=True)
    predictions = predictBasicUBCF(userID,
                                   trainData,
                                   weights,
                                   itemsToPredict)
    
    # Get the next userID
    if (i < size):
        userID = testData[i][0]
    start = end

    allPredictions += predictions
    
# Save predictions in a file
writeToFile(allPredictions)

