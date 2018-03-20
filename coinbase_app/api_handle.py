from info import Info
from coinbase.wallet.client import Client
import pandas as pd
import time

currencies = ['BCH', 'ETH', 'BTC', 'LTC']

api_info = Info()

client = Client(api_info.api_key, api_info.api_secret)

accounts = client.get_accounts()
# accounts.refresh()

# print accounts

exchange_rates = client.get_exchange_rates()

data = pd.DataFrame(columns=['time',
                             'currency_pair',
                             'spot_price',
                             'buy_price',
                             'sell_price'])

log_num = 1
while True:
    for entry in range(14400):
        for currency in currencies:
            currency_pair = currency + '-USD'
            server_time = client.get_time()
            buy_price = client.get_buy_price(currency_pair=currency_pair)
            sell_price = client.get_sell_price(currency_pair=currency_pair)
            spot_price = client.get_spot_price(currency_pair=currency_pair)

            data = data.append({'time': server_time['iso'],
                                'currency_pair': currency_pair,
                                'spot_price': spot_price['amount'],
                                'buy_price': buy_price['amount'],
                                'sell_price': sell_price['amount']},
                               ignore_index=True)

        with open('logs/log_{}.csv'.format(log_num), 'a') as f:
            if entry == 0:
                data.to_csv(f, header=True)
            else:
                data.to_csv(f, header=False)
        print
        "entry Number: " + str(entry) + '\n'
        time.sleep(5)

    log_num += 1
    print
    log_num

    '''
    data.append([server_time["iso"],
                 currency_pair,
                 spot_price["amount"],
                 buy_price["amount"],
                 sell_price["amount"]],
                ignore_index=True)
    '''

print
data
