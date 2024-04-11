import requests
import execjs
import time
import random
from datetime import datetime



class QQmusic:
    def __init__(self):
        self.file_client = execjs.compile(open("./webcode.js","r",encoding="utf-8").read())
        self.url = "https://u6.y.qq.com/cgi-bin/musics.fcg"
        self.headers = {
            "authority": "u6.y.qq.com",
            "accept": "application/json",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "no-cache",
            "content-type": "application/x-www-form-urlencoded",
            "origin": "https://y.qq.com",
            "pragma": "no-cache",
            "referer": "https://y.qq.com/",
            "^sec-ch-ua": "^\\^Chromium^^;v=^\\^122^^, ^\\^Not(A:Brand^^;v=^\\^24^^, ^\\^Google",
            "sec-ch-ua-mobile": "?0",
            "^sec-ch-ua-platform": "^\\^Windows^^^",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        }
        self.cookie = {
            "RK": "gt9ttxV8Pp",
            "ptcz": "a6ff7bfae91ca621472979101f7be3d43181e11f38c257c74e95e3694346c914",
            "pgv_pvid": "6374203785",
            "eas_sid": "11W6F9F7h0l8c5C0Y208W4t3R4",
            "_clck": "qpl70v|1|fgo|0",
            "_qimei_uuid42": "1831414311c10069f762d318cdb6beb0b53f336f73",
            "_qimei_fingerprint": "0eb0a5e792ff80d549ee2a9be85c144b",
            "fqm_pvqid": "e482da75-17bb-4808-beee-7fda039c3dfc",
            "fqm_sessionid": "e21c9b97-184a-4053-88cb-6dc6cb4063d0",
            "pgv_info": "ssid=s6548797235",
            "ts_uid": "2494508386",
            "_qpsvr_localtk": "0.3115647655283831",
            "login_type": "1",
            "psrf_musickey_createtime": "1712741649",
            "euin": "ow6iNe4z7evqNn**",
            "tmeLoginType": "2",
            "psrf_qqopenid": "3D0D20D9B30B15FA5B965A02CE893817",
            "psrf_access_token_expiresAt": "1720517649",
            "qqmusic_key": "Q_H_L_63k3NWM-QgOldgXMQG3hVnmzokv9nl3fa6zDtTzJgqzGLQ-5O42Yh1UAI1BrY-EQfmYDlOYLN_w",
            "psrf_qqaccess_token": "E76497858E444039E024AC114E9FCEBD",
            "music_ignore_pskey": "202306271436Hn@vBj",
            "uin": "2138504498",
            "wxrefresh_token": "",
            "psrf_qqunionid": "716FCFFCE6FF5DD15C0B3BDA124CBA45",
            "psrf_qqrefresh_token": "D66E4D15DAE5E36FCF5BEF3A6191341B",
            "wxopenid": "",
            "qm_keyst": "Q_H_L_63k3NWM-QgOldgXMQG3hVnmzokv9nl3fa6zDtTzJgqzGLQ-5O42Yh1UAI1BrY-EQfmYDlOYLN_w",
            "wxunionid": "",
            "ts_last": "y.qq.com/n/ryqq/search"
        }

    def get_name(self,star_name,page,page_size):
        data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":2138504498,"g_tk_new_20200303":205436222,"g_tk":205436222},"req_1":{"method":"DoSearchForQQMusicDesktop","module":"music.search.SearchCgiService","param":{"remoteplace":"txt.yqq.top","searchid":"70193178873454621","search_type":0,"query":"'+star_name+'","page_num":'+str(page)+',"num_per_page":'+str(page_size)+'}}}'
        js_code = self.file_client.call("main",data)
        params = {
            "_": str(int(time.time()*1000)),
            "sign": js_code
        }
        response = requests.post(url=self.url,headers=self.headers,cookies=self.cookie,data=data.encode(),params=params)
        for num,info in enumerate(response.json()['req_1']['data']['body']['song']['list']):
            item = {}
            item['title'] = info['title']
            print("序号 ： "+str(num+1)+"    歌曲名 ： "+info['title'])
        return response.json()['req_1']['data']['body']['song']['list']

    def get_music(self,music_info):
        data = '{"comm":{"cv":4747474,"ct":24,"format":"json","inCharset":"utf-8","outCharset":"utf-8","notice":0,"platform":"yqq.json","needNewCode":1,"uin":2138504498,"g_tk_new_20200303":205436222,"g_tk":205436222},"req_1":{"module":"music.musichallSong.PlayLyricInfo","method":"GetPlayLyricInfo","param":{"songMID":"'+music_info['mid']+'","songID":'+str(music_info['id'])+'}},"req_2":{"method":"GetCommentCount","module":"music.globalComment.GlobalCommentRead","param":{"request_list":[{"biz_type":1,"biz_id":"'+str(music_info['id'])+'","biz_sub_type":0}]}},"req_3":{"module":"music.musichallAlbum.AlbumInfoServer","method":"GetAlbumDetail","param":{"albumMid":"'+music_info['album']['mid']+'"}},"req_4":{"module":"vkey.GetVkeyServer","method":"CgiGetVkey","param":{"guid":"'+str(int(round(2147483647 * random.random()) * datetime.utcnow().microsecond // 1000 % 1e10))+'","songmid":["'+music_info['mid']+'"],"songtype":[0],"uin":"2138504498","loginflag":1,"platform":"20","filename":["RS02'+music_info['vs'][0]+'.mp3"]}}}'
        js_code = self.file_client.call("main",data)
        params = {
            "_": str(int(time.time() * 1000)),
            "sign": js_code
        }
        response = requests.post(url=self.url,headers=self.headers,cookies=self.cookie,data=data.encode(),params=params)
        music_url = "https://ws6.stream.qqmusic.qq.com/"+response.json()['req_4']['data']['midurlinfo'][0]['purl']
        print(music_url)
        return music_url,music_info['name']

    def save_music(self,url,name):
        response = requests.get(url)
        if response.status_code == 200:
            with open("./music/"+name+".mp3", 'wb') as f:
                f.write(response.content)
            print("歌曲已保存为:", "./music/"+name+".mp3")
        else:
            print("下载失败")
        pass

    def main(self,star_name,page,bool):
        if bool:
            list_song = self.get_name(star_name,page,60)
            num = int(input("选择歌曲序号 ： ————————>  "))
            music_url,name = self.get_music(list_song[num])
            self.save_music(music_url,name)
        else:
            list_song = self.get_name(star_name, page, 60)
            for num in range(60):
                music_url, name = self.get_music(list_song[num])
                self.save_music(music_url, name)


# 爬取指定一首
# if __name__ == '__main__':
#     star_name = input("输入歌手名：")
#     page = int(input("请输入页数 ： ")) + 1
#     qq = QQmusic()
#     qq.main(star_name,page,True)

# 爬取这个人全部
if __name__ == '__main__':
    star_name = input("输入歌手名：")
    qq = QQmusic()
    for page in range(100):
        qq.main(star_name,page,False)