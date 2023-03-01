import matplotlib.pyplot as plt

def plot(points, closestPair):
    # INITIALIZE ARRAYS
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    x6 = []
    x_line = []
    y_line = []
    z_line = []

    # SEPARATE POINTS INTO ARRAYS OF EACH DIMENSION
    for i in range(len(points)):
        if len(points[i]) >= 1:
            x1.append(points[i]['x0'])
        if len(points[i]) >= 2:
            x2.append(points[i]['x1'])
        if len(points[i]) >= 3:  
            x3.append(points[i]['x2'])
        if len(points[i]) >= 4:
            x4.append(points[i]['x3'])
        if len(points[i]) >= 5:
            x5.append(points[i]['x4'])
        if len(points[i]) >= 6:
            x6.append(points[i]['x5'] * 1/10)
    
    # PLOT
    fig = plt.figure()
    if len(points[0]) <= 2:

        # 1 DIMENSION
        if len(points[0]) == 1:
            plt.scatter(x1, [0]*len(x1), color='black', alpha = 1)
            for i in range(len(closestPair)):
                plt.scatter(closestPair[i][0]['x0'], 0, color='red')
                plt.scatter(closestPair[i][1]['x0'], 0, color='red')
                x_line.append([closestPair[i][0]['x0'], closestPair[i][1]['x0']])
                y_line.append([0, 0])
        
        # 2 DIMENSIONS
        elif len(points[0]) == 2:
            plt.scatter(x1, x2, color='black', alpha = 1)
            for i in range(len(closestPair)):
                plt.scatter(closestPair[i][0]['x0'], closestPair[i][0]['x1'], color='red')
                plt.scatter(closestPair[i][1]['x0'], closestPair[i][1]['x1'], color='red')
                x_line.append([closestPair[i][0]['x0'], closestPair[i][1]['x0']])
                y_line.append([closestPair[i][0]['x1'], closestPair[i][1]['x1']])

        # PLOT LINES
        for i in range(len(x_line)):
            plt.plot(x_line[i], y_line[i])
        plt.show()

    elif len(points[0]) <= 6:
        space = fig.add_subplot(111, projection='3d')
       
        # 3 DIMENSIONS
        if len(points[0]) == 3:
              space.scatter(x1, x2, x3, color='black', alpha = 0.5)
              for i in range(len(closestPair)):
                space.scatter(closestPair[i][0]['x0'], closestPair[i][0]['x1'], closestPair[i][0]['x2'], color='red')
                space.scatter(closestPair[i][1]['x0'], closestPair[i][1]['x1'], closestPair[i][1]['x2'], color='red')
        
        # 4 DIMENSIONS
        elif len(points[0]) == 4:
            img = space.scatter(x1, x2, x3, c=x4, cmap=plt.hot(), alpha = 1)
            fig.colorbar(img)
        
        # 5 DIMENSIONS
        elif len(points[0]) == 5:
            img = space.scatter(x1, x2, x3, c=x4, cmap=plt.hot(), s = x5, alpha = 1)
            fig.colorbar(img)

        # 6 DIMENSIONS
        elif len(points[0]) == 6:
            img = space.scatter(x1, x2, x3, c=x4, cmap=plt.hot(), s = x5, alpha = x6)
            fig.colorbar(img)

        # PLOT LINES
        for i in range(len(closestPair)):
            x_line.append([closestPair[i][0]['x0'], closestPair[i][1]['x0']])
            y_line.append([closestPair[i][0]['x1'], closestPair[i][1]['x1']])
            z_line.append([closestPair[i][0]['x2'], closestPair[i][1]['x2']])
            space.plot(x_line[i], y_line[i], z_line[i])
        
        space.set_xlabel('X Label')
        space.set_ylabel('Y Label')
        space.set_zlabel('Z Label')
        plt.show()
    
    else:
        print("Too many dimensions to plot!")