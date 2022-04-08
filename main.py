import requests
from PIL import Image
from io import BytesIO
    
if __name__ == '__main__':
    start_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
    response1 = requests.get(start_url)
    url = "https://www.bing.com" + response1.json()['images'][0]['urlbase'] + "_UHD.jpg"
    filename = response1.json()['images'][0]['copyright'].split(' ')[0]
    response2 = requests.get(url)
    image = Image.open(BytesIO(response2.content))
    image.save('./{}.jpg'.format(filename))
    
    
    
    
