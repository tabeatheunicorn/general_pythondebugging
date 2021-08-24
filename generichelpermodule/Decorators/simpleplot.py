import functools
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def save_figure_factory(**param):
    """ Plots and/or saves a figure depending on what parameters are passed to save_fig.
        Expects the function to draw some kind of plot.
    
        Possible params:
        filename: saves the figure to given str if present.
        show:     shows the resulting figure if present.
        else:     if none of the above is given, this just returns the function.
        """
    def func_decorator(func):
        @functools.wraps(func)
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
    return func_decorator


def overplot_functionfactory(x, y):
    """Add a plot with x,y datapairs to the plot that the decorated function creates.
        Function must not create a new figure in order for this to work!"""
    def overplot(func):
        @functools.wraps(func)
        def testplot_wrapper(*args, **kwargs):
            """Acutally plot before plotting function is called"""
            plt.plot(x, y)
            return func(*args, **kwargs)
        return testplot_wrapper
    return overplot


if __name__ == '__main__':
    df = pd.DataFrame(data={
        'foo': list(range(5)),
        'bar': list(range(5, 10, 1))
    })

    @save_figure_factory(**{'filename': 'foo.png', 'show': True})
    def plot_this():
        return plt.scatter(df['foo'], df['bar'])
    
    plot_this()
    # @overplot_functionfactory(x=np.linspace(0, 5),
    #                           y=np.linspace(0, 20))
    # def testplot():
    #     x, y = np.linspace(0, 5), np.linspace(0, 5)
    #     plt.plot(x, y)
        
    # testplot()
    # plt.show()
