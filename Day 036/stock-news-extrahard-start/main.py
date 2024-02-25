import requests

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
alpha_api = "H4H6CT0KN4PPIBFW"
stock_price_api = "https://www.alphavantage.co/query"
stock_price_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_api
}

alpha_response = requests.get(stock_price_api, params=stock_price_params)
result = alpha_response.json()['Time Series (Daily)']

yesterday = list(result.values())[0]['4. close']
day_before_yesterday = list(result.values())[1]['4. close']
difference = abs(float(yesterday)/float(day_before_yesterday)-1)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_api = "8a588d1557244e4a9ba6b7794035a405"
newsapi = "https://newsapi.org/v2/everything"
new_params = {
    "q": COMPANY_NAME,
    "apiKey": news_api,
}

newsapi_response = requests.get(newsapi, params=new_params)
top_3_news = newsapi_response.json()['articles'][:3]

MSGBODY = f"{STOCK}: 🔺{difference*100}%\nHeadline1: {top_3_news[0]['title']}\nHeadline2: {top_3_news[1]['title']}\nHeadline3: {top_3_news[2]['title']}"

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

from twilio.rest import Client
SID = "ACdc27a6785b17277a1abf60a3e9fd86b5"
AUTH = "29e2b84bcb66c3933a213f73a1fd8802"

client = Client(SID, AUTH)

message = client.messages.create(
    body = MSGBODY,
    from_ = "+13257503261",
    to = "+6592340324"
    )

print(message.sid)
#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

