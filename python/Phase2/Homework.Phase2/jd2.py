#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#京东商品信息爬虫  
#爬取京东商品信息并保存到csv格式文件中  参考答案
#2017-7-23  
  
  
import os  
import requests  
import csv  
from bs4 import BeautifulSoup  
from fake_useragent import UserAgent
  
#获取url请求  
def gethtml(kind,page):  
    #'''''获取url请求'''  
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko)"}
    pagenum = str(2 * page)  
    try:  
        r = requests.get('https://search.jd.com/Search?keyword=' + kind + '&enc=utf-8&page=' + pagenum, headers=header)#链接url  
        r.raise_for_status() 
        r.encoding = r.apparent_encoding#转码  
        print('爬取第{}页：'.format(page))  
        #print(r.text)
        return r.text#返回html  
    except:  
        print('链接异常！！！')  
        return ''  
  
#获取定位资源  
def findhtml(html,httplist):  
    #"""寻找资源"""  
    soup = BeautifulSoup(html,'lxml')  
    links = soup.find_all('div', class_='gl-i-wrap')#寻找'div'标签  
    print(len(links))
    for link in links:  
        ui = []  
        namediv = link.find('div', class_='p-name p-name-type-2')#寻找商品名称和链接  
        title = namediv.a['title'] 
        ui.append(title)#名称加入到ui中  

        href = namediv.a['href']  
        if 'https:' not in href:#添加链接  
            ui.append('https:' + href)  
        else:  
            ui.append(href) 

        pricediv = link.find('div', class_='p-price')#寻找商品价格  
        try:  
            price =  pricediv.strong.i.text 
            ui.append(price)#价格加入到ui中  
        except:  
            ui.append('')  
        
        aggressmentdiv = link.find('div', class_='p-commit')#寻找评论 
        commit = aggressmentdiv.strong.a['href']  
        ui.append(commit)#评论链接添加到ui中  


        icondiv = link.find('div', class_='p-icons') #寻找赠品标志
        #print(icondiv.text)

        '''
        #method 1
        if '赠' in icondiv.text:
            ui.append('有')
        else:
            ui.append('无')
        '''
        
        '''
        #method 2
        gift = '无'
        infolist = icondiv.find_all('i', class_='goods-icons4 J-picon-tips')
        print(len(infolist))
        if len(infolist) > 0:
            for info in infolist:
                if info.text == '赠':
                    gift = '有'
                    break
        ui.append(gift)
        '''
 

        #method 3
        gift = icondiv.find('i', attrs={'data-tips':'购买本商品送赠品'})

        if gift != None:
            ui.append('有')
        else:
            ui.append('无')

        
        httplist.append(ui)  
  
  
#保存资源  
def savehtml(goods, ul):  
    #path = 'D:/数据/'  
    #if not os.path.exists(path):  
    #    os.mkdir(path)#创建一个文件  
    with open(goods + '.csv','w+') as f:  
        writer = csv.writer(f)  
        writer.writerow(['商品','链接','价格','评价','赠品'])  
        for u in range(len(ul)):  
            if ul[u]:  
                writer.writerow([ul[u][0],ul[u][1],ul[u][2],ul[u][3], ul[u][4]])
                
  
  
#程序主体  
if __name__ == '__main__':  
    goods = input('请输入要搜索的物品：')  
    yeshu = int(input('请输入要查询到的页数:'))  
    ulist = []  
    for i in range(yeshu+1):  
        try:  
            if i != 0:  
                text = gethtml(goods,i)  
                findhtml(text , ulist)  
            savehtml(goods , ulist)  
        except:  
            break  