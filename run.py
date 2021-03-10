from fileHandling import *
from basicUBCF import performUBCF
from pearsonUBCF import performPearson
from basicIBCF import performIBCF
import math


print("Which recommendation method would you like to use? (Pick a number):")
print("1. User-Based Collaborative Filtering w/ Cosine Similarity")
print("2. User-Based Collaborative Filtering w/ Pearson Correlation")
print("3. Item-Based Collaborative Filtering w/ Adjusted Cosine Similarity")
whichMethod = input()

print("Which file would you like to test on? (Pick a number):")
print("1. test5.txt")
print("2. test10.txt")
print("3. test20.txt")
whichFile = input()
    
whichImprov = '0'
if whichMethod == '1':
    print("Using UBCF w/ Cosine Similarity")
elif whichMethod == '2':
    print("Using UBCF w/ Pearson Correlation")
    print("Do you want to make other improvements for prediction? (Pick a number):")
    print("1. Both Inverse User Frequency and Case Amplification")
    print("2. Only Inverse User Frequency")
    print("3. Only Case Amplification")
    print("4. None")
    whichImprov = input()
else:
    print("Using IBCF w/ Adjusted Cosine Similarity")

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

if whichMethod == '1':
    predictions = performUBCF(trainData, testData)
elif whichMethod == '2':
    predictions = performPearson(trainData, testData, whichImprov)
elif whichMethod == '3':
    predictions = performIBCF(trainData, testData)

#print(predictions)
writeToFile(predictions, filename)


'''
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
    
    if whichMethod == '1':
        predictions = performUBCF(trainData, testData[section], userID)
    elif whichMethod == '2':
        predictions = performPearson(trainData, testData[section], userID, averages, IUFvals, whichImprov)
    elif whichMethod == '3':
        predictions = performIBCF(trainData, testData[section], userID, averages)

    # Get the next userID
    if (i < size):
        userID = testData[i][0]
    start = end
    allPredictions += predictions

# Save predictions in a file
writeToFile(allPredictions, resultFilename)
'''
