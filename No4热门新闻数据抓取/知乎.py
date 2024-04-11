import requests
import pymongo


class ZhiHu:
    def __init__(self):
        client = pymongo.MongoClient()
        self.collection = client['zhihu']['info']
        self.headers = {
            "authority": "www.zhihu.com",
            "accept": "*/*",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "^cookie": "_zap=2c418b2f-2204-4f29-b8aa-0538771d8496; d_c0=AMBU-bLXbhePTi6E0hEACoqFYEVeLU7GF1Y=^|1695355510; YD00517437729195^%^3AWM_TID=^%^2FTwNX0QOzM1EEAAUFROVycqfFxANm18d; __snaker__id=qbdmGPvJn1cLU9vc; YD00517437729195^%^3AWM_NI=Kxn5W0MdfpVd8Ajo1ub5kFuxtj6rwcNsAS^%^2F0cb3FQ0pta7PZ4uIq7NKv2LVtEJuLg0J1YW63YoN0xoTH2awjjjchOwL^%^2BYpPiIbIQuiz2himDfWDrkcqR1XupD^%^2Fts93egUDE^%^3D; YD00517437729195^%^3AWM_NIKE=9ca17ae2e6ffcda170e2e6eed1b743a991bbd4b63497b48bb6c85b928b8bb1d572a7bdfdccec3eedb0a489f82af0fea7c3b92a89a8a2d6d63c8fbcaa91d570fc9fa690b47fa2eba5a7f874b8b6fa93f6698ead8fb4ae3ca1befda7d43cb4acafd8d352f8ab8792b64689aafeadd5808796bbade63c8aef97b8b5399bb182d1fb659898fe82f662aab6ad89ce7d90f59791d3638bbe87b2f863baeea88af050a6898c93ea69b38effb9f87c88f1bc94bc39a7b99ba5c837e2a3; z_c0=2^|1:0^|10:1712143044^|4:z_c0^|80:MS4xU1dQb01BQUFBQUFtQUFBQVlBSlZUUzg2Nm1iUlVURGxaYUVDc0MwbWFaeU5TMUE1ZHRkQUpBPT0=^|bfb04a28eb6ba3283834e9ba08907011e11e21b35c56541b9a5fcd6395445cda; _xsrf=83bac926-9c1b-4e12-a244-04e1450db218; q_c1=c6c98bbe46334902bc919ed05ea26bb7^|1712557872000^|1712557872000; SESSIONID=A4YquS6HbojBm0tU6fQQwq3v42IcslbVWfMzVXsOsUO; KLBRSID=d6f775bb0765885473b0cba3a5fa9c12^|1712557882^|1712557872; JOID=UFwcC0x3I29NEgmQD33AN6Go1P0TMBo3M2Jcq0YQSggOcDziV0agciERApwBQjwt4gYw_QYPh8eT9C-XEMjfOmE=; osd=VFwQAUxzI2NHEg2QA3fAM6Gk3v0XMBY9M2Zcp0wQTggCejzmV0qqciURDpYBRjwh6AY0_QoFh8OT-CWXFMjTMGE=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1711621241,1712143041,1712484654,1712557885; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1712557885; tst=h^",
            "pragma": "no-cache",
            "referer": "https://www.zhihu.com/hot",
            "^sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "x-api-version": "3.0.76",
            "x-requested-with": "fetch",
            "x-zse-93": "101_3_3.0",
            "x-zse-96": "2.0_PVlGjrRdqNgTlHdWNX/AVzvCKgwO37BWaFVqwZ/YDyistX8SYtPYV5lH9K05aRRm",
            "x-zst-81": "3_2.0aR_sn77yn6O92wOB8hPZnQr0EMYxc4f18wNBUgpTQ6nxERFZ8TY0-4Lm-h3_tufIwJS8gcxTgJS_AuPZNcXCTwxI78YxEM20s4PGDwN8gGcYAupMWufIeQuK7AFpS6O1vukyQ_R0rRnsyukMGvxBEqeCiRnxEL2ZZrxmDucmqhPXnXFMTAoTF6RhRuLPF4LCBveM8r3KqBOsOhxmBqOfk6UG2XVV9wgBMLwGQMH_avxfTB2LswVOeASTvLLmq9g13BXOVgOZLvHXiBemdvw0BJNqiGp_fhLO19HLCqe8rw3xOcNKRCS_3cXC9G3xQqNO8eLyBUOY8utV2AS9MeL_Ng9_9hYYwUHY8HHK6vV_9GpmOqfz5cSYVbVYx9cuYvgBgU2B_h9L6R283921WDNLxcCqt9SsD9SBpR2CJuX9FUeK39CC2JSm9u30yq2BPuwOuuC0iUUqqCLxEhe88MN9yu300D3_Q0HCWBHC"
        }
        self.url = "https://www.zhihu.com/api/v3/feed/topstory/hot-lists/total"
        self.params = {
            "limit": "50",
            "desktop": "true"
        }

    def req_data(self):
        response = requests.get(url=self.url, headers=self.headers, params=self.params)
        for info in response.json()['data']:
            item = {}
            item['title_area'] = info['target']['title_area']['text']
            item['link'] = info['target']['link']['url']
            item['metrics_area'] = info['target']['metrics_area']['text']
            item['excerpt_area'] = info['target']['excerpt_area']['text']
            self.collection.insert_one(item)


if __name__ == '__main__':
    zhihu = ZhiHu()
    zhihu.req_data()