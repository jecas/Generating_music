#jednostavan python skript za download kompozicija

#!pip install bs4
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import time

#definisemo direktorijum u kojem cemo sacuvati kompozicije
save_dir = './guitar/'

#definisemo url komponente
url0 = 'https://www.mutopiaproject.org/cgibin/make-table.cgi?startat='
url1 = '&searchingfor=&Composer=&Instrument=Guitar&Style=&collection=&id=&solo=&recent=&timelength=&timeunit=&lilyversion=&preview='

#incijalizacija
songNumber = 0
i = 0

#pronalazimo i download-ujemo sve midi fajlove
while i < 380:
    #spajamo putanju
    url = url0 + str(songNumber) + url1
    html = urlopen(url)
    #parsiramo html
    soup = BeautifulSoup(html.read())
    #pronalazimo sve linkove
    links = soup.find_all('a')
    
    for link in links:
        href = link['href']
        
        #ako link sadrzi .mid
        if href.find('.mid') >= 0:
            #download-ujemo ga
            urlretrieve(href, 'guitar'+str(i)+'.mid')
            i += 1
    
    #na svakoj stranici se nalazi po 10 kompozicija
    songNumber += 10 