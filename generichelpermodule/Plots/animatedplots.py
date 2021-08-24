import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
import numpy as np


def plot_seaborn_animation():
    def get_data(i=0):
        x,y = np.random.normal(loc=i,scale=3,size=(2, 260))
        return x,y

    x,y = get_data()
    g = sns.JointGrid(x=x, y=y, size=4)
    lim = (-10,10)

    def prep_axes(g, xlim, ylim):
        g.ax_joint.clear()
        g.ax_joint.set_xlim(xlim)
        g.ax_joint.set_ylim(ylim)
        g.ax_marg_x.clear()
        g.ax_marg_x.set_xlim(xlim)
        g.ax_marg_y.clear()
        g.ax_marg_y.set_ylim(ylim)
        plt.setp(g.ax_marg_x.get_xticklabels(), visible=False)
        plt.setp(g.ax_marg_y.get_yticklabels(), visible=False)
        plt.setp(g.ax_marg_x.yaxis.get_majorticklines(), visible=False)
        plt.setp(g.ax_marg_x.yaxis.get_minorticklines(), visible=False)
        plt.setp(g.ax_marg_y.xaxis.get_majorticklines(), visible=False)
        plt.setp(g.ax_marg_y.xaxis.get_minorticklines(), visible=False)
        plt.setp(g.ax_marg_x.get_yticklabels(), visible=False)
        plt.setp(g.ax_marg_y.get_xticklabels(), visible=False)


    def animate(i):
        g.x, g.y = get_data(i)
        prep_axes(g, lim, lim)
        g.plot_joint(sns.kdeplot, cmap="Purples_d")
        g.plot_marginals(sns.kdeplot, color="m", shade=True)

    frames=np.sin(np.linspace(0,2*np.pi,17))*5
    ani = animation.FuncAnimation(g.fig, animate, frames=frames, repeat=True)

    plt.show()
    

def plot_seaborn_heatmap_animation():
    rnd_data = np.random.normal(0, 1, (500, 100, 100))
    
    def animate(i):
        ax.cla()
        sns.heatmap(rnd_data[i, ...],
                ax = ax,
                cbar = True,
                cbar_ax = cbar_ax,
                vmin = rnd_data.min(),
                vmax = rnd_data.max())

    grid_kws = {'width_ratios': (0.9, 0.05), 'wspace': 0.2}
    fig, (ax, cbar_ax) = plt.subplots(1, 2, gridspec_kw = grid_kws, figsize = (12, 8))
    anim = animation.FuncAnimation(fig = fig, func = animate, frames = 200, interval = 50, blit = False)
    
    plt.show() # needs to be in  this function

if __name__ == "__main__":
    plot_seaborn_heatmap_animation()