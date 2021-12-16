from bs4.dammit import html_meta
import requests
from bs4 import BeautifulSoup

URL = "https://www.adkami.com/agenda"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

def scrapAgenda():
    jourDict = { "Lundi":[], "Mardi":[], "Mercredi":[], "Jeudi":[], "Vendredi":[], "Samedi":[], "Dimanche":[]}
    colone = soup.find_all('div', class_="colone")
    for jour in colone:
        titleList = []
        epsList = []
        horaireList = []
        journee = jour.h3.text.strip()
        if journee == "Lundi" or journee == "Mardi" or journee == "Mercredi":
            for a in jour.find_all('a',):
                for info in a.select('div[class*="col-12 episode"]'):
                    horaire = info.span.text.strip()
                    horaireList.append(horaire)
                    for epis in info.find_all('div', class_="info"):
                        episode = epis.find('p', class_="epis").text.strip()
                        epsList.append(episode)
                        titre = epis.find('p', class_="title").text.strip()
                        titleList.append(titre)                    
        else:
            for info in jour.select('div[class*="col-12 episode"]'):
                horaire = info.span.text.strip()
                horaireList.append(horaire)            
                for epis in info.find_all('div', class_= "info"):
                    episode = epis.p.text.strip()
                    epsList.append(episode)
                    for title in epis.find_all('a'):
                        titre = title.p.text.strip()
                        titleList.append(titre)

        for i in range(len(titleList)):
            animedict = {}
            animedict["Title"]= titleList[i]
            animedict["Epis"]=epsList[i]
            animedict["Horaire"]=horaireList[i]
            jourDict[journee].append(animedict) 
    return jourDict


