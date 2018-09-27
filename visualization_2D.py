import matplotlib.pyplot as plt
from sklearn.decomposition import TruncatedSVD
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.feature_extraction import text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from nltk.tokenize import RegexpTokenizer
from nltk.stem.snowball import SnowballStemmer
from load_dataset import path_dataset, load_datasets, load_datasets2
from string import punctuation
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.manifold import TSNE
from ggplot import *


def show_2d_view():
    """
    Realiza o plot do modelo
    """

    data = pd.read_csv(path_dataset + "news_headlines.csv", error_bad_lines=False, usecols=["headline_text"]).sample(frac=.1)
    data = data.drop_duplicates('headline_text')  # headline_text

    stop_words = text.ENGLISH_STOP_WORDS.union(list(punctuation))
    desc = data['headline_text'].values  # headline_text

    stemmer = SnowballStemmer('english')
    tokenizer = RegexpTokenizer(r'[a-zA-Z\']+')


    def tokenize(text):
        return [stemmer.stem(word) for word in tokenizer.tokenize(text.lower())]


    gram = (4, 4)
    ks = [5, 12]
    # c = ['red', 'green', 'blue', 'yellow', 'purple']

    vectorizer = TfidfVectorizer(stop_words=stop_words, tokenizer=tokenize, max_features=100, ngram_range=gram)
    x = vectorizer.fit_transform(desc)
    print("n_samples: {0}, n_features: {1}, n-gram: {2}".format(x.shape[0], x.shape[1], gram))

    for k in ks:

        print(k)
        km = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=0)
        cluster_labels = km.fit_predict(x)

        print("inicio PCA")
        pca = TruncatedSVD(n_components=10)
        x = pca.fit_transform(x)
        print(pca.explained_variance_ratio_.sum())
        print("end PCA")

        print("inicio TSNE")
        tsne = TSNE(n_components=2, verbose=1, perplexity=40, n_iter=300)
        tsne_pca_results = tsne.fit_transform(x)
        print("end TSNE")

        df_tsne = pd.DataFrame(cluster_labels.ravel(), columns=['label'])
        # df_tsne['label'] = cluster_labels
        df_tsne['x-tsne-pca'] = tsne_pca_results[:, 0]
        df_tsne['y-tsne-pca'] = tsne_pca_results[:, 1]

        chart = ggplot(df_tsne, aes(x='x-tsne-pca', y='y-tsne-pca', color='label')) \
                + geom_point(size=70, alpha=0.1) \
                + ggtitle("tSNE dimensions colored by Digit (PCA)")
        chart


if __name__ == '__main__':
    show_2d_view()