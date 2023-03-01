import math
import random

# CALCULATE EUCLIDEAN DISTANCE BETWEEN TWO POINTS
def distance(p1, p2, count):
    count += 1
    dist = 0
    for i in range(len(p1)):
        dist += (p2['x' + str(i)] - p1['x' + str(i)])**2
    return math.sqrt(dist), count

# SORT POINTS BY (AXIS)
def sort(points, axis):
    points.sort(key=lambda x: x[axis])

def printPairs(pairs):
    for i in range (len(pairs)):
        print(i + 1, end = '. ')
        for j in range (2):
            for k in range(len(pairs[i][0]) - 1):
                if k == 0:
                    print("({:.2f}, ".format(pairs[i][j]['x' + str(k)]), end = '')
                else:
                    print("{:.2f}, ".format(pairs[i][j]['x' + str(k)]), end = '')
            
            if j == 0:
                print("{:.2f})".format(pairs[i][j]['x' + str(len(pairs[i][0]) - 1)]), end = ' and ')
            else:
                print("{:.2f})".format(pairs[i][j]['x' + str(len(pairs[i][0]) - 1)]))

# INPUT POINTS
def inputPoint(points):
    flag = False

    # INPUT AMOUNT OF POINTS
    while(not flag):
        try:
            p = int(input("Input amount of point(s): "))
            if p < 2:
                print("Invalid input! (Please input integer more than 1")
            else:
                flag = True
        except ValueError:
            print("ERROR! (Input must be an integer and more than 1)")
 
    # INPUT DIMENSIONAL SPACE
    flag = False
    while(not flag):
        try:
            d = int(input("Input dimensional space: "))
            if d < 1:
                print("Invalid input! (Please input integer more than 1)")
            else:
                flag = True
        except ValueError:
            print("ERROR! (Input must be integer and more than 1)")

    # GENERATE RANDOM COORDINATES
    while(len(points) < p):
        coordinate = {}
        for i in range(d):
            coordinate['x' + str(i)] = random.uniform(-1000,1000)
        if coordinate not in points:
            points.append(coordinate)

    return points