import requests
import time
import re
import json


class JuneYaoAir:
    def __init__(self):
        self.citycode = {}
        self.headers = {
            "Origin": "https://www.juneyaoair.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
            "blackbox": "lWPSf17124897580aLfrMSHSJ7",
        }
        self.url = "https://www.juneyaoair.com/api/flightFares/queryFlightSimple"
        self.data = {
            'channelNo':"B2C",
            'data':{
                'ArrDateTimeGo':"",
                'BrandCodeGo':"",
                'CabinClassGo':"",
                'FlightDirection':"G",
                'FlightNos':"",
                'IsTransferGo':"N",
                'PassengerType':[],
                'RouteType':"OW",
                'SegCondList':[{
                            'ArrCity':"",
                            'DepCity':"",
                            'FlightDate':"",
                            'FlightDirection':"G",
                            'SegNO':0}]
            },
        }
        self.cookies = {
            "9AD585D8A7CB034A": "LJ2rL4WM-1712489406292-c0417836af1b4-1603595416",
            "Hm_lvt_f1c672edeacdaef6cb2e00251b466246": "1712489695",
            "Hm_lpvt_f1c672edeacdaef6cb2e00251b466246": "1712489743",
            ".uscka": "8d8030bce2a8e09de72de84e4a6944cc",
            ".usinfo": "3JFzqovf%2bBZAWWwq7SITDUXsTRl6StZFzNZesogynNLZTjAs3IGxLAvsmtWMPqyde5Csu%2bACWJAv3UmMCZM8fQ%3d%3d",
            "1735D64331DF397E": "xAohtUwcC6FqI2fvEnapEz1z3dS919pUinAbheBvwiwwy%2Bvmi7CQtrfyNTsRZbXdMWGBnfagOvXqsLtkuRryGw%3D%3D",
            "_xid": "%2BXLozEG%2B3%2B680%2BHjeLukvdjvXkQo7fr%2F1VUcOW3yOr8%3D"
        }

    def get_citycode(self):
        params = {
            "v":int(time.time()*1000),
        }
        response = requests.get(url="https://mediaws.juneyaoair.com/upload/flightBasicStatic/airport.js",headers=self.headers,data=params)
        list_info = json.loads(re.findall("var __cityAirportInfo = (.*)",response.text)[0])['objData']
        for info in list_info:
            self.citycode[info['cityName']] = info['cityCode']

    def req_data(self,ArrCity,DepCity,FlightDate):
        self.data['data']['SegCondList'][0]['ArrCity'] = ArrCity
        self.data['data']['SegCondList'][0]['DepCity'] = DepCity
        self.data['data']['SegCondList'][0]['FlightDate'] = FlightDate
        response = requests.post(self.url, headers=self.headers, cookies=self.cookies, json=self.data)
        response.encoding = response.apparent_encoding
        if "data" in response.json():
            for info in response.json()['data']['FlightInfoCombList']:
                print(info['FlightInfoList'][0]['FlightNo'],info['FlightInfoList'][0]['AircraftModel'],info['FlightInfoList'][0]['DepDateTime'],info['FlightInfoList'][0]['ArrDateTime'],info['FlightInfoList'][0]['LowestValueEconomy'],info['FlightInfoList'][0]['LowestValueFirst'])
        else:
            print("两地无飞机")

    @staticmethod
    def validate_date_format(date_string):
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
        if re.match(date_pattern, date_string):
            return False
        else:
            return True

    def main(self,ArrCity,DepCity,FlightDate):
        self.get_citycode()
        if ArrCity not in self.citycode or DepCity not in self.citycode or self.validate_date_format(FlightDate):
            print("这地方没有我家飞机 或 日期格式错误 哟~~")
        else:
            self.req_data(self.citycode[ArrCity],self.citycode[DepCity],FlightDate)



if __name__ == '__main__':
    juneyaoair = JuneYaoAir()
    # juneyaoair.get_citycode()
    ArrCity = input("请输入 初始台地 ：")
    DepCity = input("请输入 终焉之地 ：")
    FlightDate = input("请输入 飞翔之日 ：")
    juneyaoair.main(ArrCity, DepCity,FlightDate)