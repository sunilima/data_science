import matplotlib.pyplot as plt

def display_barchart(column):
    """
    column: dataframe column
    """

    column.value_counts().plot(kind='bar')
    