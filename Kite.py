import time
from kiteconnect import KiteConnect
import logging

class KiteApi:
    def __init__(self):
        logging.basicConfig(level=logging.DEBUG)

        # Loading api keys
        with open("API keys/kite_api.txt", "r") as file:
            api = file.readlines()
        kite_api_key = api[0].replace('\n', '')
        kite_req_token = api[1].replace('\n', '')
        kite_api_secret = api[2].replace('\n', '')

        kite = KiteConnect(api_key=kite_api_key)

        data = kite.generate_session(kite_req_token, api_secret= kite_api_secret)
