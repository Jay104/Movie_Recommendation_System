import os

# -------------------------
# Function: readData
#   input: string - name of file to extract data from
#       - file must be in the 'trainTestData' folder
#   output: m x n, 2-D array of integers where m = # of users & n = # of movies
# -------------------------
def readData(filename):
    data = []
    thisDir = os.path.dirname(os.path.realpath(__file__))
    my_file = os.path.join(thisDir, ("trainTestData/" + filename))
    with open(my_file, "r") as fp:
        for line in fp:
            stringData = line.strip("\n").split()
            intData = []
            for elt in stringData:
                intData.append(int(elt))
            data.append(intData)
    return data

# -------------------------
# Function: writeToFile
#   input:
#   output:
# -------------------------
def writeToFile(data):
    #print(data)
    f = open("result20.txt", "w")
    
    rows = len(data)
    columns = len(data[0])
    
    for i in range(rows):
        for j in range(columns):
            f.write(str(data[i][j]))
            if j != (columns - 1):
                f.write(' ')
        if i != (rows - 1):
            f.write('\n')
    f.close()



