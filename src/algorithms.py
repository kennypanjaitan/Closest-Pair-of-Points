import functions as func
# BRUTE FORCE ALGORITHM
def bruteForce(points, count):
    
    tempClosestPair = [[points[0], points[1]]]
    min_distance, count = func.distance(points[0], points[1], count)

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            if not (i == 0 and j == 1):
                temp_distance, count = func.distance(points[i], points[j], count)

                if temp_distance < min_distance:
                    min_distance = temp_distance
                    tempClosestPair = [[points[i], points[j]]]
                elif temp_distance == min_distance:
                    if ([points[i], points[j]] not in tempClosestPair) and ([points[j], points[i]] not in tempClosestPair):
                        tempClosestPair.append([points[i], points[j]])
                    
    return min_distance, tempClosestPair, count

# DIVIDE AND CONQUER ALGORITHM
def divideConquer(points, count):
    tempClosestPair = []

    # BASE
    if len(points) == 2:
        min_distance, count = func.distance(points[0], points[1], count)
        tempClosestPair = [[points[0], points[1]]]
        return min_distance, tempClosestPair, count
    
    elif len(points) == 3:
        return bruteForce(points, count)
    
    # DIVIDE
    mid = len(points)//2
    left = points[:mid]
    right = points[mid:]
    
    # RECURSIVE
    min_left, pair_left, count = divideConquer(left, count)
    min_right, pair_right, count = divideConquer(right, count)

    if min_left == min_right:
        tempClosestPair = pair_right + pair_left
        min_distance = min_left
    else:
        tempClosestPair = pair_left if min_left < min_right else pair_right
        min_distance = min_left if min_left < min_right else min_right

    mid_line = points[mid]['x0']
    strip = []
    for i in range(len(points)):
        if abs(points[i]['x0'] - mid_line) < min_distance:
            strip.append(points[i])
    if len(points[0]) != 1:
        func.sort(strip, 'x1')

    # CONQUER
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            for k in range(len(strip[i])):
                if abs(strip[j]['x' + str(k)] - strip[i]['x' + str(k)]) < min_distance:
                    dis_temp, count = func.distance(strip[i], strip[j], count)
                    if dis_temp < min_distance:
                        min_distance = dis_temp
                        tempClosestPair = [[strip[i], strip[j]]]
                        
                    elif dis_temp == min_distance:
                        if ([strip[i], strip[j]] not in tempClosestPair) and ([strip[j], strip[i]] not in tempClosestPair):
                            tempClosestPair.append([strip[i], strip[j]])
            
    return min_distance, tempClosestPair, count