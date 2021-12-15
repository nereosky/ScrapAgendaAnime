from bs4.dammit import html_meta
import requests
from bs4 import BeautifulSoup

URL = "https://www.adkami.com/agenda"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

jourList = []
titleList = []
epsList = []
horaireList = []
agendaTitle = [[],[]]
agendaEps = [[],[]]
agendaHoraire = [[],[]]
i = 0
y = 0

colone = soup.find_all('div', class_="colone")
for jour in colone:
    journee = jour.h3.text.strip()
    jourList.append(journee)
    if jour.h3.text == "Lundi" or jour.h3.text == "Mardi":
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
    # horaireList.append("wall_wall")
    # epsList.append("wall_wall")
    # titleList.append("wall_wall")
    # for y in range(len(titleList)):
    agendaTitle[0][0] = titleList[0]
    # for y in agendaEps:
    #     agendaEps[i][y] = agendaEps[y]
    # for y in agendaHoraire:
    #     agendaHoraire[i][y] = agendaHoraire[y]
    i += 1

print(agendaTitle,agendaEps, agendaHoraire)


