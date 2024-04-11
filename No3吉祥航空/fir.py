import requests
import json

session = requests.session()
headers = {
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Origin": "https://www.juneyaoair.com",
    "Pragma": "no-cache",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "accept": "application/json, text/plain, */*",
    "blackbox": "lWPSf17124897580aLfrMSHSJ7",
    "channelno": "B2C",
    "clientversion": "1.0.0",
    "content-type": "application/json;charset=utf-8",
    "sec-ch-ua-mobile": "?0",
    "versioncode": "10000"
}
data = {
    'channelNo':"B2C",
    'data':{
        'arrCity':"",
        'arrCode':"SHA",
        'depCode':"BJS",
        'depDate':"2024-04-07",
        'flightType':"OW",
        'loading':'false',
        'returnDate':"2024-04-12",
        'sendCity':""
    }
}
cookie = {
    "9AD585D8A7CB034A": "LJ2rL4WM-1712489406292-c0417836af1b4-1603595416",
    "Hm_lvt_f1c672edeacdaef6cb2e00251b466246": "1712489695",
    "Hm_lpvt_f1c672edeacdaef6cb2e00251b466246": "1712489743",
    ".uscka": "8d8030bce2a8e09de72de84e4a6944cc",
    ".usinfo": "3JFzqovf%2bBZAWWwq7SITDUXsTRl6StZFzNZesogynNLZTjAs3IGxLAvsmtWMPqyde5Csu%2bACWJAv3UmMCZM8fQ%3d%3d",
    "1735D64331DF397E": "xAohtUwcC6FqI2fvEnapEz1z3dS919pUinAbheBvwiwwy%2Bvmi7CQtrfyNTsRZbXdMWGBnfagOvXqsLtkuRryGw%3D%3D",
    "_xid": "%2BXLozEG%2B3%2B680%2BHjeLukvdjvXkQo7fr%2F1VUcOW3yOr8%3D"
}
params = {
    'channelNo':"B2C",
    'data':{
        'ArrCity':"SHA",
        'BackFlightDate':"",
        'DepCity':"BJS",
        'EndFlightDate':"2024-10-07",
        'GoFlightDate':"",
        'RouteType':"OW",
        'StartFlightDate':"2024-04-07",
        'loading':'false'
    }
}
# session.post("https://www.juneyaoair.com/server/Page/flight/cfcModule", headers=headers, cookies=cookie, json=data)
response = requests.post("https://www.juneyaoair.com/api/flightFares/queryLowPriceInfo",headers=headers,cookies=cookie,json=params)
response.encoding = response.apparent_encoding
print(response.text)
print(response)