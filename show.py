import matplotlib.pyplot as plt

def my_plot(x, y):
    plt.plot(x, y)
    plt.savefig('distribution', dpi=300, bbox_inches='tight')
    plt.show()