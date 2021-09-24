import inspect
import sys
from collections import Counter
import math
from time import time
"""
Raise a "not defined" exception as a reminder
"""


def _raise_not_defined():
    print("Method not implemented: %s" % inspect.stack()[1][3])
    sys.exit(1)


"""
Extract 'basic' features, i.e., whether a pixel is background or
forground (part of the digit)
"""


def extract_basic_features(digit_data, width, height):
    features = []
    for i in range(width):
        for j in range(height):
            if digit_data[i][j] == 1 or digit_data[i][j] == 2:
                features.append(1)
            else:
                features.append(0)
    return features


"""
Extract advanced features that you will come up with
"""


def extract_advanced_features(digit_data, width, height):

    features = []
    foundU = False
    foundD = False
    upperConnectAt = []
    lowerConnectAt = []
    noOfLoops = 0
    upperConnect = False
    lowerConnect = False
    for i in range(width):
        for j in range(height):
            if j < width - 1:
                if digit_data[i][j] != 0:
                    if digit_data[i][j + 1] == 0:
                        for k in range(j+1, width):
                            if digit_data[i-1][k] == 0:
                                break
                            for n in range(i+1, height):
                                if digit_data[n][k] == 1 or digit_data[n][k] == 2:

                                    foundD = True
                                    break
                            if foundD == False:
                                break
                            if foundD:
                                foundD = False
                            # if digit_data[i+1][k] == 1 or digit_data[i+1][k] == 2:
                            #     break
                            if digit_data[i][k] == 1 or digit_data[i][k] == 2:
                                if k == j+2:
                                    if digit_data[i+1][k-1] == 1 or digit_data[i+1][k-1] == 2:

                                        break
                                upperConnectAt.append((i, j))
                                upperConnectAt.append((i, k))
                                upperConnect = True
                                break

                        for l in range(j+1, width):
                            if i < height - 1:
                                if digit_data[i+1][l] == 0:
                                    break
                            for m in range(i-1, 0, -1):
                                if digit_data[m][l] == 1 or digit_data[m][l] == 2:

                                    foundU = True
                                    break
                            if foundU == False:
                                break
                            if foundU:

                                foundU = False
                            # if digit_data[i-1][l] == 1 or digit_data[i-1][l] == 2:
                            #     break
                            if digit_data[i][l] == 1 or digit_data[i][l] == 2:
                                if l == j+2:
                                    if digit_data[i-1][l-1] == 1 or digit_data[i-1][l-1] == 2:
                                        break
                                lowerConnectAt.append((i, j))
                                lowerConnectAt.append((i, l))
                                lowerConnect = True
                                break
    ulp = 0
    llp = 0

    
    return noOfLoops
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here


"""
Extract the final features that you would like to use
"""


def extract_final_features(digit_data, width, height):

    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here
    _raise_not_defined()
    return features


"""
Compute the parameters including the prior and and all the P(x_i|y). Note
that the features to be used must be computed using the passed in method
feature_extractor, which takes in a single digit data along with the width
and height of the image. For example, the method extract_basic_features
defined above is a function than be passed in as a feature_extractor
implementation.

The percentage parameter controls what percentage of the example data
should be used for training.
"""
computedStatistics = dict()
dict_label = dict()
labelList = dict()


def compute_statistics(data, label, width, height, feature_extractor, percentage=100.0, ):

    _raise_not_defined()
    global dict_label
    global labelList
    k = 1

    percentage = 100
    dict_label = Counter(label[:int(len(label)*percentage/100)])
    print(dict_label)
    for l in dict_label:

        dict_label[l] /= len(label)*percentage/100
        dict_label[l] = math.log(dict_label[l])

    dictLabel = dict()

    for i in range(int(len(label)*percentage / 100)):
        curLabel = label[i]
        curImg = data[i]
        curFeature = feature_extractor(curImg, width, height)
        if curLabel in dictLabel:
            dictLabel[curLabel].append(curFeature)
            continue
        dictLabel[curLabel] = [curFeature]
    noOfLoops = dict()
    for i in range(0, 10):
        noOfLoops[i] = 0

    for i in dictLabel:
        l = dictLabel[i]
        for j in l:
            if j > 0:
                noOfLoops[i] += 1
    print(noOfLoops)
    
"""
For the given features for a single digit image, compute the class
"""


def compute_class(features):
    _raise_not_defined()
    predicted = -1
    maxLabel = float('-inf')
    global dict_label
    global labelList
    for k in labelList:
        maxForThisLabel = 0
        maxForThisLabel += dict_label[k]
        l = labelList[k]

        for i in range(len(features)):

            if features[i] == 1:
                maxForThisLabel += math.log(l[i])
            if features[i] == 0:
                maxForThisLabel += math.log(1 - l[i])
        if maxForThisLabel > maxLabel:
            maxLabel = maxForThisLabel
            predicted = k
    return predicted


"""
Compute joint probablity for all the classes and make predictions for a list
of data
"""

computedStatistics = []


def classify(data, width, height, feature_extractor):
    _raise_not_defined()
    predicted = list()
    for i in range(len(data)):
        curFeature = feature_extractor(data[i], width, height)
        p = compute_class(curFeature)
        predicted.append(p)
    return predicted
