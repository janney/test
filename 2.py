from urllib.request import urlopen,urlretrieve
from bs4 import BeautifulSoup
import re
import os,stat

baseUrl = "http://nexus.bsdn.org/content/groups/public/antlr/antlr/"

def getLinks(NewUrl):
    # print("网址："+NewUrl)
    html = urlopen(NewUrl)
    ContentType = html.headers['Content-Type']
    # print("The Content Type is "+ContentType)
    if "text/html" in ContentType:
        # print("welcome")
        bsObj = BeautifulSoup(html,"html.parser",from_encoding="utf-8")
        links = bsObj.findAll("a")
        if links:
            for link in links:
                if 'href' in link.attrs:
                    a = link.attrs['href']
                    if a == '../':
                        print("ParentUrl:"+a)
                        continue
                    else:
                        print("This is Url:"+a)
                        links = getLinks(a)
    else:
        print("The End Url is "+NewUrl)
        path = NewUrl.replace("http://nexus.bsdn.org/content/groups/public/","")
        directory = re.split('/',path)
        DirectoryName = "downloaded"
        for index in range(len(directory)-1):
            DirectoryName = DirectoryName + "\\" + directory[index]
        fileDirectory = os.path.abspath(DirectoryName)
        if not os.path.exists(fileDirectory):
            os.makedirs(fileDirectory)
        new_file = fileDirectory+"\\"+ directory[-1]
        if not os.path.exists(new_file):
            urlretrieve(NewUrl,new_file)    

getLinks(baseUrl)