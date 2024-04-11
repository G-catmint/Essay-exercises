import requests
from lxml import etree
import execjs
import json


class OuYeel:
    def __init__(self):
        self.session = requests.session()
        self.url = "https://www.ouyeel.com/search-ng/queryResource/index"
        self.data_url = "https://www.ouyeel.com/search-ng/commoditySearch/queryCommodityResult"
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "^sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^"
        }
        self.sec_headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://www.ouyeel.com/search-ng/queryResource/index",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "^sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^"
        }
        self.data_headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "https://www.ouyeel.com",
            "Pragma": "no-cache",
            "Referer": "https://www.ouyeel.com/search-ng/queryResource/index",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",
            "X-Tingyun-Id": "shNg2wpepqo;r=725050102",
            "^sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^"
        }

    def first_req(self):
        response = self.session.get(url=self.url,headers=self.headers)
        obj_html = etree.HTML(response.text)
        content_data = obj_html.xpath('//meta[2]/@content')[0]
        ts_code = obj_html.xpath('//script[1]/text()')[0]
        func_url = 'https://www.ouyeel.com' + obj_html.xpath('//script[2]/@src')[0]
        return content_data,ts_code,func_url

    def get_cookie(self,content_data,ts_code,func_url):
        func_code = self.session.get(url=func_url)
        with open("./ouzhi.js","r",encoding="utf-8") as file:
            js_code = file.read().replace("'fun_code'", func_code.text).replace("'content'", content_data).replace("'ts_code'", ts_code)
        cookie = execjs.compile(js_code).call("main")
        cookies = {
            'T0k1m0u5AfREP': cookie.split(';')[0].split('=')[1]
        }
        return cookies

    def scec_req(self,cookies,page):
        self.session.get(url=self.url,headers=self.sec_headers,cookies=cookies)
        data_data = {
            "criteriaJson": '{"pageIndex":' + str(page) + ',"pageSize":50,"industryComponent":null,"channel":null,"productType":null,"sort":null,"warehouseCode":null,"key_search":null,"is_central":null,"searchField":null,"companyCode":null,"inquiryCategory":null,"inquirySpec":null,"provider":null,"shopCode":null,"steelFactory":null,"resourceIds":null,"jsonParam":{},"excludeShowSoldOut":null}'
        }
        response = self.session.post(url=self.data_url,headers=self.data_headers,data=data_data,cookies=cookies)
        json_resp = eval(json.loads(response.text)['resultList'])
        for info in json_resp:
            if "resourceObj" in info:
                print("标题 : "+info['manufactureName']+" "+info['productName']+" "+info['resourceObj']['qualityGradeName']+" "+" 基本价格 : "+str(info['resourceObj']['basicPrice'])+" 发布价格 : "+str(info['resourceObj']['publishPrice'])+" 地址 : "+info['resourceObj']['storeCityName']+" | "+info['resourceObj']['warehouseName'])
            else:
                print("标题 : "+info['manufactureName']+" "+info['productName']+" "+info['qualityGradeName']+" "+" 基本价格 : "+str(info['startingPrice'])+" 发布价格 : "+str(info['publishPrice'])+" 地址 : "+info['storeCityName']+" | "+info['warehouseName'])


    def main(self,page):
        content_data,ts_code,func_url = self.first_req()
        cookies = self.get_cookie(content_data,ts_code,func_url)
        self.scec_req(cookies,page)



if __name__ == '__main__':
    ouyeel = OuYeel()
    ouyeel.main(1)