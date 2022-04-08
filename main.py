import requests
from PIL import Image
from io import BytesIO
    
if __name__ == '__main__':
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
    }
    start_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=2"
    response1 = requests.get(start_url, headers=headers, timeout=5)
    url = "https://www.bing.com" + response1.json()['images'][0]['urlbase'] + "_UHD.jpg"
    file_name = response1.json()['images'][1]['title']
    response2 = requests.get(url, headers=headers, timeout=5)
    image = Image.open(BytesIO(response2.content))
    image.save('./{}.jpg'.format(file_name))
    print(file_name)
