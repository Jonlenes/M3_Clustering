from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD, PCA
from sklearn.cluster import KMeans

from load_dataset import load_datasets, load_base_dataset, load_changed_dataset, path_dataset
from plot_function import PlotFunction
from time import time
from sklearn.metrics import silhouette_score
from sklearn.manifold import MDS

from sklearn.preprocessing import scale
from sklearn.metrics.pairwise import cosine_similarity, paired_cosine_distances

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
import os


def main():


    x_plot = []
    y_plot = []
    silhouette = []

    k_min = 2
    k_max = 20
    step = 1

    grams = [(1, 1), (2, 2), (3, 3), (4, 4)]
    min_dfs = [5, 4, 3, 2]

    count_dataset = 15
    id_test = 3

    datasets = load_datasets(count_dataset)

    # Percorrendo os datasets por ano
    for id_dataset in range(0, count_dataset):
        # Testando diferentes grams
        for i in [3]:
            text_data =datasets[id_dataset]

            gram = grams[i]
            vectorizer = TfidfVectorizer(stop_words='english', ngram_range=gram, token_pattern=r"(?u)\b\w\w\w+\b",
                                         max_df=.5, min_df=min_dfs[i], max_features=1000)
            x = vectorizer.fit_transform(text_data)
            print("n_samples: {0}, n_features: {1}, n-gram: {2}".format(x.shape[0], x.shape[1], gram))
            # print(vectorizer.get_feature_names())

            # Numero de clusters
            for k in range(k_min, k_max + 1, step):
                t = time()
                km = KMeans(n_clusters=k, init='k-means++', max_iter=1000, n_init=1, n_jobs=-1)
                cluster_labels = km.fit_predict(x)

                x_plot.append(k)
                y_plot.append(km.inertia_)
                print("\tK =", k, "\tCost =", km.inertia_, "Time =", time() - t)

                try:
                    silhouette_avg = silhouette_score(x, cluster_labels, sample_size=3000)
                except Exception:
                    silhouette_avg = 0

                silhouette.append(silhouette_avg)
                print("\tFor n_clusters =", k, "Average silhouette_score:", silhouette_avg)
                print()

                '''' Add View '''
                new_x = PCA(n_components=2).fit_transform(x.toarray())
                plt.scatter(new_x[:, 0], new_x[:, 1], c=cluster_labels.ravel(), s=3, cmap='viridis')


                # centers = km.cluster_centers_
                # plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.4)
                plt.savefig(str(id_dataset) + "_" + str(k) + ".png")
                new_x = []
                # plt.show()
                plt.clf()
                plt.cla()
                plt.close()


            np.savetxt("dataset" + str(id_dataset) + "_" + str(id_test) + "_k_" + str(i) + ".txt", x_plot)
            np.savetxt("dataset" + str(id_dataset) + "_" + str(id_test) + "_cost_" + str(i) + ".txt", y_plot)
            np.savetxt("dataset" + str(id_dataset) + "_" + str(id_test) + "_silhouette_" + str(i) + ".txt", silhouette)

            x_plot.clear()
            y_plot.clear()
            silhouette.clear()


if __name__ == '__main__':
    main()
