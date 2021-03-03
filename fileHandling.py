import os

# -------------------------
#   function: readData
#       input(s):
#           - filename (type - string): name of the file to read data from
#       output(s):
#           - data (type - int[n][m]): n x m integer array of the data
# -------------------------
def readData(filename):
    data = []
    thisDir = os.path.dirname(os.path.realpath(__file__))
    my_file = os.path.join(thisDir, ("trainTestData/" + filename))
    
    # Open file
    with open(my_file, "r") as fp:
    
        # For each line in the file
        for line in fp:
            
            # Remove whitespace & newlines
            stringData = line.strip("\n").split()
            intData = []
            
            # Convert strings to integers
            for elt in stringData:
                intData.append(int(elt))
            data.append(intData)
    return data

# -------------------------
#   function: writeToFile
#       input(s):
#           - data (type - int[n][m]): n x m array of data to be written to file
#       output(s):
#           - none
# -------------------------
def writeToFile(data, filename):
    f = open(filename, "w")
    rows = len(data)
    columns = len(data[0])
    
    for i in range(rows):
        for j in range(columns):
            # Convert integers to strings
            f.write(str(data[i][j]))
            
            # Do not add a space at the end of a line
            if j != (columns - 1):
                f.write(' ')

        # Do not add a newline character at the end of the file
        if i != (rows - 1):
            f.write('\n')
    f.close()



