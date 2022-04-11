import requests
from PIL import Image
from io import BytesIO
import os
    
if __name__ == '__main__':
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    # start_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8"
    start_url = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&mkt=zh-cn"
    response1 = requests.get(start_url, headers=headers, timeout=3)
    num = len(response1.json()['images'])
    for i in range(num):
        url = "https://www.bing.com" + response1.json()['images'][i]['urlbase'] + "_UHD.jpg"
        filename = response1.json()['images'][i]['copyright'].split('(')[0].strip()
        rootpath = './img/'
        if os.path.exists(rootpath) == False:
            os.mkdir(rootpath)
        filepath = rootpath + filename + '.jpg'
        if os.path.exists(filepath):
            continue
        response2 = requests.get(url, headers=headers, timeout=3)
        image = Image.open(BytesIO(response2.content))
        image.save(filepath)
        print(filepath)
