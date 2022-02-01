from asyncio.windows_events import NULL
from pickle import TRUE
from socket import timeout
import threading
import time
from nbformat import write
import requests as rq
import pandas as pd
from bs4 import BeautifulSoup
from csv import DictWriter


file_header=['Pos', 'Game', 'Console', 'Publisher', 'VGChartz Score', 'Critic Score','User Score','Total Shipped',
    'Release Date','Last Update','Genre']

def a():
    page=6
    file_name="scrapData.csv"
    lost_data=[]
    with(open(file_name,'w')) as file1:
        DictWriter(file1,fieldnames=file_header).writeheader()

    for site in range(6,21):
        URL = "https://www.vgchartz.com/games/games.php?page="+str(site)+"&results=200"
        print(URL)
        r = rq.get(URL)
        
        soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
        all_1 = soup.find_all("div",{"id":"generalBody"})

        table = all_1[0].find("table")

        page=page+1
        count=0
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            if(columns != []):
                pos = columns[0].text.strip()
                game = columns[2].text.strip()
                console = columns[3].img['alt']
                publisher = columns[4].text.strip()
                vgscore = columns[5].text.strip()
                crscore = columns[6].text.strip()
                usscore = columns[7].text.strip()
                totalship = columns[8].text.strip()
                relDate = columns[9].text.strip()
                lastDate = columns[10].text.strip()
                
                print("general datacollected")
                
                link = columns[2].a['href']
                try:
                    time.sleep(4)
                    soup1 = BeautifulSoup(rq.get(link,timeout=90).content, 'html5lib')
                    d2 = soup1.find('h2',text="Genre").findNext('p').text.strip()
                    print("Genre Collected")
                except:
                    lost_data=link
                    print('Not able to get GENRE...')
                    d2 = "NULL"

                df = {'Pos':pos,'Game':game,'Console':console,'Publisher':publisher,'VGChartz Score':vgscore,
                'Critic Score':crscore,'User Score':usscore,'Total Shipped':totalship,'Release Date':relDate,'Last Update':lastDate,
                'Genre':d2}
                
                
                try:
                    with open(file_name, 'a', newline='',encoding="utf-8") as f_object:
                        dictwriter_object = DictWriter(f_object, fieldnames=file_header)
                        print("writing file....")
                        dictwriter_object.writerow(df)
                except:
                    print("...Not able to write data...of page -",page,"| count-",count)

                count=count+1
                
                print('page: ',page,' | count: ',count)

    with(open("lost_data1.txt",'w')) as ls_data:
        ls_data.write(lost_data)

def b():
    page=21
    file_name="scrapData_req2.csv"
    lost_data=[]
    with(open(file_name,'w')) as file1:
        DictWriter(file1,fieldnames=file_header).writeheader()

    for site in range(21,41):
        URL = "https://www.vgchartz.com/games/games.php?page="+str(site)+"&results=200"
        print(URL)
        r = rq.get(URL)
        
        soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
        all_1 = soup.find_all("div",{"id":"generalBody"})

        table = all_1[0].find("table")

        page=page+1
        count=0
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            if(columns != []):
                pos = columns[0].text.strip()
                game = columns[2].text.strip()
                console = columns[3].img['alt']
                publisher = columns[4].text.strip()
                vgscore = columns[5].text.strip()
                crscore = columns[6].text.strip()
                usscore = columns[7].text.strip()
                totalship = columns[8].text.strip()
                relDate = columns[9].text.strip()
                lastDate = columns[10].text.strip()
                
                print("general datacollected")
                
                link = columns[2].a['href']
                try:
                    time.sleep(4)
                    soup1 = BeautifulSoup(rq.get(link,timeout=90).content, 'html5lib')
                    d2 = soup1.find('h2',text="Genre").findNext('p').text.strip()
                    print("Genre Collected")
                except:
                    lost_data=link
                    print('Not able to get GENRE...')
                    d2 = "NULL"

                df = {'Pos':pos,'Game':game,'Console':console,'Publisher':publisher,'VGChartz Score':vgscore,
                'Critic Score':crscore,'User Score':usscore,'Total Shipped':totalship,'Release Date':relDate,'Last Update':lastDate,
                'Genre':d2}
                

                try:
                    with open(file_name, 'a', newline='',encoding="utf-8") as f_object:
                        dictwriter_object = DictWriter(f_object, fieldnames=file_header)
                        print("writing file....")
                        dictwriter_object.writerow(df)
                except:
                    print("...Not able to write data...of page -",page,"| count-",count)

                count=count+1
                
                print('page: ',page,' | count: ',count)

    with(open("lost_data2.txt",'w')) as ls_data:
        ls_data.write(lost_data)

