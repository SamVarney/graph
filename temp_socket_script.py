import logging
from socketclusterclient import Socketcluster
import pandas as pd
import datetime

logging.basicConfig(format="%s(levelname)s:%(message)s", level=logging.DEBUG)

import json

api_credentials = json.loads('{}')

api_credentials["apiKey"] = "f7fa52e512bd51b50d31f1c22abc2675"
api_credentials["apiSecret"] = "efc30946408facc7cc28b37a20b8893b"
COUNT = 0


def your_code_starts_here(socket):
    ###Code for subscription
    socket.subscribe('6492D451-6E10-F8A0-1F30-31F262BAD25E')  # Channel to be subscribed

    def channelmessage(key, data):  # Messages will be received here
        global COUNT
        print("****** Update #: " + str(COUNT))
        COUNT += 1
        print("\n\n\nGot data " + json.dumps(data, sort_keys=True) + " from channel " + key)

        data_val = pd.DataFrame(data['Data'])

        timeStamp = str(datetime.datetime.now())
        timeKeys = pd.Series([timeStamp for i in range(len(data_val))], )

        data_val.set_index(['exch_code', timeKeys], inplace=True)

        # print(data_val.to)

        with open('my_csv_2.csv', 'a') as f:
            if COUNT == 0:
                print(COUNT)
                data_val.to_csv(f, header=True, columns=True)
            else:
                data_val.to_csv(f, header=False)

    socket.onchannel('6492D451-6E10-F8A0-1F30-31F262BAD25E',
                     channelmessage)  # This is used for watching messages over channel

    ###Code for emit

    def ack(eventname, error, data):
        print("\n\n\nGot ack data " + json.dumps(data, sort_keys=True) + " and eventname is " + eventname)

    # socket.emitack("exchanges", None, ack)

    # socket.emitack("channels", "OK", ack)


def onconnect(socket):
    logging.info("on connect got called")


def ondisconnect(socket):
    logging.info("on disconnect got called")


def onConnectError(socket, error):
    logging.info("On connect error got called")


def onSetAuthentication(socket, token):
    logging.info("Token received " + token)
    socket.setAuthtoken(token)


def onAuthentication(socket, isauthenticated):
    logging.info("Authenticated is " + str(isauthenticated))

    def ack(eventname, error, data):
        print("token is " + json.dumps(data, sort_keys=True))
        your_code_starts_here(socket);

    socket.emitack("auth", api_credentials, ack)


if __name__ == "__main__":
    socket = Socketcluster.socket("wss://sc-02.coinigy.com/socketcluster/")
    socket.setBasicListener(onconnect, ondisconnect, onConnectError)
    socket.setAuthenticationListener(onSetAuthentication, onAuthentication)
    socket.setreconnection(False)
    socket.connect()
