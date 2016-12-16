from sqlalchemy.orm import sessionmaker
import requests
import json
from models import Stock
from utils import headers, BASE_URL, engine
from bs4 import BeautifulSoup

Session = sessionmaker(bind=engine)

cookies_jar = requests.get('https://xueqiu.com', headers=headers).cookies


def crawl_stocks_name():
    raw_stocks_list = requests.get("http://ctxalgo.com/api/stocks")
    print(raw_stocks_list)
    stocks_list = json.loads(raw_stocks_list.content.decode('utf-8'))
    print(stocks_list)
    for i in stocks_list:
        print(i)
        new_stock = Stock(name=stocks_list[i], code=i)
        session2 = Session()
        session2.add(new_stock)
        session2.commit()
        print(new_stock.id,new_stock.code,new_stock.name)
        session2.close()

#cawl_stocks_name()


def crawl_stocks_followers(code):
    try:
        stocks_url = BASE_URL + str(code) + "/follows"
        raw = requests.get(stocks_url, headers=headers, cookies=cookies_jar)
        soup = BeautifulSoup(str(raw.content),"html.parser")
        number = soup.find("div", class_ ="stockInfo").span.string.split("(")[1].split(")")[0]
        return number
    except Exception as e:
        print(e)
        return 404
# print(crawl_stocks_followers("sh600519"))


def crawl_stocks_prices(code):
    try:
        stocks_url = BASE_URL + str(code)
        raw = requests.get(stocks_url, headers=headers, cookies=cookies_jar)
        soup = BeautifulSoup(str(raw.content),"html.parser")
        prices = soup.find("strong", class_ ="stockUp").string.split("xa5")[1]
        return prices
    except Exception as e:
        print(e)
        return 404
#print(crawl_stocks_prices("sh600519"))