def c():
    page=41
    file_name="scrapData_req3.csv"
    lost_data=[]
    with(open(file_name,'w')) as file1:
        DictWriter(file1,fieldnames=file_header).writeheader()

    for site in range(41,61):
        URL = "https://www.vgchartz.com/games/games.php?page="+str(site)+"&results=200"
        print(URL)
        r = rq.get(URL)
        
        soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
        all_1 = soup.find_all("div",{"id":"generalBody"})

        table = all_1[0].find("table")

        page=page+1
        count=0
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            if(columns != []):
                pos = columns[0].text.strip()
                game = columns[2].text.strip()
                console = columns[3].img['alt']
                publisher = columns[4].text.strip()
                vgscore = columns[5].text.strip()
                crscore = columns[6].text.strip()
                usscore = columns[7].text.strip()
                totalship = columns[8].text.strip()
                relDate = columns[9].text.strip()
                lastDate = columns[10].text.strip()
                
                print("general datacollected")
                
                link = columns[2].a['href']
                try:
                    time.sleep(4)
                    soup1 = BeautifulSoup(rq.get(link,timeout=90).content, 'html5lib')
                    d2 = soup1.find('h2',text="Genre").findNext('p').text.strip()
                    print("Genre Collected")
                except:
                    lost_data=link
                    print('Not able to get GENRE...')
                    d2 = "NULL"

                df = {'Pos':pos,'Game':game,'Console':console,'Publisher':publisher,'VGChartz Score':vgscore,
                'Critic Score':crscore,'User Score':usscore,'Total Shipped':totalship,'Release Date':relDate,'Last Update':lastDate,
                'Genre':d2}
                
                try:
                    with open(file_name, 'a', newline='',encoding="utf-8") as f_object:
                        dictwriter_object = DictWriter(f_object, fieldnames=file_header)
                        print("writing file....")
                        dictwriter_object.writerow(df)
                except:
                    print("...Not able to write data...of page -",page,"| count-",count)

                count=count+1
                
                print('page: ',page,' | count: ',count)

    with(open("lost_data3.txt",'w')) as ls_data:
        ls_data.write(lost_data)

def d():
    page=61
    file_name="scrapData_req4.csv"
    lost_data=[]
    with(open(file_name,'w')) as file1:
        DictWriter(file1,fieldnames=file_header).writeheader()

    for site in range(61,101):
        URL = "https://www.vgchartz.com/games/games.php?page="+str(site)+"&results=200"
        print(URL)
        r = rq.get(URL)
        
        soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
        all_1 = soup.find_all("div",{"id":"generalBody"})

        table = all_1[0].find("table")

        page=page+1
        count=0
        for row in table.find_all('tr'):
            columns = row.find_all('td')
            if(columns != []):
                pos = columns[0].text.strip()
                game = columns[2].text.strip()
                console = columns[3].img['alt']
                publisher = columns[4].text.strip()
                vgscore = columns[5].text.strip()
                crscore = columns[6].text.strip()
                usscore = columns[7].text.strip()
                totalship = columns[8].text.strip()
                relDate = columns[9].text.strip()
                lastDate = columns[10].text.strip()
                
                print("general datacollected")
                
                link = columns[2].a['href']
                try:
                    time.sleep(4)
                    soup1 = BeautifulSoup(rq.get(link,timeout=90).content, 'html5lib')
                    d2 = soup1.find('h2',text="Genre").findNext('p').text.strip()
                except:
                    lost_data=link
                    print('Not able to get GENRE...')
                    d2 = "NULL"

                df = {'Pos':pos,'Game':game,'Console':console,'Publisher':publisher,'VGChartz Score':vgscore,
                'Critic Score':crscore,'User Score':usscore,'Total Shipped':totalship,'Release Date':relDate,'Last Update':lastDate,
                'Genre':d2}
                
                try:
                    with open(file_name, 'a', newline='',encoding="utf-8") as f_object:
                        dictwriter_object = DictWriter(f_object, fieldnames=file_header)
                        print("writing file....")
                        dictwriter_object.writerow(df)
                except:
                    print("...Not able to write data...of page -",page,"| count-",count)

                count=count+1
                
                print('page: ',page,' | count: ',count)

    with(open("lost_data4.txt",'w')) as ls_data:
        ls_data.write(lost_data)

threading.Thread(target=a).start()
threading.Thread(target=b).start()
threading.Thread(target=c).start()
threading.Thread(target=d).start()