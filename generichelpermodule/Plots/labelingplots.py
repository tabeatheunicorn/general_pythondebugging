import matplotlib.pyplot as plt


def labelled_row_and_columns_subplots():
    cols = ['Column {}'.format(col) for col in range(1, 4)]
    rows = ['Row {}'.format(row) for row in ['A', 'B', 'C', 'D']]

    fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(12, 8))

    for ax, col in zip(axes[0], cols):
        ax.set_title(col)

    for ax, row in zip(axes[:,0], rows):
        ax.set_ylabel(row, rotation=0, size='large')

    fig.tight_layout()
    plt.show()
    
    
if __name__ == '__main__':
    labelled_row_and_columns_subplots()