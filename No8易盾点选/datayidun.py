from functools import partial
import random
import json
import re
from urllib import request
import requests
import execjs
import base64
import guiji
from jfbym import YdmVerify


class YiDun:
    def __init__(self):
        self.ydmverify = YdmVerify()
        self.get_url = "https://c.dun.163.com/api/v3/get"
        self.jsdata = execjs.compile(open("./data.js", "r", encoding="utf-8").read())
        self.get_headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        self.pic_headers ={
            "authority": "necaptcha.nosdn.127.net",
            "accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "referer": "https://dun.163.com/",
            "^sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^",
            "sec-fetch-dest": "image",
            "sec-fetch-mode": "no-cors",
            "sec-fetch-site": "cross-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        self.params = {
            "referer": "https://dun.163.com/trial/picture-click",
            "zoneId": "CN31",
            "dt": "cjOZJRxLrPNFAlUBUUbQuV3c6t00f+4o",
            "acToken": "9ca17ae2e6ffcda170e2e6eeb0e434aa9ef997d259f2bc8ea6d84a979e9ab0d47f9b8b9689ca5af491bfa9e22af0feaec3b92a8f94fdb9d05481b68698c44e928a8ab7c14e8d9be5aad84895b0fab9b53f928cee9e",
            "id": "07e2387ab53a4d6f930b8d9a9be71bdf",
            "fp": self.open_js("get_data")['fp'],
            "https": "true",
            "type": "3",
            "version": "2.26.1",
            "dpr": "1",
            "dev": "1",
            "cb": self.open_js("get_data")['get_cb'],
            "ipv6": "false",
            "runEnv": "10",
            "group": "",
            "scene": "",
            "lang": "zh-CN",
            "sdkVersion": "undefined",
            "iv": "3",
            "width": "320",
            "audio": "false",
            "sizeType": "10",
            "smsVersion": "v3",
            "token": "fa4bcc0af2db4b4386c6a5a161a500c2",
            "callback": self.open_js("get_data")['callback']
        }

    @staticmethod
    def open_js(func,data=None):
        js = execjs.compile(open('all.js', encoding='utf-8').read()).call(func,data)
        return js

    @staticmethod
    def save_pic(pic_name,url):
        response = requests.get(url=url)
        open(pic_name,"wb").write(response.content)
        return open(pic_name,'rb').read()

    def get_req(self):
        response = requests.get(url=self.get_url,headers=self.get_headers,params=self.params)
        get_info = json.loads(re.findall('.*?\((.*?)\);',response.text)[0])
        pic_url = get_info['data']['bg'][0]
        extra = get_info['data']['front']
        print(extra)
        token = get_info['data']['token']
        pic_content = self.save_pic("./pic/image.jpg",pic_url)
        jfbym_data = self.ydmverify.click_verify(image=pic_content,extra=','.join(extra))
        list_co = self.get_guiji(jfbym_data)[1]
        lis_tra = self.jsdata.call("j8",token,list_co)
        __co = self.get_guiji(jfbym_data)[0]
        lis__co = self.jsdata.call("j8", token, __co)
        js_code = self.jsdata.call("main", token,lis__co, lis_tra)
        print(js_code)
        return {
            "token": token,
            "data": js_code,
        }

    @staticmethod
    def get_guiji(coordinate):
        ___coor = coordinate.split("|")
        list_co = []
        __co = []
        for __coor in ___coor:
            __co.append(__coor.split(","))
        list_co.extend(guiji.erjie(int(__co[0][0]),int(__co[0][1]),int(__co[1][0]),int(__co[1][1])))
        list_co.extend(guiji.erjie(int(__co[1][0]),int(__co[1][1]),int(__co[2][0]),int(__co[2][1])))
        list_co[0].append(random.randint(195,350))
        for i in range(1,len(list_co)):
            list_co[i].append(list_co[i-1][2]+random.randint(5,15))
        __co[0].append(list_co[0][2]-random.randint(5,15))
        __co[1].append(list_co[random.randint(int(len(list_co)/2)-10,int(len(list_co)/2)+10)][2]-random.randint(5,15))
        __co[2].append(list_co[-1][2]+random.randint(5,15))
        return [__co,list_co]


if __name__ == '__main__':
    yidun = YiDun()
    yidun.get_req()
    # yidun.get_guiji("105,119|201,81|110,39")


