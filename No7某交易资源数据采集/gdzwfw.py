import requests
import time
import execjs
import asyncio
import aiohttp


class Gov:
    def __init__(self):
        self.headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json",
            "Origin": "https://ygp.gdzwfw.gov.cn",
            "Pragma": "no-cache",
            "Referer": "https://ygp.gdzwfw.gov.cn/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "X-Dgi-Req-App": "ggzy-portal",
            "X-Dgi-Req-Nonce": "liChhf9BoSXP3iSx",
            "X-Dgi-Req-Signature": "1c69ef3d76c112d651cfbc8f29030f18408d2c15c7f2cf72b884b6fa51c6f1e9",
            "X-Dgi-Req-Timestamp": str(int(time.time()*1000)),
            "^sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^"
        }
        self.jsdata = execjs.compile(open("./test.js", "r", encoding="utf-8").read())
        self.url = "https://ygp.gdzwfw.gov.cn/ggzy-portal/search/v2/items"
    def req_data(self,page):
        data = {
            "type": "trading-type",
            "openConvert": 'false',
            "keyword": "",
            "siteCode": "44",
            "secondType": "A",
            "tradingProcess": "",
            "thirdType": "[]",
            "projectType": "",
            "publishStartTime": "",
            "publishEndTime": "",
            "pageNo": page,
            "pageSize": 10
        }
        jscode = self.jsdata.call("main",data)
        self.headers['X-Dgi-Req-Timestamp'] = str(jscode[1])
        self.headers['X-Dgi-Req-Nonce'] = jscode[2]
        self.headers["X-Dgi-Req-Signature"] = jscode[0]
        response = requests.post(url=self.url,headers=self.headers,json=data)
        for info in response.json()['data']['pageData']:
            item = {}
            item['noticeTitle'] = info['noticeTitle']
            item['publishDate'] = info['publishDate']
            print(item)

if __name__ == '__main__':
    gov = Gov()
    for page in range(1,1000):
        gov.req_data(page)