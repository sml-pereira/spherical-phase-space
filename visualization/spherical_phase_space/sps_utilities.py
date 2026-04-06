# notas iniciais

def points_sphere(r, total):
    points_sphere = []
    for i in range(total):
        lon = map(i, 0, total, 0, TWO_PI)
        for j in range(total):
            points_sphere.append([])
            lat = map(j, 0, total, 0, PI)
            x = r * sin(lat) * cos(lon)
            y = r * sin(lat) * sin(lon)
            z = r * cos(lat)
            points_sphere[-1].append(x)
            points_sphere[-1].append(y)
            points_sphere[-1].append(z)
    return points_sphere


def points_rads(file_name):
    # 
    point_rads = []
    # open file and read the content in a list
    with open(file_name, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]
            # add item to the list
            point_rads.append(currentPlace)
    #
    for i in range(len(point_rads)):
        point_rads[i] = point_rads[i].split(", ")
        for j in range(2):
            if j == 0:
                point_rads[i][j] = point_rads[i][j].replace("[", "")
            elif j == 1:
                point_rads[i][j] = point_rads[i][j].replace("]", "")
            point_rads[i][j] = float(point_rads[i][j])
    return point_rads


def points_cartesian(r, points_rads):
    points_rads_scaled = []
    points_cartesian = []
    for i in range(len(points_rads)):
        points_rads_scaled.append([])
        points_cartesian.append([])
        for j in range(2):
            if j == 0:
                points_rads_scaled[i].append(map(points_rads[i][j], -PI, PI, 0, TWO_PI))
            elif j == 1:
                points_rads_scaled[i].append(map(points_rads[i][j], -PI, PI, 0, PI))
        for k in range(3):
            if k == 0:
                points_cartesian[i].append(int(r * sin(points_rads_scaled[i][1]) * cos(points_rads_scaled[i][0])))
            elif k == 1:
                points_cartesian[i].append(int(r * sin(points_rads_scaled[i][1]) * sin(points_rads_scaled[i][0])))
            elif k == 2:
                points_cartesian[i].append(int(r * cos(points_rads_scaled[i][1])))
    return points_cartesian


def cluster_center(file_name):
    # 
    cluster_center = []
    # open file and read the content in a list
    with open(file_name, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]
            # add item to the list
            cluster_center.append(currentPlace)
    
    for i in range(len(cluster_center)):
        cluster_center[i] = cluster_center[i].split(", ")
        for j in range(3):
            if j == 0:
                cluster_center[i][j] = cluster_center[i][j].replace("[", "")
            elif j == 2:
                cluster_center[i][j] = cluster_center[i][j].replace("]", "")
            cluster_center[i][j] = float(cluster_center[i][j])
            cluster_center[i][j] = int(cluster_center[i][j])
    return cluster_center


def labels_reader(file_name):
    # 
    cluster_center = []
    # open file and read the content in a list
    with open(file_name, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]
            # add item to the list
            cluster_center.append(currentPlace)
    #        
    for i in range(len(cluster_center)):
        cluster_center[i] = int(cluster_center[i])
    return cluster_center


def color_generator():
    # set 5 different colors to represent each chord cluster
    color_list = [[56, 0, 60], [233, 0, 82], [4, 245, 255], [0, 255, 133], [240, 232, 7]]
    return color_list
