# dt参数的断点：, z = D[ij(0x6ec)]();

from datayidun import YiDun
import requests
import execjs


class Moriary:
    def __init__(self):
        self.yidun = YiDun()
        self.headers = {
            "Accept": "*/*",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://dun.163.com/",
            "Sec-Fetch-Dest": "script",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Site": "same-site",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "^sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^"
        }
        self.url = "https://c.dun.163.com/api/v3/check"
        response = self.yidun.get_req()
        self.params = {
            "referer": "https://dun.163.com/trial/picture-click",
            "zoneId": "CN31",
            "dt": "cjOZJRxLrPNFAlUBUUbQuV3c6t00f+4o",
            "id": "07e2387ab53a4d6f930b8d9a9be71bdf",
            "token": response['token'],
            "acToken": "undefined",
            "data": response['data'],
            "width": "320",
            "type": "3",
            "version": "2.26.1",
            "cb": self.open_js("get_data")['get_cb'],
            "extraData": "",
            "bf": "0",
            "runEnv": "10",
            "sdkVersion": "undefined",
            "iv": "3",
            "callback":self.open_js("get_data")['callback']
        }

    @staticmethod
    def open_js(func,data=None):
        js = execjs.compile(open('all.js', encoding='utf-8').read()).call(func,data)
        return js

    def get_response(self):
        response = requests.get(url=self.url, headers=self.headers, params=self.params)
        print(response.text)


if __name__ == '__main__':
    moriary = Moriary()
    moriary.get_response()