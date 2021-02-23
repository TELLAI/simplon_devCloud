from bs4 import BeautifulSoup
import requests
import prettify
import datetime

class Scrap_info:
    def __init__(self):
        self.matchs = []
        self.list_url = ['https://www.footao.tv/programmefoot.php?mois=f%C3%A9vrier&ms=02&an=2021', 'https://www.footao.tv/programmefoot.php?mois=mars&ms=03&an=2021', 'https://www.footao.tv/programmefoot.php?mois=avril&ms=04&an=2021', 'https://www.footao.tv/programmefoot.php?mois=mai&ms=05&an=2021', 'https://www.footao.tv/programmefoot.php?mois=juin&ms=06&an=2021']
        self.list_response = []
        self.list_content = []
        self.list_name = []
        self.list_date_text = []
        self.list_time = []
        self.list_equipe1 = []
        self.list_equipe2 = []
        self.list_competition = []
        self.list_chaine = []
        self.list_date_num = []
        

    def get_response(self):
        for i in self.list_url:
            self.list_response.append(requests.get(i))

    def get_content(self):
        for i in self.list_response:
            self.list_content.append(BeautifulSoup(i.content, 'html.parser'))
    
    def get_name(self):
        for i in self.list_content:
            element = i.select('article>section')
            for ii, i in enumerate(element):
                divs = element[ii].select("div")
                for yy, y in enumerate(divs):
                    match_s = divs[yy].select("a[class=rc]")
                    self.list_name.append(match_s[0].get_text())
    def get_date(self):
        for i in self.list_content:
            element = i.select('article>section')
            for ii, i in enumerate(element):
                date_s = element[ii].select("h2>a")
                self.list_date_text.append(date_s[0].get_text())
                dates = element[ii]['id']
                if dates=="pjr":
                    dates = datetime.date.today()
                    j = str(dates.day)
                    m = list(str(dates.month))
                    if len(m) == 1:
                        m.insert(0, "0")
                        m = "".join(m)
                    else:
                        m = "".join(m)
                    yyyy = list(str(dates.year))
                    yy = "".join(yyyy[2:])
                    self.list_date_num.append(j+m+yy)
                else:
                    date_nums = list(dates)
                    del date_nums[0]
                    self.list_date_num.append("".join(date_nums))
        
    def get_equipe(self):
        for i in self.list_name:
            match_l = list(i)
            if '·' in match_l:
                self.list_equipe1.append(''.join(match_l[:match_l.index('·')-1]))
                self.list_equipe2.append(''.join(match_l[match_l.index('·')+2:]))
            else:
                self.list_equipe1.append(i)
                self.list_equipe2.append(i)

    def get_competition(self):
        for i in self.list_content:
            element = i.select('article>section')
            for ii, i in enumerate(element):
                divs = element[ii].select("div")
                for yy, y in enumerate(divs):
                    compet_s = divs[yy].select("span[class=ap]")
                    if len(compet_s) > 0:
                        compet = compet_s[0].get_text()
                        if compet == "\xa0 \xa0»\xa0":
                            compet = "Ligue Europa"
                            self.list_competition.append(compet)
                        else :
                            compet = "match finie"
                            self.list_competition.append(compet)

    def get_chaine(self):
        for i in self.list_content:
            element = i.select('article>section')
            for ii, i in enumerate(element):
                divs = element[ii].select("div")
                for yy, y in enumerate(divs):
                    chaine_s = divs[yy].select('a')
                    chaine_o = list(chaine_s[0].find('img')['alt'])
                    if 'm' in chaine_o:
                        self.list_chaine.append(''.join(chaine_o[:chaine_o.index('m') - 1]))
                    else:
                        self.list_chaine.append("???")
    
    def get_time(self):
        for i in self.list_content:
            element = i.select('article>section')
            for ii, i in enumerate(element):
                divs = element[ii].select("div")
                for yy, y in enumerate(divs):
                    time_s = divs[yy].select('time')
                    self.list_time.append(time_s[0].get_text())

    def finder(self):
        for i in self.list_content:
            element = i.select('article>section')
            for ii, i in enumerate(element):
                dates = element[ii]['id']
                if dates=="pjr":
                    dates = datetime.date.today()
                    j = str(dates.day)
                    m = list(str(dates.month))
                    if len(m) == 1:
                        m.insert(0, "0")
                        m = "".join(m)
                    else:
                        m = "".join(m)
                    yyyy = list(str(dates.year))
                    yy = "".join(yyyy[2:])
                    date_num = j+m+yy
                else:
                    date_nums = list(dates)
                    del date_nums[0]
                    date_num = "".join(date_nums)
                date_s = element[ii].select("h2>a")
                date_text = date_s[0].get_text()
                divs = element[ii].select("div")
                for yy, y in enumerate(divs):
                    time_s = divs[yy].select('time')
                    time = time_s[0].get_text()
                    chaine_s = divs[yy].select('a')
                    chaine_o = list(chaine_s[0].find('img')['alt'])
                    if 'm' in chaine_o:
                        chaine = ''.join(chaine_o[:chaine_o.index('m') - 1])
                    else:
                        chaine = "???"
                    match_s = divs[yy].select("a[class=rc]")
                    match = match_s[0].get_text()
                    match_l = list(match)
                    if '·' in match_l:
                        eq1 = ''.join(match_l[:match_l.index('·')-1])
                        eq2 = ''.join(match_l[match_l.index('·')+2:])
                    else:
                        eq1 = match
                        eq2 = match
                    compet_s = divs[yy].select("span[class=ap]")
                    if len(compet_s) > 0:
                        compet = compet_s[0].get_text()
                        if compet == "\xa0 \xa0»\xa0":
                            compet = "Ligue Europa"
                        dict_match = {"Nom":match, "Date_text":date_text, "Time":time, "Equipe1":eq1, "Equipe2":eq2, "Competition":compet, "Chaine":chaine, "Date_num": date_num}
                    else :
                        compet = "match finie"
                        dict_match = {"Nom":match, "Date_text":date_text, "Time":time, "Equipe1":eq1, "Equipe2":eq2, "Competition":compet, "Chaine":chaine, "Date_num": date_num}
                    self.matchs.append(dict_match)

test = Scrap_info()
test.get_response()
test.get_content()
test.get_name()
print(len(test.list_name))