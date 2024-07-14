import numpy as np
import matplotlib.pyplot as plt
import plotly


def plot_data(database):
    """
    This function is a test to see if we can use the code in different branches
    :param database : database we are using
    :return:
    """

    data = database[:5][:]
    player = data["Player"]
    points = data["PTS"]
    mp = data["MP"]
    for i in range(5):
        plt.plot(mp[i], points[i])
        plt.annotate(player[i], xy=(mp[i], points[i]))
    plt.show()
