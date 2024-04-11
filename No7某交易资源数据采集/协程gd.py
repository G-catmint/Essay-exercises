import aiohttp
import asyncio
import aiofiles
import execjs


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
            "X-Dgi-Req-Timestamp": '',
            "^sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^"
        }
        self.url = "https://ygp.gdzwfw.gov.cn/ggzy-portal/search/v2/items"

    async def post_data(self,url, data):
        proxy_ip = "://127.0.0.1:7890"
        proxies = {
            "http":"http"+proxy_ip,
            "https":"https"+proxy_ip
        }
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(url, json=data,proxy=proxies["http"] or proxies['https']) as response:
                return await response.json(content_type=None)
    async def get_data(self,page):
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
        async with aiofiles.open("./test.js", "r", encoding="utf-8") as f:
            js_code = await f.read()
        jscode = execjs.compile(js_code).call("main",data)
        self.headers['X-Dgi-Req-Timestamp'] = str(jscode[1])
        self.headers['X-Dgi-Req-Nonce'] = jscode[2]
        self.headers["X-Dgi-Req-Signature"] = jscode[0]
        result = await self.post_data(self.url, data)
        print("---------------------"+str(page)+"-------------------------")
        print(result)
        for info in result['data']['pageData']:
            item = {}
            item['noticeTitle'] = info['noticeTitle']
            item['publishDate'] = info['publishDate']
            print(item)

    async def main(self):
        task = [asyncio.create_task(self.get_data(page))for page in range(1,1000)]
        await asyncio.wait(task)


if __name__ == "__main__":
    gov = Gov()
    asyncio.run(gov.main())
