import pandas
import string

from nltk.stem.snowball import SnowballStemmer
from load_dataset import path_dataset


def remove_pnt_and_stemming(text_arr):
    """ Remove pontuação e executa o o stemming de todo o dataset"""

    stemmer = SnowballStemmer("english", ignore_stopwords=True)

    for i in range(0, text_arr.shape[0]):
        x[i] = x[i].translate(str.maketrans('', '', string.punctuation))  # removendo todas as pontuaçoes
        words = x[i].split()
        x[i] = ""
        for word in words:
            x[i] += stemmer.stem(word) + " "
        x[i] = x[i].strip()
        x[i] = re.sub(r'[^A-Za-z]+', ' ', x[i])

    return text_final


def split_dataset_by_year(dataset, save_dataset=True):
    """ Split dataset por ano - retorna/salva 1 dataset para cada ano no arquivo ogirinal """

    key = str(dataset[0][0])[:4]
    datasets = []
    current_dataset = []

    for data in dataset:
        if key == str(data[0])[:4]:
            current_dataset.append(data[1])
        else:
            datasets.append(current_dataset.copy())
            key = str(data[0])[:4]
            current_dataset.clear()
            current_dataset.append(data[1])

    datasets.append(current_dataset.copy())

    if save_dataset:
        for i in range(0, len(datasets)):
            pandas.DataFrame(datasets[i]).to_csv("dataset_" + str(i + 1) + ".csv", index=False)

    return datasets


if __name__ == '__main__':
    split_dataset_by_year(path_dataset)