from lxml import etree
import re
import requests
import execjs

class State_Grid:
    def __init__(self):
        self.url = 'https://www.nmpa.gov.cn/yaopin/ypjgdt/index.html'
        self.headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                      "avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                          "537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "sec-ch-ua": "^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^"
        }
        self.session = requests.session()

    def first_requset(self):
        first_response = self.session.get(url=self.url,headers=self.headers)
        headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://www.nmpa.gov.cn/yaopin/ypjgdt/index.html",
            "Sec-Fetch-Dest": "script",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "sec-ch-ua": "^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^"
        }
        url = "https://www.nmpa.gov.cn/fpqQrgG7L6po/eaKJbLE9bqof.294cc83.js"
        cookies = {
            "acw_tc": first_response.cookies.get("acw_tc"),
            "NfBCSins2OywO": first_response.cookies.get("NfBCSins2OywO"),
        }
        second_response = self.session.get(url, headers=headers, cookies=cookies)
        print(first_response.cookies)
        print(first_response)
        html = etree.HTML(first_response.text)
        ts_cd = html.xpath('//script[@r="m"]/text()')[0]
        content = re.findall('ta content="(.*?)" r="m',first_response.text,re.S)[0]
        with open('./test.js', 'r', encoding='UTF-8') as file:
            file = file.read().replace("arg1_content",content).replace("'arg2_function'",ts_cd)
        ctll = execjs.compile(file)
        cookie = ctll.call('go')
        all_cookie = re.findall('(.*?); path=/;',cookie,re.S)[0]
        list_cookie = all_cookie.split('=')
        cookies[list_cookie[0]] = list_cookie[1]
        return cookies

    def second_requset(self):
        cookies = self.first_requset()
        print(cookies)
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/"
                      "avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://www.nmpa.gov.cn/yaopin/ypjgdt/index.html",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/"
                          "537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
            "sec-ch-ua": "Google Chrome",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "^\\^Windows^^"
        }
        response = self.session.get(url=self.url,cookies=cookies,headers=headers)
        print(response)


if __name__ == '__main__':
    state_grid = State_Grid()
    state_grid.second_requset()
