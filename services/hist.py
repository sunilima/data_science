import matplotlib.pyplot as plt

def display_histogram(column):
    """
    column: dataframe column
    """

    plt.hist(column,bins=4,edgecolor='black')