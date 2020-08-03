
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
red_kolvo = 1
black_kolvo = 1
grey_kolvo = 1
cup_kolvo = 1
maxi = 0
chislo = 0
grey = 0
red = 0
black = 0
cup = 0
kolvo = 0
h = 9
d1 = datetime.datetime.now().date()


def cronjob():
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
  bo = 1
  while(h == 9):
    d2 = datetime.datetime.now().date()
    d3 = datetime.datetime.now()
    if(d3.minute % 2 == 1 and d3.second == 25 and bo == 1):
      bo = 2
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
          if red >= 7 and maxi - red_kolvo >= 5 and kolvo / red_kolvo >= 3.1:
            table1 = Table(color='grey', number=ch, recom='red')
            table1.save()
          elif black >= 7 and maxi - black_kolvo >= 5 and kolvo / black_kolvo >= 3.1:
            table1 = Table(color='grey', number=ch, recom='black')
            table1.save()
          elif cup > 87 and maxi - cup_kolvo >= 5 and kolvo / cup_kolvo >= 3.1:
            table1 = Table(color='grey', number=ch, recom='cup')
            table1.save()
          elif kkk == 1 and numbers_kolvo[nomer] != 0:
            if numbers[nomer] > 35 and kolvo / numbers_kolvo[nomer] >= 30:
              if nomer == 0 and black >= 5 and numbers[7] >= 7 and cup >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 1 and grey >= 5 and numbers[8] >= 7 and numbers[12] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 2 and red >= 5 and numbers[9] >= 7 and numbers[13] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 3 and black >= 5 and numbers[14] >= 7 and numbers[10] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 4 and grey >= 5 and numbers[15] >= 7 and numbers[11] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 5 and red >= 5 and numbers[12] >= 7 and numbers[16] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 6 and black >= 5 and numbers[13] >= 7 and numbers[17] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 7 and grey >= 5 and numbers[0] >= 7 and numbers[14] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 8 and red >= 5 and numbers[15] >= 7 and numbers[1] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 9 and black >= 5 and numbers[2] >= 7 and numbers[16] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 10 and grey >= 5 and numbers[3] >= 7 and numbers[17] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 11 and red >= 5 and numbers[4] >= 7 and cup >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 12 and black >= 5 and numbers[1] >= 7 and numbers[5] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 13 and grey >= 5 and numbers[2] >= 7 and numbers[6] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 14 and red >= 5 and numbers[3] >= 7 and numbers[7] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 15 and black >= 5 and numbers[4] >= 7 and numbers[8] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 16 and grey >= 5 and numbers[5] >= 7 and numbers[9] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 17 and red >= 5 and numbers[6] >= 7 and numbers[10] >= 7:
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
          if black >= 7 and maxi - black_kolvo >= 5 and kolvo / black_kolvo >= 3.1:
            table1 = Table(color='red', number=ch, recom='black')
            table1.save()
          elif grey >= 7 and maxi - grey_kolvo >= 5 and kolvo / grey_kolvo >= 3.1:
            table1 = Table(color='red', number=ch, recom='grey')
            table1.save()
          elif cup > 87 and maxi - cup_kolvo >= 5 and kolvo / cup_kolvo >= 3.1:
            table1 = Table(color='red', number=ch, recom='cup')
            table1.save()
          elif kkk == 1 and numbers_kolvo[nomer] != 0 and numbers[nomer] > 35 and kolvo / numbers_kolvo[nomer] >= 30:
            if nomer == 0 and black >= 5 and numbers[7] >= 7 and cup >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 1 and grey >= 5 and numbers[8] >= 7 and numbers[12] >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 2 and red >= 5 and numbers[9] >= 7 and numbers[13] >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 3 and black >= 5 and numbers[14] >= 7 and numbers[10] >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 4 and grey >= 5 and numbers[15] >= 7 and numbers[11] >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 5 and red >= 5 and numbers[12] >= 7 and numbers[16] >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 6 and black >= 5 and numbers[13] >= 7 and numbers[17] >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 7 and grey >= 5 and numbers[0] >= 7 and numbers[14] >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 8 and red >= 5 and numbers[15] >= 7 and numbers[1] >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 9 and black >= 5 and numbers[2] >= 7 and numbers[16] >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 10 and grey >= 5 and numbers[3] >= 7 and numbers[17] >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 11 and red >= 5 and numbers[4] >= 7 and cup >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 12 and black >= 5 and numbers[1] >= 7 and numbers[5] >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 13 and grey >= 5 and numbers[2] >= 7 and numbers[6] >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 14 and red >= 5 and numbers[3] >= 7 and numbers[7] >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 15 and black >= 5 and numbers[4] >= 7 and numbers[8] >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 16 and grey >= 5 and numbers[5] >= 7 and numbers[9] >= 7:
              nomer += 1
              table1 = Table(color='red', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 17 and red >= 5 and numbers[6] >= 7 and numbers[10] >= 7:
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
          if red >= 7 and maxi - red_kolvo >= 5 and kolvo / red_kolvo >= 3.1:
            table1 = Table(color='black', number=ch, recom='red')
            table1.save()
          elif grey >= 7 and maxi - grey_kolvo >= 5 and kolvo / grey_kolvo >= 3.1:
            table1 = Table(color='black', number=ch, recom='grey')
            table1.save()
          elif cup > 87 and maxi - cup_kolvo >= 5 and kolvo / cup_kolvo >= 3.1:
            table1 = Table(color='black', number=ch, recom='cup')
            table1.save()
          elif kkk == 1 and numbers_kolvo[nomer] != 0 and numbers[nomer] > 35 and kolvo / numbers_kolvo[nomer] >= 30:
            if nomer == 0 and black >= 5 and numbers[7] >= 7 and cup >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 1 and grey >= 5 and numbers[8] >= 7 and numbers[12] >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 2 and red >= 5 and numbers[9] >= 7 and numbers[13] >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 3 and black >= 5 and numbers[14] >= 7 and numbers[10] >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 4 and grey >= 5 and numbers[15] >= 7 and numbers[11] >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 5 and red >= 5 and numbers[12] >= 7 and numbers[16] >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 6 and black >= 5 and numbers[13] >= 7 and numbers[17] >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 7 and grey >= 5 and numbers[0] >= 7 and numbers[14] >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 8 and red >= 5 and numbers[15] >= 7 and numbers[1] >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 9 and black >= 5 and numbers[2] >= 7 and numbers[16] >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 10 and grey >= 5 and numbers[3] >= 7 and numbers[17] >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 11 and red >= 5 and numbers[4] >= 7 and cup >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 12 and black >= 5 and numbers[1] >= 7 and numbers[5] >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 13 and grey >= 5 and numbers[2] >= 7 and numbers[6] >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 14 and red >= 5 and numbers[3] >= 7 and numbers[7] >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 15 and black >= 5 and numbers[4] >= 7 and numbers[8] >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 16 and grey >= 5 and numbers[5] >= 7 and numbers[9] >= 7:
              nomer += 1
              table1 = Table(color='black', number=ch, recom=str(nomer))
              table1.save()
            elif nomer == 17 and red >= 5 and numbers[6] >= 7 and numbers[10] >= 7:
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
          if red >= 7 and maxi - red_kolvo >= 5 and kolvo / red_kolvo >= 3.1:
            table1 = Table(color='cup', number=ch, recom='red')
            table1.save()
          elif black >= 7 and maxi - black_kolvo >= 5 and kolvo / black_kolvo >= 3.1:
            table1 = Table(color='cup', number=ch, recom='black')
            table1.save()
          elif grey > 6 and maxi - grey_kolvo >= 5 and kolvo / grey_kolvo >= 3.1:
            table1 = Table(color='cup', number=ch, recom='grey')
            table1.save()
          elif kkk == 1 and numbers_kolvo[nomer] != 0:
            if numbers[nomer] > 35 and kolvo // numbers_kolvo[nomer] >= 30:
              if nomer == 0 and black >= 5 and numbers[7] >= 7 and cup >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 1 and grey >= 5 and numbers[8] >= 7 and numbers[12] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 2 and red >= 5 and numbers[9] >= 7 and numbers[13] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 3 and black >= 5 and numbers[14] >= 7 and numbers[10] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 4 and grey >= 5 and numbers[15] >= 7 and numbers[11] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 5 and red >= 5 and numbers[12] >= 7 and numbers[16] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 6 and black >= 5 and numbers[13] >= 7 and numbers[17] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 7 and grey >= 5 and numbers[0] >= 7 and numbers[14] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 8 and red >= 5 and numbers[15] >= 7 and numbers[1] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 9 and black >= 5 and numbers[2] >= 7 and numbers[16] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 10 and grey >= 5 and numbers[3] >= 7 and numbers[17] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 11 and red >= 5 and numbers[4] >= 7 and cup >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 12 and black >= 5 and numbers[1] >= 7 and numbers[5] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 13 and grey >= 5 and numbers[2] >= 7 and numbers[6] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 14 and red >= 5 and numbers[3] >= 7 and numbers[7] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 15 and black >= 5 and numbers[4] >= 7 and numbers[8] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 16 and grey >= 5 and numbers[5] >= 7 and numbers[9] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 17 and red >= 5 and numbers[6] >= 7 and numbers[10] >= 7:
                nomer += 1
                table1 = Table(color='cup', number=ch, recom=str(nomer))
                table1.save()
              else:
                table1 = Table(color='cup', number=ch, recom='-')
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
          if black >= 7 and maxi - black_kolvo >= 5 and kolvo / black_kolvo >= 3.1:
            table1 = Table(color='red', number=ch, recom='black')
            table1.save()
          elif grey >= 7 and maxi - grey_kolvo >= 5 and kolvo / grey_kolvo >= 3.1:
            table1 = Table(color='red', number=ch, recom='grey')
            table1.save()
          elif cup > 87 and maxi - cup_kolvo >= 5 and kolvo / cup_kolvo >= 3.1:
            table1 = Table(color='red', number=ch, recom='cup')
            table1.save()
          elif kkk == 1 and numbers_kolvo[nomer] != 0:
            if numbers[nomer] > 35 and kolvo // numbers_kolvo[nomer] >= 30:
              if nomer == 0 and black >= 5 and numbers[7] >= 7 and cup >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 1 and grey >= 5 and numbers[8] >= 7 and numbers[12] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 2 and red >= 5 and numbers[9] >= 7 and numbers[13] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 3 and black >= 5 and numbers[14] >= 7 and numbers[10] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 4 and grey >= 5 and numbers[15] >= 7 and numbers[11] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 5 and red >= 5 and numbers[12] >= 7 and numbers[16] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 6 and black >= 5 and numbers[13] >= 7 and numbers[17] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 7 and grey >= 5 and numbers[0] >= 7 and numbers[14] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 8 and red >= 5 and numbers[15] >= 7 and numbers[1] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 9 and black >= 5 and numbers[2] >= 7 and numbers[16] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 10 and grey >= 5 and numbers[3] >= 7 and numbers[17] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 11 and red >= 5 and numbers[4] >= 7 and cup >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 12 and black >= 5 and numbers[1] >= 7 and numbers[5] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 13 and grey >= 5 and numbers[2] >= 7 and numbers[6] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 14 and red >= 5 and numbers[3] >= 7 and numbers[7] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 15 and black >= 5 and numbers[4] >= 7 and numbers[8] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 16 and grey >= 5 and numbers[5] >= 7 and numbers[9] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 17 and red >= 5 and numbers[6] >= 7 and numbers[10] >= 7:
                nomer += 1
                table1 = Table(color='red', number=ch, recom=str(nomer))
                table1.save()
              else:
                table1 = Table(color='red', number=ch, recom='-')
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
          if red >= 7 and maxi - red_kolvo >= 5 and kolvo / red_kolvo >= 3.1:
            table1 = Table(color='black', number=ch, recom='red')
            table1.save()
          elif grey >= 7 and maxi - grey_kolvo >= 5 and kolvo / grey_kolvo >= 3.1:
            table1 = Table(color='black', number=ch, recom='grey')
            table1.save()
          elif cup > 87 and maxi - cup_kolvo >= 5 and kolvo / cup_kolvo >= 3.1:
            table1 = Table(color='black', number=ch, recom='cup')
            table1.save()
          elif kkk == 1 and numbers_kolvo[nomer] != 0:
            if numbers[nomer] > 35 and kolvo // numbers_kolvo[nomer] >= 30:
              if nomer == 0 and black >= 5 and numbers[7] >= 7 and cup >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 1 and grey >= 5 and numbers[8] >= 7 and numbers[12] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 2 and red >= 5 and numbers[9] >= 7 and numbers[13] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 3 and black >= 5 and numbers[14] >= 7 and numbers[10] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 4 and grey >= 5 and numbers[15] >= 7 and numbers[11] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 5 and red >= 5 and numbers[12] >= 7 and numbers[16] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 6 and black >= 5 and numbers[13] >= 7 and numbers[17] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 7 and grey >= 5 and numbers[0] >= 7 and numbers[14] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 8 and red >= 5 and numbers[15] >= 7 and numbers[1] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 9 and black >= 5 and numbers[2] >= 7 and numbers[16] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 10 and grey >= 5 and numbers[3] >= 7 and numbers[17] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 11 and red >= 5 and numbers[4] >= 7 and cup >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 12 and black >= 5 and numbers[1] >= 7 and numbers[5] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 13 and grey >= 5 and numbers[2] >= 7 and numbers[6] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 14 and red >= 5 and numbers[3] >= 7 and numbers[7] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 15 and black >= 5 and numbers[4] >= 7 and numbers[8] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 16 and grey >= 5 and numbers[5] >= 7 and numbers[9] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 17 and red >= 5 and numbers[6] >= 7 and numbers[10] >= 7:
                nomer += 1
                table1 = Table(color='black', number=ch, recom=str(nomer))
                table1.save()
              else:
                table1 = Table(color='black', number=ch, recom='-')
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
          if red >= 7 and maxi - red_kolvo >= 5 and kolvo / red_kolvo >= 3.1:
            table1 = Table(color='grey', number=ch, recom='red')
            table1.save()
          elif black >= 7 and maxi - black_kolvo >= 5 and kolvo / black_kolvo >= 3.1:
            table1 = Table(color='grey', number=ch, recom='black')
            table1.save()
          elif cup > 87 and maxi - cup_kolvo >= 5 and kolvo / cup_kolvo >= 3.1:
            table1 = Table(color='grey', number=ch, recom='cup')
            table1.save()
          elif kkk == 1 and numbers_kolvo[nomer] != 0:
            if numbers[nomer] > 35 and kolvo // numbers_kolvo[nomer] >= 30:
              if nomer == 0 and black >= 5 and numbers[7] >= 7 and cup >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 1 and grey >= 5 and numbers[8] >= 7 and numbers[12] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 2 and red >= 5 and numbers[9] >= 7 and numbers[13] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 3 and black >= 5 and numbers[14] >= 7 and numbers[10] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 4 and grey >= 5 and numbers[15] >= 7 and numbers[11] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 5 and red >= 5 and numbers[12] >= 7 and numbers[16] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 6 and black >= 5 and numbers[13] >= 7 and numbers[17] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 7 and grey >= 5 and numbers[0] >= 7 and numbers[14] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 8 and red >= 5 and numbers[15] >= 7 and numbers[1] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 9 and black >= 5 and numbers[2] >= 7 and numbers[16] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 10 and grey >= 5 and numbers[3] >= 7 and numbers[17] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 11 and red >= 5 and numbers[4] >= 7 and cup >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 12 and black >= 5 and numbers[1] >= 7 and numbers[5] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 13 and grey >= 5 and numbers[2] >= 7 and numbers[6] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 14 and red >= 5 and numbers[3] >= 7 and numbers[7] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 15 and black >= 5 and numbers[4] >= 7 and numbers[8] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 16 and grey >= 5 and numbers[5] >= 7 and numbers[9] >= 7:
                nomer += 1
                table1 = Table(color='grey', number=ch, recom=str(nomer))
                table1.save()
              elif nomer == 17 and red >= 5 and numbers[6] >= 7 and numbers[10] >= 7:
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
            table1 = Table(color='grey', number=ch, recom='-')
            table1.save()
      else:
        print('Error')
    elif d3.minute % 2 == 0:
      bo = 1
