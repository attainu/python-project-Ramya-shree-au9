# BITCOIN PRICE NOTIFICATION                  
## BITCOIN PROJECT:
_______
![alt text](https://miro.medium.com/max/700/1*Jy_4rwG3dtf7rLUm7h0MRA.png)

## About:-
____
> As we all know, Crypto Currency price is a fickle thing.You never really know where it’s going 
    to be at the end of the day.  So,instead of constantly checking various sites for the latest updates,
    this python program push crypto currency price notifications at certain time interval and also notify 
    when price reach to a certain value as threshold value provided by user.

## Advantage Of Bitcoin
______
>By using a cryptocurrency, users are able to exchange value digitally without third party oversight


## Installation Guide:
____________
#### step by step series of examples and explanations about how to get your development env running.

### Step 1
* Either Download the Repo,Which you will find at the top right of Repo link or clone it in your Local Machine.

       git clone https://github.com/attainu/python-project-Ramya-shree-au9

### Step 2
* Go into the Folder by using command line. 

### Step 3
* Make Sure that your Machine has Python 3.8+
Run the follwing Command

        $ python3 Bitcoin_Notification.py --help

### Step 4
* Then, you will see the following options

        Optional arguments:

        -h, --help show this help message exit

        -e ALERT_AMOUNT, --alert_amount ALERT_AMOUNT
                        The price of 1 bitcoin when an emergency 
                        alert will be sent. Default is 10000 USD

        -t TIME_INTERVAL, --time_interval TIME_INTERVAL
                        The Frequency at which the Bitcoin value
                        is going to be Fetched from Server

        -d DESTINATION_APP,   --destination_app DESTINATION_APP
                        The Messaging Service Destiation 
                        1. TWITTER  
                        2. TELEGRAM

        -c CURRENCY, --currency CURRENCY
                        Bitcoin value in 
                        1.INR(Indian Rupees) 
                        2.USD(US Dollars)

        -ct COINTYPE, --cointype COINTYPE
                        Type of crypto currency is bitcoin

### Step 5
* If user didn't give above optional argument then python will consider below default parameter

    * alert_amount = 10000 
    * time_interval = 60 
    * coinType = 'Bitcoin'
    * currency = user’s choice out of the 2 option 1.INR (Indian Rupees) 2.USD (US Dollars)
    * For destination_app update will send to any app of the user’s choice out of the 2 option. 1. TWITTER   2. TELEGRAM

* After sends a notification to a Particular app, if the price does not cross the threshold limit it sends Android 
  SMS (particular phone no.).Otherwise a normal price update will send to the user's choice out of the 2 option.

## Target Applications:
_____
* Telegram
* Twitter
* Android SMS

## Python Packages & Libraries Used
________
* Request
* time
* Argparser
* Tqdm (For Progress bar)
## Technologies Used:
______
* Python 3.8
* HTTPS
* Webhooks
* Messaging Platforms Available:
    * Telegram
    * IFTTT App
    * Twitter
    * Android SMS

## Future Scope:
____
* Expand the Messaging Platforms
* Include other Cryptocurrency for this Project.

## API Reference:
____
* [Cinedesk Docs](https://www.coindesk.com/coindesk-api)
* [IFTTT API reference](https://platform.ifttt.com/docs/api_reference)

