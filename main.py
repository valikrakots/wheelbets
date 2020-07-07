from blog.models import Table
import time
import requests
from bs4 import BeautifulSoup
import datetime


URL = 'https://betgames9.betgames.tv/ext/game_results/get_results_info/testpartner/2019-04-03/0/1/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
           'accept': '*/*'}


def get_html(url, params=None):
  r = requests.get(url, headers=HEADERS, params=params)
  return r


def cronjob():
  red_kolvo = 0
  black_kolvo = 0
  grey_kolvo = 0
  cup_kolvo = 0
  maxi = 0
  chislo = 0
  grey = 0
  red = 0
  black = 0
  cup = 0
  kolvo = 0
  h = 9
  d1 = datetime.datetime.now().date()
  while(h == 9):
    d2 = datetime.datetime.now().date()
    if d1 < d2:
      d1 = datetime.datetime.now().date()
      table1 = Table(color='change', number='ch', recom='ch')
      table1.save()
    html = get_html(URL)
    if html.status_code == 200:
      htmlu = html.text
      kolvo += 1
      k = htmlu.find('"game_id":"7"')
      if(htmlu[k + 150] == '"' and htmlu[k + 161] == 'g'):
        ch = htmlu[k + 149]
        red += 1
        black += 1
        grey = 0
        cup += 1
        grey_kolvo += 1
        if grey_kolvo > maxi:
          maxi = grey_kolvo
        chislo = int(ch)
        if red >= 6 and maxi - red_kolvo <= 26:
          table1 = Table(color='grey', number=ch, recom='red')
          table1.save()
        elif black >= 6 and maxi - black_kolvo <= 26:
          table1 = Table(color='grey', number=ch, recom='black')
          table1.save()
        elif cup > 87 and maxi - cup_kolvo <= 26:
          table1 = Table(color='grey', number=ch, recom='cup')
          table1.save()
        else:
          table1 = Table(color='grey', number=ch, recom='-')
          table1.save()
      elif(htmlu[k + 150] == '"' and htmlu[k + 161] == 'r'):
        ch = htmlu[k + 149]
        grey += 1
        red = 0
        black += 1
        cup += 1
        red_kolvo += 1
        if red_kolvo > maxi:
          maxi = red_kolvo
        chislo = int(ch)
        if black >= 6 and maxi - black_kolvo <= 26:
          table1 = Table(color='red', number=ch, recom='black')
          table1.save()
        elif grey >= 6 and maxi - grey_kolvo <= 26:
          table1 = Table(color='red', number=ch, recom='grey')
          table1.save()
        elif cup > 87 and maxi - cup_kolvo <= 26:
          table1 = Table(color='red', number=ch, recom='cup')
          table1.save()
        else:
          table1 = Table(color='red', number=ch, recom='-')
          table1.save()
      elif(htmlu[k + 150] == '"' and htmlu[k + 161] == 'b'):
        ch = htmlu[k + 149]
        red += 1
        grey += 1
        black = 0
        cup += 1
        black_kolvo += 1
        if black_kolvo > maxi:
          maxi = black_kolvo
        chislo = int(ch)
        if red >= 6 and maxi - red_kolvo <= 26:
          table1 = Table(color='black', number=ch, recom='red')
          table1.save()
        elif grey >= 6 and maxi - grey_kolvo <= 26:
          table1 = Table(color='black', number=ch, recom='grey')
          table1.save()
        elif cup > 87 and maxi - cup_kolvo <= 26:
          table1 = Table(color='black', number=ch, recom='cup')
          table1.save()
        else:
          table1 = Table(color='black', number=ch, recom='-')
          table1.save()
      elif(htmlu[k + 149] == '0'):
        ch = htmlu[k + 149]
        red += 1
        grey += 1
        black += 1
        cup_kolvo += 1
        cup = 0
        if cup_kolvo > maxi:
          maxi = cup_kolvo
        chislo = int(ch)
        if red >= 6 and maxi - red_kolvo <= 26:
          table1 = Table(color='cup', number=ch, recom='red')
          table1.save()
        elif black >= 6 and maxi - black_kolvo <= 26:
          table1 = Table(color='cup', number=ch, recom='black')
          table1.save()
        elif grey > 6 and maxi - grey_kolvo <= 26:
          table1 = Table(color='cup', number=ch, recom='grey')
          table1.save()
        else:
          table1 = Table(color='cup', number=ch, recom='-')
          table1.save()
      elif(htmlu[k + 162] == 'r'):
        ch = htmlu[k + 149] + htmlu[k + 150]
        red = 0
        grey += 1
        black += 1
        cup += 1
        red_kolvo += 1
        if red_kolvo > maxi:
          maxi = red_kolvo
        chislo = int(ch)
        if black >= 6 and maxi - black_kolvo <= 26:
          table1 = Table(color='red', number=ch, recom='black')
          table1.save()
        elif grey >= 6 and maxi - grey_kolvo <= 26:
          table1 = Table(color='red', number=ch, recom='grey')
          table1.save()
        elif cup > 87 and maxi - cup_kolvo <= 26:
          table1 = Table(color='red', number=ch, recom='cup')
          table1.save()
        else:
          table1 = Table(color='red', number=ch, recom='-')
          table1.save()
      elif(htmlu[k + 162] == 'b'):
        ch = htmlu[k + 149] + htmlu[k + 150]
        black = 0
        red += 1
        grey += 1
        cup += 1
        black_kolvo += 1
        if black_kolvo > maxi:
          maxi = black_kolvo
        chislo = int(ch)
        if red >= 6 and maxi - red_kolvo <= 26:
          table1 = Table(color='black', number=ch, recom='red')
          table1.save()
        elif grey >= 6 and maxi - grey_kolvo <= 26:
          table1 = Table(color='black', number=ch, recom='grey')
          table1.save()
        elif cup > 87 and maxi - cup_kolvo <= 26:
          table1 = Table(color='black', number=ch, recom='cup')
          table1.save()
        else:
          table1 = Table(color='black', number=ch, recom='-')
          table1.save()
      elif(htmlu[k + 162] == 'g'):
        ch = htmlu[k + 149] + htmlu[k + 150]
        grey = 0
        red += 1
        black += 1
        cup += 1
        grey_kolvo += 1
        if grey_kolvo > maxi:
          maxi = grey_kolvo
        chislo = int(ch)
        if red >= 6 and maxi - red_kolvo <= 26:
          table1 = Table(color='grey', number=ch, recom='red')
          table1.save()
        elif black >= 6 and maxi - black_kolvo <= 26:
          table1 = Table(color='grey', number=ch, recom='black')
          table1.save()
        elif cup > 87 and maxi - cup_kolvo <= 26:
          table1 = Table(color='grey', number=ch, recom='cup')
          table1.save()
        else:
          table1 = Table(color='grey', number=ch, recom='-')
          table1.save()
    else:
      print('Error')
    time.sleep(119)
