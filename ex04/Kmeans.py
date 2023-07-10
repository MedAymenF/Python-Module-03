#!/usr/bin/env python3
import argparse
import numpy as np


class CsvReader():
    def __init__(self, filename=None, sep=',',
                 header=False, skip_top=0, skip_bottom=0):
        self.get_header = header
        self.missing = False
        self.corrupted = False
        self.data = []
        try:
            self.file = open(filename)
        except FileNotFoundError:
            self.missing = True
        else:
            n_columns = None
            if self.get_header:
                self.header = self.file.readline().rstrip().split(sep)
                n_columns = len(self.header)
            for i in range(skip_top):
                self.file.readline()
            while True:
                line = self.file.readline().rstrip()
                if not line:
                    break
                split_line = line.split(sep)
                if '' in split_line:
                    self.corrupted = True
                    break
                length = len(split_line)
                if (n_columns and n_columns != length):
                    self.corrupted = True
                    break
                n_columns = length
                self.data.append(split_line)
            if not self.corrupted and skip_bottom:
                self.data = self.data[:-skip_bottom]

    def __enter__(self):
        if self.missing or self.corrupted:
            return None
        return self

    def __exit__(self, type, value, traceback):
        if not self.missing:
            self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip_bottom.
Returns:
nested list (list(list, list, ...)) representing the data."""
        return self.data

    def getheader(self):
        """ Retrieves the header from csv file.
Returns:
list: representing the data (when self.get_header is True).
None: (when self.get_header is False)."""
        if self.get_header:
            return self.header
        else:
            return None


class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=4):
        if not isinstance(max_iter, int) or not isinstance(ncentroid, int)\
                or max_iter <= 0 or ncentroid < 1:
            raise ValueError
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []

    def find_closest_centroid(self, X):
        distances = []
        for centroid in self.centroids:
            distance = abs(X - centroid).sum(axis=1)
            distance = distance.reshape((-1, 1))
            distances.append(distance)
        distances = np.hstack(distances)
        closest_centroid = distances.argmin(axis=1)
        return closest_centroid

    def fit(self, X):
        """Run the K-means clustering algorithm.
For the location of the initial centroids,\
 random pick ncentroids from the dataset.
Args:
X: has to be an numpy.ndarray, a matrice of dimension m * n.
Returns:
None.
Raises:
This function should not raise any Exception."""
        if not isinstance(X, np.ndarray):
            return None
        n = X.shape[0]
        if self.ncentroid > n:
            self.trained = False
            return None
        index = np.random.choice(n, self.ncentroid, replace=False)
        self.centroids = X[index]
        for _ in range(self.max_iter):
            clusters = []
            # Assign each data point to its closest centroid using L1 distance
            closest_centroid = self.find_closest_centroid(X)
            for i in range(self.ncentroid):
                index = closest_centroid == i
                clusters.append(X[index])
            # Move each centroid to its cluster's average
            for i, cluster in enumerate(clusters):
                self.centroids[i] = cluster.mean(axis=0)
        self.clusters = clusters
        self.trained = True

    def predict(self, X):
        """Predict from wich cluster each datapoint belongs to.
Args:
X: has to be an numpy.ndarray, a matrice of dimension m * n.
Returns:
the prediction has a numpy.ndarray, a vector of dimension m * 1.
Raises:
This function should not raise any Exception."""
        if not isinstance(X, np.ndarray) or not self.trained:
            return None
        closest_centroid = self.find_closest_centroid(X)
        return closest_centroid


if __name__ == "__main__":
    # parse the arguments
    parser = argparse.ArgumentParser(
        description="Implementation of a basic Kmeans algorithm.")
    parser.add_argument('--filepath', type=str,
                        default='../resources/solar_system_census.csv')
    parser.add_argument('--ncentroid', type=int, default=4)
    parser.add_argument('--max_iter', type=int, default=30)
    args = parser.parse_args()

    # read the dataset
    with CsvReader(args.filepath, header=True) as file:
        header = file.getheader()
        data = file.getdata()
    data = np.array(data, dtype=float)
    data = data[:, 1:]

    # fit the dataset
    kmc = KmeansClustering(max_iter=args.max_iter, ncentroid=args.ncentroid)
    kmc.fit(data)

    # Sort centroids by height
    centroids = kmc.centroids
    index = centroids[:, 0].argsort()
    index = index[::-1]
    centroids = centroids[index]

    # display the coordinates of the different centroids
    # and the associated region (for the case ncentroid=4)
    # display the number of individuals associated to each centroid
    header[0] = 'Centroids'
    header.append('Number of individuals')
    for column in header:
        print(f'{column:30}', end='')
    print('')
    n = centroids.shape[0]
    if n == 4:
        areas = ['Asteroids’ Belt colonies', 'Mars Republic',
                 'The flying cities of Venus', 'United Nations of Earth']
    else:
        areas = [f'centroid_{i}:' for i in range(n)]
    for i, centroid in enumerate(centroids):
        row = areas[i]
        print(f'{row:30}', end='')
        for value in centroid:
            print(f'{value:<30.3f}', end='')
        print(kmc.clusters[i].shape[0])
    print('')

    prediction = kmc.predict(data)
    print(prediction)
