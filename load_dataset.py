import pandas
import pandas as pd
from nltk.corpus import stopwords

path_dataset = "./dataset/"


def load_csv_file(file_name):
    """
    Carrega um arquivo csv no path_dataset
    """
    return pandas.read_csv(path_dataset + file_name)


def load_base_dataset(perct=1):
    """
    Carrega o dataset
    """
    if perct != 1:
        return load_csv_file("news_headlines4.csv").sample(frac=perct).values
    return load_csv_file("news_headlines4.csv").values


def load_changed_dataset():
    """
    Carrega o dataset.
    """
    return load_csv_file("dataset_PCA90.csv").values


def load_datasets(index_last_dataset=15):
    """
    Carrega todos os datasets
    """
    datasets = []
    for i in range(1, index_last_dataset + 1):
        datasets.append(load_csv_file("dataset_" + str(i) + ".csv").values.ravel())

    return datasets

def load_datasets2(index_last_dataset=15):
    """
    Carrega todos os datasets
    """
    datasets = []
    for i in range(1, index_last_dataset + 1):
        datasets.append(  pd.read_csv(path_dataset + "dataset_" + str(i) + ".csv", error_bad_lines=False))

    return datasets
