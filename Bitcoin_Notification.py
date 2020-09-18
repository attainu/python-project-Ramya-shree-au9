import requests # Import From Library
import time
import json
import argparse
from datetime import datetime
from tqdm import tqdm

# Coinmarket _API_URL
BITCOIN_API_URL_INR = 'https://api.coindesk.com/v1/bpi/currentprice/INR.json'
BITCOIN_API_URL_USD = 'https://api.coindesk.com/v1/bpi/currentprice.json'
# IFTTT_Webhooks_URL
IFTTT_WEBHOOKS_URL = 'https://maker.ifttt.com/trigger/{}/with/key/NF-CSWQZErEpMx6UJNDlktZQKIw5hRJsoGwChxtnS-'

# Latest Bitcoin Price is Fetched from Bitcoin API.
def get_latest_bitcoin_price_in_inr():
    response = requests.get(BITCOIN_API_URL_INR)    
    response_json = response.json()
    return(float(response_json['bpi']['INR']['rate_float'])) # (Bitcoin Price Is Get In Indian Rupee)

# Latest Bitcoin Price is Fetched from Bitcoin API.
def get_latest_bitcoin_price_in_usd():
    response = requests.get(BITCOIN_API_URL_USD)
    response_json = response.json()
    return(float(response_json['bpi']['USD']['rate_float'])) # (Bitcoin Price Is Get In US dollars)
  
# Formating The Bitcoin Price Notification in INR.
def format_bitcoin_price_in_inr(price): 
    date = datetime.now()
    date, price = date.strftime('%d.%m.%Y %H:%M'),price
    row = '{}: ₹ <{}>'.format(date, price)
    return row  # Format Of Bitcoin Price Is Shows First Date,Time And value Of The Bitcoin

# Formating The Bitcoin Price Notification in USD
def format_bitcoin_price_in_usd(price): 
    date = datetime.now()
    date, price = date.strftime('%d.%m.%Y %H:%M'),price
    row = '{}: $ <{}>'.format(date, price)
    return row

# It Post The Message To webhook. 
def post_ifttt_webhook(value, event):
    data = {'value1': value}
    post_event = IFTTT_WEBHOOKS_URL.format(event)
    requests.post(post_event, json=data) 

# When Choose TELEGRAM  Notification,Push IFTTT Master Driver That Fetches The Data And Post TO App. 
def telegram_master_driver(alert, time_interval, bitcoin_price, format_bitcoin,BITCOIN_ALERT_LIMIT):
    print("Welcome :) ")
    print("Bitcoin Notification Updating")
    TIME_INTERVAL = float(time_interval[0])
    x = 1
    for i in tqdm(range(0,100000)):
        for x in range(0,1000):
            x*=4 
    while True:
        if bitcoin_price < BITCOIN_ALERT_LIMIT:  # IF Bitcoin Price Is BeloW Alert Limit, Notification Sends To This NUmber - 919535940239
            print("You Will Receive a SMS in This Number - 919535940239")
            event = 'Bitcoin_Price_Emergency'
            post_ifttt_webhook(format_bitcoin, event)
            
        else:                # Else Message Sends To telegram
            print('You will Receive a Text-Message In Telegram')
            event = 'Latest_Bitcoin_Price_Alert'
            post_ifttt_webhook(format_bitcoin, event)

        time.sleep(5 * TIME_INTERVAL)

