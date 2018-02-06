import pandas as pd
import Fetch_Data
import Ploting


def summarize_stats(sorted_data, exchange_names):
    all_stats = []

    # find highest & Lowest trading averages
    for exchange in exchange_names:
        data = sorted_data.loc[exchange]

        stats = data.describe()
        print('*******************' + exchange + '*******************')
        print(stats)
        all_stats.append(stats)

    summary_stats = pd.concat(all_stats, keys=exchange_names)

    return summary_stats


sorted_data = pd.read_excel("Downloaded Indexes.xlsx", header=[0], index_col=[0, 1])
exchange_names = sorted_data.index.levels[0].values

# sorted_data, exchange_names = Fetch_Data.download_all_exchange_data()

all_stats = summarize_stats(sorted_data, exchange_names)

# print(stats)
maxes = all_stats.idxmax()  # TODO: Look at lowExchange's Ask Price, and HighExchange's Bid Price
mins = all_stats.idxmin()

print(maxes.price[0], mins.price[0])

Ploting.graph_exchanges(sorted_data, [maxes.price[0], mins.price[0]])

# print(stats)
