from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

from load_dataset import load_datasets
from plot_function import PlotFunction

import numpy as np


def main():

    datasets = load_datasets(3)
    k_max = 500

    # For plots
    plot = PlotFunction()
    x_plot = []
    y_plot = []

    for d in range(0, len(datasets)):

        text_data = datasets[d]
        vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 1))
        x = vectorizer.fit_transform(text_data)
        print("Dataset: {0}, n_samples: {1}, n_features: {2}".format(d + 1, x.shape[0], x.shape[1]))

        for k in range(1, k_max + 1):

            km = KMeans(n_clusters=k, init='k-means++', max_iter=1000, n_init=1, n_jobs=-1)
            km.fit(x)

            x_plot.append(k)
            y_plot.append(km.inertia_)

            print("\tK =", k, "\tCost =", km.inertia_)

        # np.savetxt("k2.txt", x_plot)
        np.savetxt("cost_" + str(d + 1) + ".txt", y_plot)

        plot.add_function(x_plot.copy(), y_plot.copy())
        x_plot = y_plot = []

    # plota os resultados para cada K
    plot.show()


if __name__ == '__main__':
    main()
