# WebScrapping Game data
This project is for scrapping data of website containing the data of number of games 

# Libraries used:
<li>import threading</li>
<li>import time</li>
<li>import requests as rq</li>
<li>import pandas as pd</li>
<li>from bs4 import BeautifulSoup</li>
<li>from csv import DictWriter</li>

# Brief
MultiThreading is used to fetch the data simultaneously from multiple range of pages and load the data to csv file format.<br>
BeautifulSoup is used to fetch the required data in form of columns for the headers. <br>
Headers are loaded in the csv file in the very begining in LIST format <br>
Data is being saved in Dictionary format and appended continuously in the csv file<br>
Encoding utf-8 is used to write the file so that character fromat error can be handled.<br>
