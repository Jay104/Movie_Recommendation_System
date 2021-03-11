import math

# --------------------
#   function: cosSimilarity
#       input(s):
#           - v1 (type - int[n]): size n array where n = # of rated movies in common
#           - v2 (type - int[n]): size n array where n = # of rated movies in common
#       output(s):
#           - cos(v1, v2) (type - float): The cosine similarity of vectors v1 & v2. Range: [-1, 1]
# --------------------
def cosSimilarity(v1, v2):
    numerator = 0.0
    magnitude1 = 0.0
    magnitude2 = 0.0
    
    # For each element in the vectors
    for i in range(len(v1)):
        numerator += v1[i] * v2[i]
        magnitude1 += v1[i]**2
        magnitude2 += v2[i]**2
    magnitude1 = math.sqrt(magnitude1)
    magnitude2 = math.sqrt(magnitude2)
    denominator = magnitude1 * magnitude2
    
    return numerator / denominator

def calcAverages(data):
    averages = []
    for user in data:
        average = 0.0
        count = 0
        for elt in user:
            if elt != 0:
                average += elt
                count += 1
        average /= count
        average += 0.001    # Form of add-one smoothing
        averages.append(average)
    return averages
