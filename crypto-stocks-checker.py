import requests
from lxml import html
# import pandas as pd
#yahoo allows only 100 days data through scrapping probably.
#user agent -> to get all source code of requested url.
user_agent={
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
}

url="https://finance.yahoo.com/quote/BTC-USD/history?p=BTC-USD"
response = requests.get(url=url, headers=user_agent)
html_content = html.fromstring(response.content)
date = html_content.xpath('//tr[@class = "BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)"]/td[1]/span/text()')
close_price = html_content.xpath('//tr[@class = "BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)"]/td[5]/span/text()')

#map closing price with date
date_price = {}
for i in range(len(date)):
	date_price[date[i]]=close_price[i]


"""take input as date from user and use dictionary to get the price of that date and 
current date and calcualate the profit and loss."""

user_date=input("Enter the date on which you invested in bitcoin,\nFormate of date(Mar 20, 2021, for date below 10, enter like: Mar 01, 2021),\nRange of date(last 100 days): ")

if user_date in date:
	price = date_price[user_date]
	price = float(price.replace(',', ''))

	current_price = close_price[0]
	current_price = float(current_price.replace(',', ''))
	profit=((current_price-price)*100)/price
	profit=format(profit, '.2f')
	print(f"Your current profit/loss is: {profit}%")
else:
	print('either date is out of range or check the format of date')


