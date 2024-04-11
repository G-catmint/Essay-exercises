import requests
from lxml import etree
import execjs


class Sugh:
    def __init__(self):
        self.session = requests.session()
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
        self.url = "https://sugh.szu.edu.cn/Html/News/Columns/7/2.html"
        self.sec_headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://sugh.szu.edu.cn/Html/News/Columns/7/2.html",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "^sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^"
        }
    def fail_req(self):
        response = self.session.get(url=self.url, headers=self.headers)
        obj_html = etree.HTML(response.text)
        content_data = obj_html.xpath('//meta[2]/@content')[0]
        func_code = obj_html.xpath('//script[2]/text()')[0]
        no1_code = obj_html.xpath("//script[@type='text/javascript']/text()")[1].split()[0]
        no2_code = obj_html.xpath("//script[@type='text/javascript']/text()")[2].split()[0]
        ts_url = 'https://sugh.szu.edu.cn' + obj_html.xpath('//script[1]/@src')[0]
        return content_data,func_code,ts_url,response.cookies['ihkYnttrQXfVO'],no1_code,no2_code

    def success_req(self,content_data, func_code, ts_url,ihkYnttrQXfVO,no1_code,no2_code):
        ts_code = requests.get(ts_url)
        with open('./瑞数5.js', encoding='utf-8') as f:
            js_code = f.read().replace("'fun_code'", func_code).replace("'ts_code'", ts_code.text).replace("'content'",content_data).replace("'No.1'", no1_code).replace("'No.2'", no2_code)
        js = execjs.compile(js_code)
        cookie = js.call('main')
        print(cookie)
        cookies = {
            'ihkYnttrQXfVP': cookie.split(';')[0].split('=')[1]
        }
        return cookies

    def main(self):
        content_data, func_code, ts_url,ihkYnttrQXfVO,no1_code,no2_code = self.fail_req()
        cookies = self.success_req(content_data, func_code, ts_url,ihkYnttrQXfVO,no1_code,no2_code)
        response = self.session.get(url=self.url,headers=self.sec_headers,cookies=cookies)
        response.encoding = response.apparent_encoding
        obj_html = etree.HTML(response.text)
        title_list = obj_html.xpath("//ul[@id='zoom']/li/a[@class='dy_title']/text()")

        href_list = obj_html.xpath("//ul[@id='zoom']/li/a[2]/@href")
        data_list = obj_html.xpath("//ul[@id='zoom']/li/div/span[2]/text()")

        for title, href, data in zip(title_list, href_list, data_list):
            item = dict()
            item["title"] = title
            item["data"] = data
            item["href"] = href
            print(item)


if __name__ == '__main__':
    sugh = Sugh()
    sugh.main()

