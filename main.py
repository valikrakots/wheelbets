
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


numbers = [1] * 18
numbers_kolvo = [1] * 18
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
kolvo = 4
h = 9
d1 = datetime.datetime.now().date()
promezh = [1] * 3
promezh_kolvo = [0] * 3
bome = [1] * 2
bome_prom = [0] * 2


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
  global promezh
  global promezh_kolvo
  global bome
  global bome_prom
  rec = "-"
  bo = 1
  last_rec = "-"
  while(h == 9):
    d2 = datetime.datetime.now().date()
    d3 = datetime.datetime.now()
    if(d3.minute % 2 == 1 and d3.second == 25 and bo == 1):
      bo = 2
      if d1 < d2:
        d1 = datetime.datetime.now().date()
        table1 = Table(color='change', number='ch',
                       recom='ch', success='e', previous='e')
        table1.save()
      html = get_html(URL)
      if html.status_code == 200:
        ch = ""
        f = 0
        while f < 18:
          numbers[f] += 1
          f += 1
        f = 0
        while f < 3:
          promezh[f] += 1
          f += 1
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
          if ch == '2':
            bome[0] += 1
            bome_prom[1] += 1
            promezh_kolvo[0] += 1
            promezh[0] = 0
            numbers[1] = 0
            numbers_kolvo[1] += 1
          elif ch == '8':
            bome[0] += 1
            bome_prom[1] += 1
            promezh_kolvo[1] += 1
            promezh[1] = 0
            numbers[7] = 0
            numbers_kolvo[7] += 1
          elif ch == '5':
            bome[0] += 1
            bome_prom[1] += 1
            promezh_kolvo[0] += 1
            promezh[0] = 0
            numbers[4] = 0
            numbers_kolvo[4] += 1
          if grey_kolvo > maxi:
            maxi = grey_kolvo
        elif(htmlu[k + 150] == '"' and htmlu[k + 161] == 'r'):
          ch = htmlu[k + 149]
          grey += 1
          red = 0
          black += 1
          cup += 1
          red_kolvo += 1
          if ch == '3':
            bome[0] += 1
            bome_prom[1] += 1
            promezh_kolvo[0] += 1
            promezh[0] = 0
            numbers[2] = 0
            numbers_kolvo[2] += 1
          elif ch == '9':
            bome[0] += 1
            bome_prom[1] += 1
            promezh_kolvo[1] += 1
            promezh[1] = 0
            numbers[8] = 0
            numbers_kolvo[8] += 1
          elif ch == '6':
            bome[0] += 1
            bome_prom[1] += 1
            promezh_kolvo[0] += 1
            promezh[0] = 0
            numbers[5] = 0
            numbers_kolvo[5] += 1
          if red_kolvo > maxi:
            maxi = red_kolvo
        elif(htmlu[k + 150] == '"' and htmlu[k + 161] == 'b'):
          ch = htmlu[k + 149]
          red += 1
          grey += 1
          black = 0
          cup += 1
          black_kolvo += 1
          if ch == '1':
            bome[0] += 1
            bome_prom[1] += 1
            promezh_kolvo[0] += 1
            promezh[0] = 0
            numbers[0] = 0
            numbers_kolvo[0] += 1
          elif ch == '4':
            bome[0] += 1
            bome_prom[1] += 1
            promezh_kolvo[0] += 1
            promezh[0] = 0
            numbers[3] = 0
            numbers_kolvo[3] += 1
          elif ch == '7':
            bome[0] += 1
            bome_prom[1] += 1
            promezh_kolvo[1] += 1
            promezh[1] = 0
            numbers[6] = 0
            numbers_kolvo[6] += 1
          if black_kolvo > maxi:
            maxi = black_kolvo
        elif(htmlu[k + 149] == '0'):
          ch = htmlu[k + 149]
          red += 1
          grey += 1
          black += 1
          cup_kolvo += 1
          cup = 0
          if cup_kolvo > maxi:
            maxi = cup_kolvo
        elif(htmlu[k + 162] == 'r'):
          ch = htmlu[k + 149] + htmlu[k + 150]
          red = 0
          grey += 1
          black += 1
          cup += 1
          red_kolvo += 1
          if ch == '12':
            bome[1] += 1
            bome_prom[0] += 1
            promezh_kolvo[1] += 1
            promezh[1] = 0
            numbers[11] = 0
            numbers_kolvo[11] += 1
          elif ch == '18':
            bome[1] += 1
            bome_prom[0] += 1
            promezh_kolvo[2] += 1
            promezh[2] = 0
            numbers[17] = 0
            numbers_kolvo[17] += 1
          elif ch == '15':
            bome[1] += 1
            bome_prom[0] += 1
            promezh_kolvo[2] += 1
            promezh[2] = 0
            numbers[14] = 0
            numbers_kolvo[14] += 1
          if red_kolvo > maxi:
            maxi = red_kolvo
        elif(htmlu[k + 162] == 'b'):
          ch = htmlu[k + 149] + htmlu[k + 150]
          black = 0
          red += 1
          grey += 1
          cup += 1
          black_kolvo += 1
          if ch == '10':
            bome[1] += 1
            bome_prom[0] += 1
            promezh_kolvo[1] += 1
            promezh[1] = 0
            numbers[9] = 0
            numbers_kolvo[9] += 1
          elif ch == '13':
            bome[1] += 1
            bome_prom[0] += 1
            promezh_kolvo[2] += 1
            promezh[2] = 0
            numbers[12] = 0
            numbers_kolvo[12] += 1
          elif ch == '16':
            bome[1] += 1
            bome_prom[0] += 1
            promezh_kolvo[2] += 1
            promezh[2] = 0
            numbers[15] = 0
            numbers_kolvo[15] += 1
          if black_kolvo > maxi:
            maxi = black_kolvo
        elif(htmlu[k + 162] == 'g'):
          ch = htmlu[k + 149] + htmlu[k + 150]
          grey = 0
          red += 1
          black += 1
          cup += 1
          grey_kolvo += 1
          if ch == '11':
            bome[1] += 1
            bome_prom[0] += 1
            promezh_kolvo[1] += 1
            promezh[1] = 0
            numbers[10] = 0
            numbers_kolvo[10] += 1
          elif ch == '14':
            bome[1] += 1
            bome_prom[0] += 1
            promezh_kolvo[2] += 1
            promezh[2] = 0
            numbers[13] = 0
            numbers_kolvo[13] += 1
          elif ch == '17':
            bome[1] += 1
            bome_prom[0] += 1
            promezh_kolvo[2] += 1
            promezh[2] = 0
            numbers[16] = 0
            numbers_kolvo[16] += 1
          if grey_kolvo > maxi:
            maxi = grey_kolvo
        minimum = 0
        pervyj = 0
        nomer = 0
        sczetczik = 0
        kkk = 0
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
        da = 2
        r = '-'
        if rec == "< 9.5" and len(ch) == 1:
          da = 1
        elif rec == "> 9.5" and len(ch) == 2:
          da = 1
        elif rec == "1-6" and (ch == '1' or ch == '2' or ch == '3' or ch == '4' or ch == '5' or ch == '6'):
          da = 1
        elif rec == "7-12" and (ch == '7' or ch == '8' or ch == '9' or ch == '10' or ch == '11' or ch == '12'):
          da = 1
        elif rec == "13-18" and (ch == '13' or ch == '14' or ch == '15' or ch == '16' or ch == '17' or ch == '18'):
          da = 1
        elif rec == 'black' and (ch == '1' or ch == '4' or ch == '7' or ch == '10' or ch == '13' or ch == '16'):
          da = 1
        elif rec == 'red' and (ch == '3' or ch == '6' or ch == '9' or ch == '12' or ch == '15' or ch == '18'):
          da = 1
        elif rec == 'grey' and (ch == '2' or ch == '5' or ch == '8' or ch == '11' or ch == '14' or ch == '17'):
          da = 1
        elif rec == '1' and ch == '1':
          da = 1
        elif rec == '2' and ch == '2':
          da = 1
        elif rec == '3' and ch == '3':
          da = 1
        elif rec == '4' and ch == '4':
          da = 1
        elif rec == '5' and ch == '5':
          da = 1
        elif rec == '6' and ch == '6':
          da = 1
        elif rec == '7' and ch == '7':
          da = 1
        elif rec == '8' and ch == '8':
          da = 1
        elif rec == '9' and ch == '9':
          da = 1
        elif rec == '10' and ch == '10':
          da = 1
        elif rec == '11' and ch == '11':
          da = 1
        elif rec == '12' and ch == '12':
          da = 1
        elif rec == '13' and ch == '13':
          da = 1
        elif rec == '14' and ch == '14':
          da = 1
        elif rec == '15' and ch == '15':
          da = 1
        elif rec == '16' and ch == '16':
          da = 1
        elif rec == '17' and ch == '17':
          da = 1
        elif rec == '18' and ch == '18':
          da = 1
        elif rec == '-':
          da = 3
        if bome[0] / (kolvo - cup_kolvo) <= 0.36 and bome_prom[0] >= 3:
          rec = "< 9.5"
        elif bome[1] / (kolvo - cup_kolvo) <= 0.36 and bome_prom[1] >= 3:
          rec = "> 9.5"
        elif promezh[0] >= 6 and promezh_kolvo[0] / (kolvo - cup_kolvo) <= 0.26:
          rec = "1-6"
        elif promezh[1] >= 6 and promezh_kolvo[1] / (kolvo - cup_kolvo) <= 0.26:
          rec = "7-12"
        elif promezh[2] >= 6 and promezh_kolvo[2] / (kolvo - cup_kolvo) <= 0.26:
          rec = "13-18"
        elif red >= 7 and maxi - red_kolvo >= 5 and kolvo / red_kolvo >= 2.9:
          rec = "red"
        elif black >= 7 and maxi - black_kolvo >= 5 and kolvo / black_kolvo >= 2.9:
          rec = "black"
        elif grey >= 7 and maxi - grey_kolvo >= 5 and kolvo / grey_kolvo >= 2.9:
          rec = "grey"
        elif cup > 87 and maxi - cup_kolvo >= 5 and kolvo / cup_kolvo >= 2.9:
          rec = "cup"
        elif kkk == 1:
          if numbers[nomer] > 35 and kolvo / numbers_kolvo[nomer] >= 23:
            if nomer == 0 and black >= 3 and numbers[7] >= 7 and cup >= 7:
              nomer += 1
              rec = "1"
            elif nomer == 1 and grey >= 3 and numbers[8] >= 7 and numbers[12] >= 7:
              nomer += 1
              rec = "2"
            elif nomer == 2 and red >= 3 and numbers[9] >= 7 and numbers[13] >= 7:
              nomer += 1
              rec = "3"
            elif nomer == 3 and black >= 3 and numbers[14] >= 7 and numbers[10] >= 7:
              nomer += 1
              rec = "4"
            elif nomer == 4 and grey >= 3 and numbers[15] >= 7 and numbers[11] >= 7:
              nomer += 1
              rec = "5"
            elif nomer == 5 and red >= 3 and numbers[12] >= 7 and numbers[16] >= 7:
              nomer += 1
              rec = "6"
            elif nomer == 6 and black >= 3 and numbers[13] >= 7 and numbers[17] >= 7:
              nomer += 1
              rec = "7"
            elif nomer == 7 and grey >= 3 and numbers[0] >= 7 and numbers[14] >= 7:
              nomer += 1
              rec = "8"
            elif nomer == 8 and red >= 3 and numbers[15] >= 7 and numbers[1] >= 7:
              nomer += 1
              rec = "9"
            elif nomer == 9 and black >= 3 and numbers[2] >= 7 and numbers[16] >= 7:
              nomer += 1
              rec = "10"
            elif nomer == 10 and grey >= 3 and numbers[3] >= 7 and numbers[17] >= 7:
              nomer += 1
              rec = "11"
            elif nomer == 11 and red >= 3 and numbers[4] >= 7 and cup >= 7:
              nomer += 1
              rec = "12"
            elif nomer == 12 and black >= 3 and numbers[1] >= 7 and numbers[5] >= 7:
              nomer += 1
              rec = "13"
            elif nomer == 13 and grey >= 3 and numbers[2] >= 7 and numbers[6] >= 7:
              nomer += 1
              rec = "14"
            elif nomer == 14 and red >= 3 and numbers[3] >= 7 and numbers[7] >= 7:
              nomer += 1
              rec = "15"
            elif nomer == 15 and black >= 3 and numbers[4] >= 7 and numbers[8] >= 7:
              nomer += 1
              rec = "16"
            elif nomer == 16 and grey >= 3 and numbers[5] >= 7 and numbers[9] >= 7:
              nomer += 1
              rec = "17"
            elif nomer == 17 and red >= 3 and numbers[6] >= 7 and numbers[10] >= 7:
              nomer += 1
              rec = "18"
            else:
              rec = "-"
          else:
            rec = "-"
        else:
          rec = "-"
        if da == 1:
          table1 = Table(number=ch, recom=rec,
                         previous=last_rec, success='t')
          table1.save()
        elif da == 2:
          table1 = Table(number=ch, recom=rec,
                         previous=last_rec, success='f')
          table1.save()
        else:
          table1 = Table(number=ch, recom=rec,
                         previous=last_rec, success='n')
          table1.save()
        last_rec = rec
      else:
        print('Error')
    elif d3.minute % 2 == 0 and bo != 1:
      bo = 1
