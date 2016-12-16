import requests
import json
from utils import headers
from bs4 import BeautifulSoup
from datetime import date,timedelta


cookies_jar = requests.get('http://www.haodf.com/', headers=headers).cookies

# print cookies_jar

raw = requests.get('http://www.haodf.com/wenda/lixiangyangdr_g_4897693203.html',headers=headers).content

def parserQandA(raw):
    soup = BeautifulSoup(raw,'html.parser')
    question = soup.find(class_='h_s_cons_info_title')
    answer = soup.find_all(class_='h_s_cons_title')[1]
    return question.string,answer.string


def getDaymap(date):
    date = str(date).replace('-','')
    url = 'http://www.haodf.com/sitemap-zx/'+date+'_1/'
    raw = requests.get(url,headers=headers).content
    soup = BeautifulSoup(raw,'html.parser')
    urls = soup.find(class_='hh').find_all('a')
    return map(lambda x:str(x.get('href')), urls)
# except Exception as e:
    # print e


# print getDaymap(str(date(2016,12,1)).replace('-',''))[:-1]
start_date = date(2016,1,1)
end_date = date(2016,12,1)
dates_2016 = [ start_date + timedelta(n) for n in range(int ((end_date - start_date).days))]
# print map(lambda x:getDaymap(str(x).replace('-','')),[dates_2016])

result = []
for i in dates_2016:
    result += getDaymap(i)
    print len(result)
print len(result)

