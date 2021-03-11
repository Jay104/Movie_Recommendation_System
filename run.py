from fileHandling import *
from basicUBCF import performUBCF
from pearsonUBCF import performPearson
from basicIBCF import performIBCF
from customAlg import performCustom
import math


print("Which recommendation method would you like to use? (Pick a number):")
print("1. User-Based Collaborative Filtering w/ Cosine Similarity")
print("2. User-Based Collaborative Filtering w/ Pearson Correlation")
print("3. Item-Based Collaborative Filtering w/ Adjusted Cosine Similarity")
print("4. My Custom Algorithm")
whichMethod = input()

print("Which file would you like to test on? (Pick a number):")
print("1. test5.txt")
print("2. test10.txt")
print("3. test20.txt")
whichFile = input()
    
# Ask user which method they want to use
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
elif whichMethod == '3':
    print("Using IBCF w/ Adjusted Cosine Similarity")
else:
    print("Using Custom Algorithm")
    print("Do you want to make other improvements for prediction? (Pick a number):")
    print("1. Both Inverse User Frequency and Case Amplification")
    print("2. Only Inverse User Frequency")
    print("3. Only Case Amplification")
    print("4. None")
    whichImprov = input()

# Select which files to read from/write to
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

# Run algorithm based on user's choice
if whichMethod == '1':
    predictions = performUBCF(trainData, testData)
elif whichMethod == '2':
    predictions = performPearson(trainData, testData, whichImprov)
elif whichMethod == '3':
    predictions = performIBCF(trainData, testData)
else:
    predictions = performCustom(trainData, testData, whichImprov)

#print(predictions)
writeToFile(predictions, resultFilename)
