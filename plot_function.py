import matplotlib.pyplot as plt


class PlotFunction:
    count = 0
    year = 2003

    def __init__(self):
        self.style = ['r', 'g', 'b', 'y', 'b', 'r--']

    def add_function(self, x_plot, y_plot, id):
        self.count = id
        plt.plot(x_plot, y_plot, self.style[self.count], label="4-gram")

    def show(self, x_plot=None, fig_name=None):
        plt.legend(loc=1)
        plt.xlabel('Numero de clusters (K)')
        plt.ylabel('Cost function J')
        if x_plot is not None:
            plt.xticks(x_plot)
        # plt.yscale('log')
        # plt.yticks([10 ** 24 * (10 ** 26) ** i for i in range(11)])
        plt.grid(True)
        if fig_name is not None:
            plt.savefig("/home/jonlenes/Dropbox/_0000_report/by_year/" + fig_name + ".png")
            # plt.savefig("C:/Users/Kchristtyne/Dropbox/_0000_report/by_year/" + fig_name + ".png")
        #plt.show()

        plt.clf()
        plt.cla()
        plt.close()
