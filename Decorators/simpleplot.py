import functools
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def save_fig(func, **param):
    """ Plots and/or saves a figure depending on what parameters are passed to save_fig"""
    def inner(*args, **kwargs):
        artist = func(*args, **kwargs)
        if 'filename' in param.keys():
            print('filename')
            plt.savefig(param['filename'])
        if 'show' in param.keys() and param["show"]:
            print('show')
            plt.show()
        else:
            return artist
    return inner


def save_show_no(plotfunc):
    # A function decorator that adds the option to save or show a plot
    # depending on whether a filename option is set.

    def decorate(*args, **kwargs):
        ax = plotfunc(*args)

        if 'filename' in kwargs.keys():
            plt.savefig(kwargs['filename'])

        elif 'show' in kwargs.keys():
            plt.show()

        else:
            return ax

    return decorate

def overplot_functionfactory(x,y):
    def overplot(func):
        """Acutally plot before and after function"""
        @functools.wraps(func)
        def testplot_wrapper(*args, **kwargs):
            plt.plot(x, y)
            return func(*args, **kwargs)
        return testplot_wrapper
    return overplot

@overplot_functionfactory(x=np.linspace(0,5), 
                          y= np.linspace(0,20))
def testplot():
    x, y = np.linspace(0,5), np.linspace(0,5)
    plt.plot(x,y) 


if __name__ == '__main__':
    # df = pd.DataFrame(data={
    #     'foo': list(range(5)),
    #     'bar': list(range(5, 10, 1))
    # })

    # @save_fig(**{'filename': 'foo.png', 'show': True})
    # def plot_this():
    #     return plt.scatter(df['foo'], df['bar'])

    testplot()
    plt.show() 