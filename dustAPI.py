from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import requests
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
queryParams = '?'+urlencode({quote_plus('serviceKey'):
    'LkdSSySmxfcaeFc/tKdOTVs35ZcASQISUraDwsqGNDcDqwGaDOqID+6BBMceRl12hrm8SFSPICxTPS2lmtoYVSg=='
    ,quote_plus('returnType'):'xml'
    ,quote_plus('numOfRows'):'100'
    ,quote_plus('pageNo'):'1'
    ,quote_plus('stationName'):'주안'
    ,quote_plus('dataTerm'):'DAILY'
    ,quote_plus('ver'):'1.0'})

res = requests.get(url+queryParams)
print(res)
soup = BeautifulSoup(res.content, 'html.parser')
data = soup.find_all('item')
print(url+queryParams)
print(data)
print('---')

for item in data:
    dataterm = item.find('')
    pm25value = item.find('pm25value')
    print(pm25value.get_text())
    print(dataterm.get_text())
