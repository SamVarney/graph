from matplotlib import pyplot as plt
import pandas as pd
from coinigy_api_rest import *


# bits_exchange = open.data('BITS', 'BTC/USD', 'all')
# btcm_exchange = open.data('CBNK', 'BTC/USD', 'all')

def download_all_exchange_data(save=False):
    open = CoinigyREST(creds)

    all_exchanges_resp = open.request('exchanges')  # request info on supported exchanges

    exchanges = pd.DataFrame(all_exchanges_resp)  # convert response to dataframe

    keys = []  # hold keys (used to concatinate all dataframes at the end)
    histories = []  # array to hold history data (concatinated at the end)

    for exchange in exchanges.exch_code.values:
        data = open.data(exchange, 'BTC/USD', 'history')

        if len(data['history']) != 0:
            history = data['history']
            keys.append(exchange)
            histories.append(history)

    all_histories = pd.concat(histories, keys=keys)

    sorted_data = all_histories.sort_index()
    exchange_names = keys  # for the sake of reading clarity

    if save == True:
        sorted.to_excel("Downloaded Indexes.xlsx")  # TODO: figure out how to save & Parse multi Index nicely

    return sorted_data, exchange_names


sorted, names = download_all_exchange_data()

# index_names = sorted.index.levels[0].values

# print(sorted.index.levels[1])
# print(sorted.index.levels[1].tz_localize(None))
