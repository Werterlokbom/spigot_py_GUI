import mcpi.minecraft as minecraft
from PIL import Image, ImageQt
from gui import mainwin
import urllib
import urllib.request
import urllib.parse
import re
import time
import random
import gui.kehuduan_rc

head = {
    ':Authority' : 'o.xbottle.top' ,
    ':Method' : 'GET' ,
    ':Path' : '/bottleskin/process.php?nid=Flepis00&method=zb' ,
    ':Scheme' : 'https' ,
    'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' ,
    'Accept-Encoding' : 'gzip, deflate, br' ,
    'Accept-Language' : 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6' ,
    'Referer' : 'https://o.xbottle.top/bottleskin/' ,
    'Sec-Ch-Ua' : '''"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"''' ,
    'Sec-Ch-Ua-Mobile' : '?0' ,
    'Sec-Ch-Ua-Platform' : "Windows", 
    'Sec-Fetch-Dest' : 'iframe' ,
    'Sec-Fetch-Mode' : 'navigate' ,
    'Sec-Fetch-Site' : 'same-origin',
    'Sec-Fetch-User' : '?1' ,
    'Upgrade-Insecure-Requests' : '1' ,
    'User-Agent' : '''Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43''' ,
}

getter_url = "https://o.xbottle.top/bottleskin/process.php?nid={name}&method={mode}"

class PlayerAvatarGetter:
    '''获得玩家的头像'''
    def __init__(self, player_id : str, mode: str) -> None:
        self.send_url = getter_url
        self._player_id = player_id
        self._mode = mode
        self.icon = self.getter_icon(player_id=player_id,mode=mode)
    
    def load_str(self, html: str) -> str:
        '''获取目标玩家的皮肤文件url'''
        return re.search(r'http://textures.minecraft.net/texture/[\w]*', html).group(0)
    
    def getter_icon(self, player_id: str, mode: str) -> bytes:
        '''获取玩家头像'''
        icon = None
        times = 1
        steve = open('./skin/steve.png', 'rb')
        alex = open('./skin/alex.png', 'rb')
        g = [steve, alex]
        if mode == 'zb':
            #超时检测
            while icon == None:
                try:    
                    html = urllib.request.urlopen(getter_url.format(name=player_id, mode=mode))
                    loaded_str = self.load_str(urllib.parse.unquote(html.read()))
                    icon = urllib.request.urlopen(loaded_str)

                except TimeoutError:
                    time.sleep(1.0)
                    times += 1
                    if times == 3:
                        return Image.open(random.choice(g))
                
                pic = Image.open(icon)
                pic = pic.crop((7,8,17,16))
        
        else: 
            #非正版玩家
            pic = Image.open(random.choice(g))          
        
        return ImageQt.ImageQt(pic)

#测试
# l = PlayerIcoGetter(player_id='Flepis00', mode='zb')
# print(l.icon)

class Main:
    def __init__(self, main_win=mainwin.MainWindow, **kargs):
        self.window = main_win(**kargs)
    
    def start(self):
        self.window.start_win()

if __name__ == '__main__':
    
    b = Main(icon=None)
    b.start()
    
    
