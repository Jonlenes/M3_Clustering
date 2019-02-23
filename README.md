# Clusters of News Headlines

## Activities

* Dataset preprocessing and feature extraction;
* TF-IDF, K-mens and the choice of K;


## The dataset
Million News Headlines contains 1 million data published over a 15-year period by Australian news source ABC (Australian Broadcasting Corp.).

| Year     | Samples  |   Year     |   Samples         |
|---|-------|-------|---------|
| 2003    |   59343   |   2011    |   69919   |
| 2004    |   65975   |   2012    |   78547  |
| 2005    |   66320   |   2013    |   81016  |
| 2006    |   61568   |   2014    |   73361  |
| 2007    |   69431   |   2015    |   70004   |
| 2008    |   71591   |   2016    |   52162  |
| 2009    |   68867   |   2017    |   44182  |
| 2010    |   67715   |     |

## Pre-processing
* Conversion to lowercase;
* Punctuation removal;
* Removal of words with size less than or equal to 2;
* Stemming;
* Removal of numbers.


## Feature Extration
Bag of Words

## TF-IDF
## K-Means

### Methods for choosing K
Elbow and Silhouette analysis.

## PCA e t-SNE
Principal component analysis (PCA) and T-Distributed Stochastic Neighbouring Entities (t-SNE).

## Experiments with the whole dataset

* Removal of stopwords;
* Disregarding words that appears in over 50% of documents;
* Disregarding words that do not occur in by at least 5 documents, to 1-gram, going up to 2 documents to 4-gram (with increasing gram, the amount of repetition in documents decreases);

### Experiment 1

* Features: 500;
* Dataset: 10%;
* Feature extraction: 1-gram, 2-gram, 3-gram and 4-gram;
* K: between: 2 and 250.

#### Elbow

<p align="center">
  <img src="imgs/1-gram.png">
</p>

<p align="center">
  <img src="imgs/2-gram.png">
</p>
  
<p align="center">
  <img src="imgs/3-gram.png">
</p>
  
<p align="center">
  <img src="imgs/4-gram.png">
</p>
    
#### Silhouette analysi

<p align="center">
  <img src="imgs/silhouette_0.png">
</p>

<p align="center">
  <img src="imgs/silhouette_3.png">
</p>

### Experiment 2
Com o intuindo de melhor o agrupamento, foi aumentada a quantidade de features para 1000 e diminuída a quantidade de K testados (2 <= K <= 100) para melhor visualização do gráfico e diminuição do tempo de execução. Os resultados para 3-gram podem ser visto na Figura.

<p align="center">
  <img src="imgs/10k_3-gram.png">
</p>


Novamente obteve-se diversos pontos possíveis para K, sendo alguns deles para k menor do 20. Para a finalização desta parte será realizado um ultimo experimento, como se segue.

### Experimento 3

Neste experimento foram realizadas mais algumas alterações no dataset, como se segue:

* Remoção de headlines duplicadas: ao analisar o dataset é possível perceber que se tem muitos exemplos duplicas, removendo-os, o tamanho do dataset é reduzido para 643715 exemplos;
* Todo o dataset foi utilizado (sem os valores duplicados);
* Foram considerados 10.000 features;
* K-Means foi executado somente para 2 <= K <= 20.

Os resultados obtidos para 4-gram podem ser visto nas figuras abaixo.

<p align="center">
  <img src="imgs/all_4-gram.png">
</p>

<p align="center">
  <img src="imgs/all_4-gram1.png">
</p>


Nessa primeira analise, considerando a função de custo e análise silhouette obteve se os melhores resultados com utilizando todos os exemplos não duplicados no dataset, 1000 features e 4-gram. No entanto, apareceu cotovelo em quase todos os pontos, quando se modificava o modelo treinado.

É percebível, que o numero de clusters exato dependo do objetivo e do que se deseja extrair do dataset. Neste caso, foi utilizado dois critérios para selecionar um possível numero de clusters: considerando todos os testes, os cotovelos mais apareceram e os que tiveram o melhor valor de silhouette.

Na tabela abaixo são apresentados os valores que mais apareceram em cada um dos casos (considerando valores de K menores do que ou igual a 20):


