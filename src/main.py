import time
import platform

import plot as plot
import functions as func
import algorithms as algorithm

if __name__ == '__main__':
    # GLOBAL VARIABLE
    closestPair = []
    closestDistance = 0
    count = 0
    points = []
    
    # START MENU
    print('CLOSEST PAIR OF RANDOM POINTS IN 3D (AND MORE) SPACE')
    print('============================================================')

    # INPUT POINTS
    func.inputPoint(points)

    # DIVIDE AND CONQUER
    print('============================================================')
    print("DIVIDE AND CONQUER")
    print("------------------")
    start_dnc = time.time()
    func.sort(points, 'x0')
    closestDistance, closestPair, count = algorithm.divideConquer(points, count)
    end_dnc = time.time()
    print("Shortest Distance                = " + str(closestDistance))
    print("Euclidean Distance Calculated    = " + str(count))
    print("Time taken                       = {:.2f} ms".format((end_dnc - start_dnc) * 1000))
    print("Closest Pair(s)")
    func.printPairs(closestPair)
    plot.plot(points, closestPair)

    _ = input('Press Enter to continue and see Brute Force Algorithm')

    # BRUTE FORCE
    print('============================================================')
    print("BRUTE FORCE")
    print("-----------")
    closestPair = []
    closestDistance = 0
    count = 0
    start_bf = time.time()
    closestDistance, closestPair, count = algorithm.bruteForce(points, count)
    end_bf = time.time()
    print("Shortest Distance                = " + str(closestDistance))
    print("Euclidean Distance Calculated    = " + str(count))
    print("Time taken                       = {:.2f} ms".format((end_bf - start_bf) * 1000))
    print("Closest Pair(s)")
    func.printPairs(closestPair)
    plot.plot(points, closestPair)
    print('============================================================')
    print('Device used: ' + platform.processor())