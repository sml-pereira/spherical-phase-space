import kmeans_utilities as kmu
from sklearn.cluster import KMeans


def main():

    r = 700
    file_name = "phases_skk_III_4_5.txt"
    clusters_number = 3

    kmu.set_directory()

    point_rads = kmu.point_rads(file_name)
    #print(point_rads)

    points_cartesian = kmu.points_cartesian(point_rads, r)
    #print(points_cartesian)


    X = kmu.points_cartesian_array(points_cartesian)
    #print(X)

    # to determine the optimal number of k
    sum_squared_distances = []
    K = range(1,7)
    for k in K:
        km = KMeans(n_clusters=k)
        km = km.fit(X)
        sum_squared_distances.append(km.inertia_)


    # Initializing KMeans
    kmeans = KMeans(n_clusters = clusters_number)
    # Fitting with inputs
    kmeans = kmeans.fit(X)
    # Predicting the clusters
    labels = kmeans.predict(X)
    # Getting the cluster centers
    C = kmeans.cluster_centers_
    #print(C)
    #print(labels)

    #kmu.cluster_center_exporter(C, "III")
    #kmu.labels_exporter(labels, "III")

    kmu.plot_optimal_k(K, sum_squared_distances)
    kmu.plot_graph(X, C)
    
    

if __name__ == "__main__":
    main()