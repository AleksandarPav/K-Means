import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.metrics import classification_report, confusion_matrix


def main():
    # the goal is to categorize features into two groups - private and public universities

    # reading data into a dataframe
    df = pd.read_csv('College_Data', index_col = 0)

    # data information
    print(df.head())
    print(df.info())
    print(df.describe())

    # scatterplot of Grad.Rate versus Room.Board where the points are colored by the Private feature
    sns.scatterplot(x = 'Room.Board', y = 'Grad.Rate', data = df, hue = 'Private')

    # scatterplot of F.Undergrad versus Outstate where the points are colored by the Private feature
    plt.figure()
    sns.scatterplot(x = 'Outstate', y = 'F.Undergrad', hue = 'Private', data = df)

    # histogram showing Out of State Tuition based on the Private feature
    sns.set_style('darkgrid')
    g = sns.FacetGrid(data = df, hue = 'Private', height = 6, aspect = 2)
    g = g.map(plt.hist, 'Outstate', bins = 20, alpha = 0.7)

    # similar histogram for the Grad.Rate feature
    sns.set_style('darkgrid')
    g = sns.FacetGrid(data = df, hue = 'Private', height = 6, aspect = 2)
    g = g.map(plt.hist, 'Grad.Rate', bins = 20, alpha = 0.7)

    # there is a private school with a graduation rate of higher than 100%
    print(df[df['Grad.Rate'] > 100])

    # setting that school's graduation rate to 100 so it makes sense
    df['Grad.Rate'].loc[df['Grad.Rate'] > 100] = 100
    print(df[df['Grad.Rate'] > 100])

    # instance of a K Means model with 2 clusters
    kmeans = KMeans(n_clusters = 2)

    # fitting the model to all the data except for the Private label
    kmeans.fit(df.drop('Private', axis = 1))

    # cluster center vectors
    print(kmeans.cluster_centers_)

    # new column called 'Cluster', which is a 1 for a Private school, and a 0 for a public school
    df['Cluster'] = df['Private'].apply(converter)
    print(df['Cluster'])

    # confusion matrix and classification report to see how well the Kmeans clustering worked
    print(confusion_matrix(df['Cluster'], kmeans.labels_), '\n')
    print(classification_report(df['Cluster'], kmeans.labels_))

    plt.show()


def converter(private):
    if private == 'Yes':
        return 1
    else:
        return 0


if __name__ == '__main__':
    main()