import requests 
from bs4 import BeautifulSoup
import re
#import html5lib
#import os.path

def code(x):
    return x.encode('ascii','ignore').decode('utf8')


def incometax_data():
    r = requests.get('https://www.incometaxindia.gov.in/News/Forms/AllItems.aspx')
    
    res = BeautifulSoup(r.text,'html')
    
    r1 = str(res.find_all('div',{'id':"WebPartWPQ2"}))
    
    xs = r1.split('<input class="s4-itm-cbx" type="checkbox"/></td><td class="ms-vb-icon">')
    
    p1 = re.compile(r'title=\"(.*?)\"')
    p2 = re.compile(r'<a href=\"(.*?)\"')
    p3 = re.compile(r'<nobr>(.*?)<\/nobr>')
    p4 = re.compile(r'<div class="ms-rtestate-field" dir="">(.*?)<\/div>')
    
    data =[]
    for x in xs[1:]:
        data.append((code(p1.findall(x)[0]),code(p2.findall(x)[0]),code(p3.findall(x)[0]),code(p4.findall(x)[0])))
    
    return(data)

