import pandas as pd
from matplotlib import pyplot as plt


# testData = pd.read_excel("Downloaded Indexes.xlsx", header = [0], index_col= [0,1])
# print(testData)

def graph_exchanges(data, exchanges_to_graph):
    for exchange in exchanges_to_graph:
        exchange_data = data.loc[exchange]
        plt.plot_date(x=exchange_data.index.values, y=exchange_data.price, ls='solid', linewidth='1.0', marker=None,
                      label=exchange)

    plt.legend()
    plt.show()

# exchanges_to_graph = ['BITS', 'BITF', 'CBNK']

# graph_exchanges(exchanges_to_graph)
