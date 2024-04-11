import scrapy
from scrapy import cmdline
from scrapy.http import HtmlResponse,FormRequest,JsonRequest
import json
import random
from 逆向练习.考核.No1某品牌数据采集.myScrapy.myScrapy.items import MyscrapyItem


class ShangSpider(scrapy.Spider):
    name = 'winshang'
    allowed_domains = ['winshangdata.com']
    start_urls = ['http://www.winshangdata.com/brandList']
    cookies = {
        "_uab_collina": "171141832816562841571871",
        "Hm_lvt_f48055ef4cefec1b8213086004a7b78d": "1711418329",
        "JSESSIONID": "6E1D3888924C8D88317A1C2E370B9F6A",
        "Hm_lpvt_f48055ef4cefec1b8213086004a7b78d": "1711418455"
    }

    def start_requests(self):
        url = 'http://www.winshangdata.com/wsapi/brand/getBigdataList3_4'
        title_list = ['餐饮','儿童亲子','文体娱','零售','生活服务','其他类型']
        # title_list = ['餐饮']
        for title in title_list:
            for page in range(1, 15):
                data = {
                    "isHaveLink": "",
                    "isTuozhan": "",
                    "isXxPp": "",
                    "kdfs": "",
                    "key": "",
                    "orderBy": "1",
                    "pageNum": page,
                    "pageSize": 60,
                    "pid": "",
                    "qy_p": "",
                    "qy_r": "",
                    "xqMj": "",
                    "ytlb1": title,
                    "ytlb2": ""
                }
                yield scrapy.Request(url=url, body=json.dumps(data, separators=(',', ':')), callback=self.brandId_parse,cookies=self.cookies, method="POST")

    def parse(self, response, **kwargs):
        pass

    def brandId_parse(self, response, **kwargs):
        for data in response.json()['data']['list']:
            brandId = data['brandId']
            print(f"http://www.winshangdata.com/brandDetail?brandId={brandId}")
            yield scrapy.Request(url=f"http://www.winshangdata.com/brandDetail?brandId={brandId}",cookies=self.cookies,method="GET",callback=self.item_parse)

    def item_parse(self, response, **kwargs):
        item = MyscrapyItem()
        item['_id'] = response.xpath("//div[@class='tit-name']/div/div/text()").get()+ str(random.randint(1,1000))
        item['title'] = response.xpath("//div[@class='el-col el-col-17']/div[1]/text()").get()
        item['ceate_time'] = response.xpath("//div[@class='fl w-p-50 detail-info']/ul/li[1]/span[2]/text()").get()
        item['Way'] = response.xpath("//div[@class='fl w-p-50 detail-info']/ul/li[3]/span[2]/text()").get()
        item['term_cooperation'] = response.xpath("//div[@class='fl w-p-50 detail-info']/ul/li[4]/span[2]/text()").get()
        item['area_req'] = response.xpath("//div[@class='fl w-p-50 detail-info']/ul/li[5]/span[2]/text()").get()
        yield item


if __name__ == '__main__':
    cmdline.execute("scrapy crawl winshang".split())