| Grams  | Valores de K                             |
|------|-------|
| 1-gram | 4, 6, 9, 10, 12, 13, 15, 16, 18, 19      |
| 2-gram | 2, 3, 4, 5, 7, 8, 10, 11, 12, 15, 17, 19 |
| 3-gram | 3, 5, 8, 9, 12, 14, 16, 17              |
| 4-gram | 5, 7, 8, 9, 11, 14, 16, 18, 19         |

Alguns dos valores que mais apareceram foi: 5, 12. Para esses valores de K, foi executada novamente o treinamento e obtido os valores de silhouette utilizando 1-gram e 4-gram, conforme tabela abaixo.

| Gram   | K  | Silhouette |
|----|-----|-----|
| 1-gram | 5  | 0.0154    |
| 1-gram | 12 | 0.0233    |
| 4-gram | 5  | 0.9719     |
| 4-gram | 12 | 0.9761      | 

Como pode ser observado, os valores de Silhouette foram bem melhores para 4-gram, sendo praticamente equivalente para K igual a 5 e K igual a 12. Nesse caso foi utilizando K = 5 para apresentar as palavras comuns em cada clusters, conforme abaixo (serão mostradas apenas 10 palavras como exemplo para cada cluster). 


**Cluster 1**: vic countri hour podcast, rural qld rural report, rural nsw rural report, sa countri hour podcast, nation rural news wednesday, man face court accus, aung san suu kyi, test day live blog, nation rural news tuesday, speak abc news breakfast;
**Cluster 2**: nation rural news monday, youth mental health servic, form guid men m, gold coast man face, gold coast light rail, gold coast hit run, gold coast high rise, gold coast commonwealth game, given suspend jail term, given good behaviour bond;
**Cluster 3**: nsw countri hour wednesday, countri hour wednesday decemb, countri hour wednesday septemb, countri hour wednesday novemb, countri hour wednesday april, countri hour wednesday june, countri hour wednesday octob, countri hour wednesday januari, countri hour wednesday august, countri hour wednesday februari;
**Cluster 4**: tas countri hour friday, countri hour friday octob, countri hour friday april, countri hour friday june, countri hour friday august, countri hour friday juli, countri hour friday march, countri hour friday novemb, heavi rain caus flood, heavi rain caus flash;
**Cluster 5**: wa countri hour podcast, countri hour podcast octob, countri hour podcast th, countri hour podcast decemb, countri hour podcast septemb, countri hour podcast juli, countri hour podcast august, countri hour podcast februari, countri hour podcast januari, countri hour podcast march.
    
## Experimentos por ano
 
Para os experimentos por ano foi considerado todo o dataset (com 1M de exemplos), dividido por ano, para cada ano foi removidas headlines duplicadas. Após a remoção das headlines duplicadas, para cada ano, os exemplos diminuíram de 34% a 37%.

Após esse processo, os mesmo experimentos da seção anterior foi realizado para cada ano, conforme resumo dos experimentos apresentados na tabela abaixo.


| Ano  | K                   | Ano  | K                    | 
| -----| -----| ----| -----| 
| 2003 | 3, 5, 8, 11, 16     | 2011 | 3, 5, 11             |
| 2004 | 3, 6, 9, 11, 15     | 2012 | 3, 5, 8, 13, 16      |
| 2005 | 4, 6, 9, 11, 13, 18 | 2013 | 4, 7, 10, 13, 15     |
| 2006 | 3, 8, 11, 13, 15    | 2014 | 3, 7, 10, 14         |
| 2007 | 3, 5, 6, 10, 18     | 2015 | 5, 8, 11, 14, 16     |
| 2008 | 4, 8, 13, 16, 19    | 2016 | 4, 6, 10, 13, 17     |
| 2009 | 4, 9, 13, 15, 18    | 2017 | 4, 8, 10, 12, 15, 17 | 


Com a divisão do dataset por ano, facilitou a utilização do algoritmo de agrupamento, pois a quantidade de dados é bem menor com essa divisão. No entanto, os resultados com o dataset divididos por ano não foi tão bons quanto o do dataset inteiro, considerando o valor de silhouette, e principalmente na visualização dos resultados.

Considerando a tabela por ano é possível perceber que o valor de K = 3 aparecer em quase todos os anos, sendo um possível escolha para valor de K.

## Cluster visualization

<p align="center">
  <img src="imgs/3-clusters.png">
</p>

<p align="center">
  <img src="imgs/5-clusters.png">
</p>
