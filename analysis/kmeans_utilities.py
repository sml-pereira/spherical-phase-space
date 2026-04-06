import os
import pathlib
import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def set_directory():
    os.chdir(pathlib.Path(__file__).parent.absolute())

def point_rads(file_name):
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



def points_cartesian(point_rads, r):
    points_rads_scaled = []
    points_cartesian = []
    for i in range(len(point_rads)):
        points_rads_scaled.append([])
        points_cartesian.append([])
        for j in range(2):
            # to define a range between 0 and 2*PI
            if j == 0:
                points_rads_scaled[i].append(point_rads[i][j] + math.pi)
            # to define a range between 0 and PI
            elif j == 1:
                points_rads_scaled[i].append((point_rads[i][j] + math.pi)/2)
        for k in range(3):
            if k == 0:
                points_cartesian[i].append(int(r * math.sin(points_rads_scaled[i][1]) * math.cos(points_rads_scaled[i][0])))
            elif k == 1:
                points_cartesian[i].append(int(r * math.sin(points_rads_scaled[i][1]) * math.sin(points_rads_scaled[i][0])))
            elif k == 2:
                points_cartesian[i].append(int(r * math.cos(points_rads_scaled[i][1])))
    return points_cartesian


def points_cartesian_array(points_cartesian):
    X = np.array(points_cartesian)
    return X


def cluster_center_exporter(cluster_list, movement):
    new_list = []
    for i in range(len(cluster_list)):
        new_list.append([])
        for j in range(3):
            new_list[i].append(cluster_list[i][j])
    with open("cluster_center_" + str(movement) + "_movement" + ".txt", 'w') as filehandle:
        for listitem in new_list:
            filehandle.write('%s\n' % listitem)


def labels_exporter(labels_list, movement):
    with open("labels_" + str(movement) + "_movement" + ".txt", 'w') as filehandle:
        for listitem in labels_list:
            filehandle.write('%s\n' % listitem)


def plot_optimal_k(K, sum_squared_distances):
    plt.plot(K, sum_squared_distances, 'bx-')
    plt.xlabel('k')
    plt.ylabel('Sum_of_squared_distances')
    plt.title('Elbow Method For Optimal k')
    plt.show()


def plot_graph(X, C):
    plt.rcParams['figure.figsize'] = (16, 9)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter(X[:, 0], X[:, 1], X[:, 2])
    ax.scatter(C[:, 0], C[:, 1], C[:, 2], marker='*', c='#050505', s=1000)
    plt.show()