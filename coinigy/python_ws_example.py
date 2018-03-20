import logging
from socketclusterclient import Socketcluster
import pandas as pd

logging.basicConfig(format="%s(levelname)s:%(message)s", level=logging.DEBUG)

import json

api_credentials = json.loads('{}')
api_credentials["apiKey"] = "f7fa52e512bd51b50d31f1c22abc2675"
api_credentials["apiSecret"] = "efc30946408facc7cc28b37a20b8893b"


def your_code_starts_here(socket):
    ###Code for subscription
    # print(socket.emit("channels","OK"))

    socket.subscribe('TRADE-BITS--BTC--USD')  # Channel to be subscribed

    def channelmessage(key, data):  # Messages will be received here
        print("\n\n\nGot data " + json.dumps(data, sort_keys=True) + " from channel " + key)

    socket.onchannel('TRADE-BITS--BTC--USD', channelmessage)  # This is used for watching messages over channel

    ###Code for emit

    def ack(eventname, error, data):
        # print ("\n\n\nGot ack data " + json.dumps(data, indent = 4, sort_keys=True) + " and eventname is " + eventname)

        data_org = pd.DataFrame(data[0])
        # print(data_org)
        return data_org

    socket.emitack("exchanges", None, ack)

    # print(socket.emit("channels", None))

    print('((((((')

    socket.emitack("channels", "OK", ack)


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
