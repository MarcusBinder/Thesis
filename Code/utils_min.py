import numpy as np
import matplotlib.pyplot as plt

def plot_learning_curve(x, scores, figure_file, ylim=[-10, 10]):
    running_avg = np.zeros(len(scores))
    for i in range(len(running_avg)):
        running_avg[i] = np.mean(scores[max(0, i-100):(i+1)])
    plt.plot(x, running_avg)
    plt.title('Running average of previous 100 scores')
    plt.grid()
    plt.ylim((ylim[0], ylim[1]))
    plt.savefig(figure_file)
