from __future__ import print_function, division
# http://www-personal.umich.edu/~mejn/computational-physics/
from pylab import scatter, xlabel, ylabel, xlim, ylim, show
from numpy import loadtxt
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def givenmethod(file):
    data = loadtxt(file, float)
    x = data[:, 0]
    y = data[:, 1]

    scatter(x, y)
    xlabel("Temperature")
    ylabel("Magnitude")
    xlim(0, 13000)
    ylim(-5, 20)
    show()


# ("../../Downloads/stars.dat",
def mymethod(samefile):
    df = pd.read_csv(stars, sep=r'\s+', header=None, names=['x', 'y'])
    sns.scatterplot(data=df, x='x', y='y')
    sns.set(style="whitegrid")
    plt.xlabel('Temperature')
    plt.ylabel('Magnitude')
    plt.title('Seaborn Scatter Plot')
    plt.show()


if __name__ == "__main__":
    stars = r"C:\Users\shipp\PycharmProjects\Simulacion_de_Sistemas\stars.dat"

    mymethod(stars)
    givenmethod(stars)
