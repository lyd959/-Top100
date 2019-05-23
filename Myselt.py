import requests
from  lxml import etree

#数据获取
def get_one_page(url):
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    return None

#数据存入Excel文件内
# def withinexcel():
#     with open() in

#获取html中有用信息
def findAllTips(html):
    a=[]
    r=etree.HTML(html)
    theme=r.xpath("//*[@class='movie-item-info']/p[@class='name']/a/text()")
    actor=r.xpath("//*[@class='movie-item-info']/p[@class='star']/text()")
    time=r.xpath("//*[@class='movie-item-info']/p[@class='releasetime']/text()")
    imgurl=r.xpath("//*[@class='image-link']/img[1]/@src")
    return theme,actor,time,imgurl
def main():
    num=0
    for offset in range(0,100,10):
        url='https://maoyan.com/board/4?offset='+str(offset)
        html=get_one_page(url)
        #print(html)
        theme,actor,time,imgurl=findAllTips(html)
        for i in range(0,len(theme)):
            print(theme[i],actor[i],time[i],imgurl[i])

main()