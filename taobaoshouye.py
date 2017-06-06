# -*- coding: utf-8 -*-
"""
Created on Thu May 11 19:31:25 2017

@author: rogue
"""

from bs4 import BeautifulSoup
def tecent(url):
    response=urllib.request.urlopen(url)
    html=response.read()
    data=html.decode("utf-8")  #转换编码，默认转换为utf-8
    soup=BeautifulSoup(data,"html5lib")
    for list in soup.find_all("a"):
        if list.string==None:
            continue
        else:
            print(type(list.string))
            print(list.string)   #暂时无法将NavigableString类型进行转换，此例子暂时在控制台输出
            # with open("taobao1.txt","ab") as f:
            #     f.write(list.string)

if __name__=="__main__":
    url="https://www.taobao.com/"
    tecent(url)