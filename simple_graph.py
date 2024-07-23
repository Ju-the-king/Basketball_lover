import numpy as np
import matplotlib.pyplot as plt
import plotly


def plot_data(database):
    """
    This function is a test to see if we can use the code in different branches
    :param database : database we are using
    :return:
    """
    data = database.head(6)
    team = data["Nickname"]
    block = data["BLK"]
    steal = data["STL"]
    turnover = data["TOV"]
    print(turnover)
    print(block + steal)
    for i in range(5):
        plt.scatter(turnover[i], block[i] + steal[i])
        plt.annotate(team[i], xy=(turnover[i], block[i] + steal[i]+1))
    plt.show()
