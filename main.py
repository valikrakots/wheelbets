
from blog.models import Table
import time
import requests
from bs4 import BeautifulSoup
import datetime
import threading


URL = 'https://betgames9.betgames.tv/ext/game_results/get_results_info/testpartner/2019-04-03/0/1/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
           'accept': '*/*'}


def get_html(url, params=None):
  r = requests.get(url, headers=HEADERS, params=params)
  return r


numbers = [0] * 18
numbers_kolvo = [0] * 18
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


def runui():
  global numbers
  global numbers_kolvo
  global red_kolvo
  global black_kolvo
  global grey_kolvo
  global cup_kolvo
  global maxi
  global chislo
  global grey
  global red
  global black
  global cup
  global kolvo
  global h
  global d1
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
        minimum = 0
        pervyj = 0
        nomer = 0
        sczetczik = 0
        kkk = 0
        f = 0
        while f < 18:
          numbers[f] += 1
          f += 1
        if ch == '2':
          numbers[1] = 0
          numbers_kolvo[1] += 1
        elif ch == '8':
          numbers[7] = 0
          numbers_kolvo[7] += 1
        elif ch == '5':
          numbers[4] = 0
          numbers_kolvo[4] += 1
        for num in numbers_kolvo:
          if pervyj == 0:
            pervyj = 1
            kkk = 1
            minimum = num
            nomer = 0
          else:
            if num < minimum:
              kkk = 1
              minimum = num
              nomer = sczetczik
            elif num == minimum:
              kkk += 1
          sczetczik += 1
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
        elif kkk == 1 and numbers_kolvo[nomer] != 0:
          if numbers[nomer] > 50 and kolvo / numbers_kolvo[nomer] >= 30:
            nomer += 1
            table1 = Table(color='grey', number=ch, recom=str(nomer))
            table1.save()
          else:
            table1 = Table(color='grey', number=ch, recom='-')
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
        minimum = 0
        pervyj = 0
        nomer = 0
        sczetczik = 0
        kkk = 0
        f = 0
        while f < 18:
          numbers[f] += 1
          f += 1
        if ch == '3':
          numbers[2] = 0
          numbers_kolvo[2] += 1
        elif ch == '9':
          numbers[8] = 0
          numbers_kolvo[8] += 1
        elif ch == '6':
          numbers[5] = 0
          numbers_kolvo[5] += 1
        for num in numbers_kolvo:
          if pervyj == 0:
            pervyj = 1
            kkk = 1
            minimum = num
            nomer = 0
          else:
            if num < minimum:
              kkk = 1
              minimum = num
              nomer = sczetczik
            elif num == minimum:
              kkk += 1
          sczetczik += 1
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
        elif kkk == 1 and numbers_kolvo[nomer] != 0:
          if numbers[nomer] > 50 and kolvo // numbers_kolvo[nomer] >= 30:
            nomer += 1
            table1 = Table(color='red', number=ch, recom=str(nomer))
            table1.save()
          else:
            table1 = Table(color='red', number=ch, recom='-')
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
        minimum = 0
        pervyj = 0
        nomer = 0
        sczetczik = 0
        kkk = 0
        f = 0
        while f < 18:
          numbers[f] += 1
          f += 1
        if ch == '1':
          numbers[0] = 0
          numbers_kolvo[0] += 1
        elif ch == '4':
          numbers[3] = 0
          numbers_kolvo[3] += 1
        elif ch == '7':
          numbers[6] = 0
          numbers_kolvo[6] += 1
        for num in numbers_kolvo:
          if pervyj == 0:
            pervyj = 1
            kkk = 1
            minimum = num
            nomer = 0
          else:
            if num < minimum:
              kkk = 1
              minimum = num
              nomer = sczetczik
            elif num == minimum:
              kkk += 1
          sczetczik += 1
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
        elif kkk == 1 and numbers_kolvo[nomer] != 0:
          if numbers[nomer] > 50 and kolvo // numbers_kolvo[nomer] >= 30:
            nomer += 1
            table1 = Table(color='black', number=ch, recom=str(nomer))
            table1.save()
          else:
            table1 = Table(color='black', number=ch, recom='-')
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
        minimum = 0
        pervyj = 0
        nomer = 0
        sczetczik = 0
        kkk = 0
        f = 0
        while f < 18:
          numbers[f] += 1
          f += 1
        for num in numbers_kolvo:
          if pervyj == 0:
            pervyj = 1
            kkk = 1
            minimum = num
            nomer = 0
          else:
            if num < minimum:
              kkk = 1
              minimum = num
              nomer = sczetczik
            elif num == minimum:
              kkk += 1
          sczetczik += 1
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
        elif kkk == 1 and numbers_kolvo[nomer] != 0:
          if numbers[nomer] > 50 and kolvo // numbers_kolvo[nomer] >= 30:
            nomer += 1
            table1 = Table(color='cup', number=ch, recom=str(nomer))
            table1.save()
          else:
            table1 = Table(color='cup', number=ch, recom='-')
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
        minimum = 0
        pervyj = 0
        nomer = 0
        sczetczik = 0
        kkk = 0
        f = 0
        while f < 18:
          numbers[f] += 1
          f += 1
        if ch == '12':
          numbers[11] = 0
          numbers_kolvo[11] += 1
        elif ch == '18':
          numbers[17] = 0
          numbers_kolvo[17] += 1
        elif ch == '15':
          numbers[14] = 0
          numbers_kolvo[14] += 1
        for num in numbers_kolvo:
          if pervyj == 0:
            pervyj = 1
            kkk = 1
            minimum = num
            nomer = 0
          else:
            if num < minimum:
              kkk = 1
              minimum = num
              nomer = sczetczik
            elif num == minimum:
              kkk += 1
          sczetczik += 1
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
        elif kkk == 1 and numbers_kolvo[nomer] != 0:
          if numbers[nomer] > 50 and kolvo // numbers_kolvo[nomer] >= 30:
            nomer += 1
            table1 = Table(color='red', number=ch, recom=str(nomer))
            table1.save()
          else:
            table1 = Table(color='red', number=ch, recom='-')
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
        minimum = 0
        pervyj = 0
        nomer = 0
        sczetczik = 0
        kkk = 0
        f = 0
        while f < 18:
          numbers[f] += 1
          f += 1
        if ch == '10':
          numbers[9] = 0
          numbers_kolvo[9] += 1
        elif ch == '13':
          numbers[12] = 0
          numbers_kolvo[12] += 1
        elif ch == '16':
          numbers[15] = 0
          numbers_kolvo[15] += 1
        for num in numbers_kolvo:
          if pervyj == 0:
            pervyj = 1
            kkk = 1
            minimum = num
            nomer = 0
          else:
            if num < minimum:
              kkk = 1
              minimum = num
              nomer = sczetczik
            elif num == minimum:
              kkk += 1
          sczetczik += 1
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
        elif kkk == 1 and numbers_kolvo[nomer] != 0:
          if numbers[nomer] > 50 and kolvo // numbers_kolvo[nomer] >= 30:
            nomer += 1
            table1 = Table(color='black', number=ch, recom=str(nomer))
            table1.save()
          else:
            table1 = Table(color='black', number=ch, recom='-')
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
        minimum = 0
        pervyj = 0
        nomer = 0
        sczetczik = 0
        kkk = 0
        f = 0
        while f < 18:
          numbers[f] += 1
          f += 1
        if ch == '11':
          numbers[10] = 0
          numbers_kolvo[10] += 1
        elif ch == '14':
          numbers[13] = 0
          numbers_kolvo[13] += 1
        elif ch == '17':
          numbers[16] = 0
          numbers_kolvo[16] += 1
        for num in numbers_kolvo:
          if pervyj == 0:
            pervyj = 1
            kkk = 1
            minimum = num
            nomer = 0
          else:
            if num < minimum:
              kkk = 1
              minimum = num
              nomer = sczetczik
            elif num == minimum:
              kkk += 1
          sczetczik += 1
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
        elif kkk == 1 and numbers_kolvo[nomer] != 0:
          if numbers[nomer] > 50 and kolvo // numbers_kolvo[nomer] >= 30:
            nomer += 1
            table1 = Table(color='grey', number=ch, recom=str(nomer))
            table1.save()
          else:
            table1 = Table(color='grey', number=ch, recom='-')
            table1.save()
        else:
          table1 = Table(color='grey', number=ch, recom='-')
          table1.save()
    else:
      print('Error')
    h = 10


def cronjob():
  flag = 1
  global h
  while flag == 1:
    h = 9
    t1 = threading.Thread(target=runui)
    t1.start()
    print("oooooo")
    time.sleep(119.8564806382369)
