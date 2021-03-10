from fileHandling import *

whichMethod = '3'
trainData = readData("train.txt")
print("Before transpose")
print(len(trainData))
print(len(trainData[0]))
if whichMethod == '3':
    trainData = [[trainData[j][i] for j in range(len(trainData))] for i in range(len(trainData[0]))]
print("After transpose")
print(len(trainData))
print(len(trainData[0]))


testData = readData("test5.txt")