# When Choose Twitter Notification,Push IFTTT Master Driver That Fetches The Data And Post TO App. 
def twitter_master_driver(alert, time_interval, bitcoin_price, format_bitcoin, BITCOIN_ALERT_LIMIT):
    print("Welcome :) ")
    print("Bitcoin Notification Updating")
    TIME_INTERVAL = float(time_interval[0])
    x = 1
    for i in tqdm(range(0,100000)):
        for x in range(0,1000):
            x*=4 
    while True:
        if bitcoin_price < BITCOIN_ALERT_LIMIT:     ## IF Bitcoin Price Is BeloW Alert Limit, Notification Sends To This NUmber - 919535940239
            print("You Will Receive a SMS in This Number - 919535940239")
            event = 'Bitcoin_Price_Emergency'
            post_ifttt_webhook(format_bitcoin, event)
            
        else:                   # Else Tweets The Twitter Acount
            print('Plese Follow This Twitter Acount - https://twitter.com/HcRamyashree')
            event = 'Latest_bitcoin_price'
            post_ifttt_webhook(format_bitcoin, event)
        
        time.sleep(5 * TIME_INTERVAL)

# This Is The Matrix Of This App,Which Takes The Input Throght CLI And Passes It.
def MainControlFunc():
    input = argparse.ArgumentParser(
        description='Bitcoin Price Notification App.', epilog='This Script helps in sharing Real-Time Bitcoin Prices to Appropriate Services')

    input.add_argument('-e', '--alert_amount',default=[736745.00, 10000], # (10000 USD = 736745.00 Indian Rupee) 
                        help='The price of 1 bitcoin when an emergency alert will be sent. Default is 10000 USD')

    input.add_argument('-t', '--time_interval', default=[60], 
                        help='The Frequency at which the Bitcoin value is going to be Fetched from Server')
    
    input.add_argument('-d', '--destination_app',
                        help='The Messaging Service Destiation 1. TWITTER 2. TELEGRAM', required=True)

    input.add_argument('-c', '--currency',  
                        help='Bitcoin value in 1.INR (Indian Rupees 2.USD (US Dollars)', required = True)

    input.add_argument('-ct', '--cointype',  default=['Bitcoin'], # (In Cryptocurrency Choosing Bitcoin)
                        help='Type of crypto currency is bitcoin')

    args = input.parse_args()

    # This Is The Switch Control This Will Call Only That Function That Is Mentioned
    # By User And Transfer The Control To It.
    if(args.destination_app == 'TELEGRAM' and args.currency == 'INR'):
        bitcoin_price = get_latest_bitcoin_price_in_inr()
        format_bitcoin = format_bitcoin_price_in_inr(bitcoin_price)
        BITCOIN_ALERT_LIMIT = float(args.alert_amount[0])
        telegram_master_driver(args.alert_amount,
                            args.time_interval,bitcoin_price,format_bitcoin,BITCOIN_ALERT_LIMIT)
    
    if(args.destination_app == 'TELEGRAM' and args.currency == 'USD'):
        bitcoin_price = get_latest_bitcoin_price_in_usd()
        format_bitcoin = format_bitcoin_price_in_usd(bitcoin_price)
        BITCOIN_ALERT_LIMIT = float(args.alert_amount[1])
        telegram_master_driver(args.alert_amount,
                            args.time_interval,bitcoin_price,format_bitcoin,BITCOIN_ALERT_LIMIT)

    if(args.destination_app == 'TWITTER' and args.currency == 'INR'):
        bitcoin_price = get_latest_bitcoin_price_in_inr()
        format_bitcoin = format_bitcoin_price_in_inr(bitcoin_price)
        BITCOIN_ALERT_LIMIT = float(args.alert_amount[0])
        twitter_master_driver(args.alert_amount,
                            args.time_interval,bitcoin_price,format_bitcoin,BITCOIN_ALERT_LIMIT)

    if(args.destination_app == 'TWITTER' and args.currency == 'USD'):
        bitcoin_price = get_latest_bitcoin_price_in_usd()
        format_bitcoin = format_bitcoin_price_in_usd(bitcoin_price)
        BITCOIN_ALERT_LIMIT = float(args.alert_amount[1])
        twitter_master_driver(args.alert_amount,
                            args.time_interval,bitcoin_price,format_bitcoin,BITCOIN_ALERT_LIMIT)
   
   
if __name__ == '__main__':
    MainControlFunc()   # Main Function
