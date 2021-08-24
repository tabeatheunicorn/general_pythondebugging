# %% Check if program is executed as notebook
def isnotebook():
    try:
        shell = get_ipython().class.name
        if shell == 'ZMQInteractiveShell':
            return True   # Jupyter notebook or qtconsole
        elif shell == 'TerminalInteractiveShell':
            return False  # Terminal running IPython
        else:
            return False  # Other type (?)
    except NameError:
        return False      # Probably standard Python interpreter

def select_displayer():
    # Use WebAgg if no d
    # isplay is connected (e.g. ssh) and not running as notebook
    import os
    import matplotlib
    import logging
    logger = logging.getLogger("Environment_Checker")
    if (os.name == 'posix' and "DISPLAY" not in os.environ) and not isnotebook():
        matplotlib.use('WebAgg')
    # Return used Matplotlib backend
    logger.info(matplotlib.get_backend())

    import matplotlib.pyplot as plt