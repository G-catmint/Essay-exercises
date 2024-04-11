import requests
import time
import execjs
import json
import queue
import pymongo

class JingDong:
    global_queue = queue.Queue()
    def __init__(self):
        client = pymongo.MongoClient()
        self.collection = client['jd']['jd2']
        self.session = requests.session()
        self.cookie = {
            "__jdv": "209449046|direct|-|none|-|1712457059767",
            "shshshfpa": "f0eed065-f8d7-bcde-9eed-dce45f1b1e49-1712457060",
            "shshshfpx": "f0eed065-f8d7-bcde-9eed-dce45f1b1e49-1712457060",
            "__jdu": "1712457059767241933113",
            "wlfstk_smdl": "i5af64wjyu16ufeubmx9arzh9de9dawv",
            "3AB9D23F7A4B3C9B": "QMGJZUHE2X3CBTIGH2F7NO353OIVRLED2MYXY7PCOL6RCBTDFC2JUTCK2FASEPYN55N4GOMQI5VIAAZFGVYT3FIG2M",
            "TrackID": "1quYR7-Cw6wC-oeX-V7VyZps7GKRO5_sZBpE8e97Z4A0YGru9Q65d2S_O7ildFo41ZOglhjc7IjFOAF1PWLoZS3m9CY5AJ-lWsW5pPnOjBPlBPL4hqmEMG_ltHcdszQXT",
            "thor": "A12DFE1D812054796C53D9EA070BB436B02C7640AD6655D2FABA16CCE4FBBE03AA52519567039223BD0A6F827FF928DE3B45D1524F9DAFF7E7C064CCDFD1C8D280842D0D1692D7076B8FB4F84FEF581AB6714B386B16261EF854E68166064FE3563E344624B71580D5CB96A81DBC824C7D98BF1970306965EB19D696A0C4197CB37BA43BBA0680454C6930580325C3D6A851E039562320D65E0A6E6A26CBFA87",
            "flash": "2_bHSUD66uALshTyTv7bBUtExTwfXtkx-PF0kYUk-lCSvpcA_AOw396JhjreSEUKIATIi_oWmvqWkJThDyUFdYhBLE0S5jUpZRJ9fp8TMn96K*",
            "pinId": "8ziHFf5Y-SPanbavO_6mfA",
            "pin": "jd_yBsFJYkLAQJd",
            "unick": "jd_yBsFJYkLAQJd",
            "ceshi3.com": "000",
            "_tp": "WhaBQW9NO%2FdUxVT5TUyP5w%3D%3D",
            "_pst": "jd_yBsFJYkLAQJd",
            "__jda": "209449046.1712457059767241933113.1712457060.1712457060.1712548354.2",
            "__jdc": "209449046",
            "RT": "\"z=1&dm=jd.com&si=84z3hdtdcjn&ss=luqf2m8c&sl=9&tt=9ug\"",
            "__jdb": "209449046.17.1712457059767241933113|2.1712548354",
            "3AB9D23F7A4B3CSS": "jdd03QMGJZUHE2X3CBTIGH2F7NO353OIVRLED2MYXY7PCOL6RCBTDFC2JUTCK2FASEPYN55N4GOMQI5VIAAZFGVYT3FIG2MAAAAMOXPQDD7YAAAAAD64DZXUSZ33AHMX",
            "_gia_d": "1",
            "shshshfpb": "BApXeyqXouOtAGH51CpBSaiwktZPk3a-TBlAEd09t9xJ1MtU-D4C2"
        }
        self.headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "origin": "https://union.jd.com",
            "referer": "https://union.jd.com/",
            "sec-ch-ua": "\"Microsoft Edge\";v=\"123\", \"Not:A-Brand\";v=\"8\", \"Chromium\";v=\"123\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "x-referer-page": "https://union.jd.com/overview",
            "x-rp-client": "h5_1.0.0"
        }
        self.url = "https://api.m.jd.com/api"
        self.params = {
            "functionId": "unionSearch",
            "appid": "unionpc",
            "_": int(time.time()*1000),
            "loginType": "3",
            "uuid": "171254978110884372808",
            "x-api-eid-token": "jdd03P7K3JCON6PZRIGBDCUPPDOONTHU7ZK35U7VG4TOKHX3WGYR4NEDG2DKCBMMAYGIQFKUAYS3G7P2RZ4GBMCTEDFYPMQAAAAMOXMQTO4YAAAAAC6DSTDCSDXHTDMX",
            "h5st": "",
            "body": ""
        }

    @staticmethod
    def open_js(file,func, data=None):
        js = execjs.compile(open(file, encoding='utf-8').read()).call(func, data)
        return js

    def first_req(self,page):
        body = '{"funName":"search","version":"v3","source":20310,"param":{"pageNo":'+str(page)+',"pageSize":60,"searchUUID":"58e970af38e44669b312e3112cccc5ba","bonusIds":null,"category1":null,"category2":null,"category3":null,"deliveryType":null,"wlRate":null,"maxWlRate":null,"fromPrice":null,"toPrice":null,"hasCoupon":null,"isHot":null,"isNeedPreSale":null,"isPinGou":null,"isZY":null,"isCare":null,"lock":null,"orientationFlag":null,"sort":null,"sortName":null,"keyWord":"","searchType":"st3","keywordType":"kt0"},"clientPageId":"jingfen_pc"}'
        self.params['h5st'] = self.open_js('京东.js', "main", body)
        self.params['_'] = int(time.time()*1000)
        self.params['body'] = body
        response = self.session.get(self.url,headers=self.headers, cookies=self.cookie, params=self.params)
        print(response)
        if response.status_code != 200:
            self.global_queue.put(page)
        else:
            for info in response.json()['data']['skuPage']['result']:
                dict_data = {}
                dict_data['title'] = info['skuName']
                dict_data['wlPrice'] = info['wlPrice']
                dict_data['venderName'] = info['venderName']
                dict_data['goodComments'] = info['goodComments']
                self.collection.insert_one(dict_data)
                print("mongodb插入成功")

    def main(self):
        for page_queue in range(1,100):
            self.global_queue.put(page_queue)
        while not self.global_queue.empty():
            item = self.global_queue.get()
            self.first_req(item)

if __name__ == '__main__':
    jingdong = JingDong()
    jingdong.main()




