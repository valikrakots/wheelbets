
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
chislo = 0
grey = 0
red = 0
black = 0
cup = 0
kolvo = 0
h = 9
d1 = datetime.datetime.now().date()
promezh = [0] * 3
promezh_kolvo = [0] * 3
bome = [0] * 2
bome_prom = [0] * 2
czetn = [0] * 2
czetn_prom = [0] * 2


def cronjob():
  global numbers
  global numbers_kolvo
  global red_kolvo
  global black_kolvo
  global grey_kolvo
  global cup_kolvo
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
  global czetn
  global czetn_prom
  rec = "-"
  bo = 1
  last_rec = "-"
  while(h == 9):
    d2 = datetime.datetime.now().date()
    d3 = datetime.datetime.now()
    if (d3.hour == 5 and d3.minute == 59) or d3.hour == 6:
      if bo == 2:
        table1 = Table(number='w',
                       recom='w', success='w', previous='w')
        table1.save()
        bo = 3
    elif(d3.minute % 2 == 1 and d3.second == 25 and bo == 1):
      bo = 2
      if d1 < d2:
        d1 = datetime.datetime.now().date()
        table1 = Table(number='ch',
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
        f = 0
        while f < 2:
          bome_prom[f] += 1
          f += 1
        f = 0
        while f < 2:
          czetn_prom[f] += 1
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
            czetn[1] += 1
            czetn_prom[1] = 0
            bome[0] += 1
            bome_prom[0] = 0
            promezh_kolvo[0] += 1
            promezh[0] = 0
            numbers[1] = 0
            numbers_kolvo[1] += 1
          elif ch == '8':
            czetn[1] += 1
            czetn_prom[1] = 0
            bome[0] += 1
            bome_prom[0] = 0
            promezh_kolvo[1] += 1
            promezh[1] = 0
            numbers[7] = 0
            numbers_kolvo[7] += 1
          elif ch == '5':
            czetn[0] += 1
            czetn_prom[0] = 0
            bome[0] += 1
            bome_prom[0] = 0
            promezh_kolvo[0] += 1
            promezh[0] = 0
            numbers[4] = 0
            numbers_kolvo[4] += 1
        elif(htmlu[k + 150] == '"' and htmlu[k + 161] == 'r'):
          ch = htmlu[k + 149]
          grey += 1
          red = 0
          black += 1
          cup += 1
          red_kolvo += 1
          if ch == '3':
            czetn[0] += 1
            czetn_prom[0] = 0
            bome[0] += 1
            bome_prom[0] = 0
            promezh_kolvo[0] += 1
            promezh[0] = 0
            numbers[2] = 0
            numbers_kolvo[2] += 1
          elif ch == '9':
            czetn[0] += 1
            czetn_prom[0] = 0
            bome[0] += 1
            bome_prom[0] = 0
            promezh_kolvo[1] += 1
            promezh[1] = 0
            numbers[8] = 0
            numbers_kolvo[8] += 1
          elif ch == '6':
            czetn[1] += 1
            czetn_prom[1] = 0
            bome[0] += 1
            bome_prom[0] = 0
            promezh_kolvo[0] += 1
            promezh[0] = 0
            numbers[5] = 0
            numbers_kolvo[5] += 1
        elif(htmlu[k + 150] == '"' and htmlu[k + 161] == 'b'):
          ch = htmlu[k + 149]
          red += 1
          grey += 1
          black = 0
          cup += 1
          black_kolvo += 1
          if ch == '1':
            czetn[0] += 1
            czetn_prom[0] = 0
            bome[0] += 1
            bome_prom[0] = 0
            promezh_kolvo[0] += 1
            promezh[0] = 0
            numbers[0] = 0
            numbers_kolvo[0] += 1
          elif ch == '4':
            czetn[1] += 1
            czetn_prom[1] = 0
            bome[0] += 1
            bome_prom[0] = 0
            promezh_kolvo[0] += 1
            promezh[0] = 0
            numbers[3] = 0
            numbers_kolvo[3] += 1
          elif ch == '7':
            czetn[0] += 1
            czetn_prom[0] = 0
            bome[0] += 1
            bome_prom[0] = 0
            promezh_kolvo[1] += 1
            promezh[1] = 0
            numbers[6] = 0
            numbers_kolvo[6] += 1
        elif(htmlu[k + 149] == '0'):
          ch = htmlu[k + 149]
          red += 1
          grey += 1
          black += 1
          cup_kolvo += 1
          cup = 0
        elif(htmlu[k + 162] == 'r'):
          ch = htmlu[k + 149] + htmlu[k + 150]
          red = 0
          grey += 1
          black += 1
          cup += 1
          red_kolvo += 1
          if ch == '12':
            czetn[1] += 1
            czetn_prom[1] = 0
            bome[1] += 1
            bome_prom[1] = 0
            promezh_kolvo[1] += 1
            promezh[1] = 0
            numbers[11] = 0
            numbers_kolvo[11] += 1
          elif ch == '18':
            czetn[1] += 1
            czetn_prom[1] = 0
            bome[1] += 1
            bome_prom[1] = 0
            promezh_kolvo[2] += 1
            promezh[2] = 0
            numbers[17] = 0
            numbers_kolvo[17] += 1
          elif ch == '15':
            czetn[0] += 1
            czetn_prom[0] = 0
            bome[1] += 1
            bome_prom[1] = 0
            promezh_kolvo[2] += 1
            promezh[2] = 0
            numbers[14] = 0
            numbers_kolvo[14] += 1
        elif(htmlu[k + 162] == 'b'):
          ch = htmlu[k + 149] + htmlu[k + 150]
          black = 0
          red += 1
          grey += 1
          cup += 1
          black_kolvo += 1
          if ch == '10':
            czetn[1] += 1
            czetn_prom[1] = 0
            bome[1] += 1
            bome_prom[1] = 0
            promezh_kolvo[1] += 1
            promezh[1] = 0
            numbers[9] = 0
            numbers_kolvo[9] += 1
          elif ch == '13':
            czetn[0] += 1
            czetn_prom[0] = 0
            bome[1] += 1
            bome_prom[1] = 0
            promezh_kolvo[2] += 1
            promezh[2] = 0
            numbers[12] = 0
            numbers_kolvo[12] += 1
          elif ch == '16':
            czetn[1] += 1
            czetn_prom[1] = 0
            bome[1] += 1
            bome_prom[1] = 0
            promezh_kolvo[2] += 1
            promezh[2] = 0
            numbers[15] = 0
            numbers_kolvo[15] += 1
        elif(htmlu[k + 162] == 'g'):
          ch = htmlu[k + 149] + htmlu[k + 150]
          grey = 0
          red += 1
          black += 1
          cup += 1
          grey_kolvo += 1
          if ch == '11':
            czetn[0] += 1
            czetn_prom[0] = 0
            bome[1] += 1
            bome_prom[1] = 0
            promezh_kolvo[1] += 1
            promezh[1] = 0
            numbers[10] = 0
            numbers_kolvo[10] += 1
          elif ch == '14':
            czetn[1] += 1
            czetn_prom[1] = 0
            bome[1] += 1
            bome_prom[1] = 0
            promezh_kolvo[2] += 1
            promezh[2] = 0
            numbers[13] = 0
            numbers_kolvo[13] += 1
          elif ch == '17':
            czetn[0] += 1
            czetn_prom[0] = 0
            bome[1] += 1
            bome_prom[1] = 0
            promezh_kolvo[2] += 1
            promezh[2] = 0
            numbers[16] = 0
            numbers_kolvo[16] += 1
        minimum = 0
        pervyj = 0
        nomer = 0
        sczetczik = 0
        kkk = 0
        for num in numbers:
          if pervyj == 0 and num > 40:
            pervyj = 1
            kkk = 1
            minimum = num
            nomer = sczetczik
          elif pervyj != 0:
            if num > minimum:
              kkk = 1
              minimum = num
              nomer = sczetczik
            elif num == minimum and num > 40:
              kkk += 1
          sczetczik += 1
        da = 2
        r = '-'
        if rec == "< 9.5" and len(ch) == 1:
          da = 1
        elif rec == "> 9.5" and len(ch) == 2:
          da = 1
        elif rec == "чет" and (int(ch)) % 2 == 0:
          da = 1
        elif rec == "нечет" and (int(ch)) % 2 == 1:
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
        elif rec == 'cup' and ch == '0':
          da = 1
        elif rec == '-':
          da = 3
        if kolvo != cup_kolvo and bome[0] / (kolvo - cup_kolvo) <= 0.4 and bome_prom[0] >= 5:
          rec = "< 9.5"
        elif kolvo != cup_kolvo and bome[1] / (kolvo - cup_kolvo) <= 0.4 and bome_prom[1] >= 5:
          rec = "> 9.5"
        elif kolvo != cup_kolvo and czetn[0] / (kolvo - cup_kolvo) <= 0.4 and czetn_prom[0] >= 5:
          rec = "нечет"
        elif kolvo != cup_kolvo and czetn[1] / (kolvo - cup_kolvo) <= 0.4 and czetn_prom[1] >= 5:
          rec = "чет"
        elif kolvo != cup_kolvo and promezh[0] >= 9 and promezh_kolvo[0] / (kolvo - cup_kolvo) <= 0.25:
          rec = "1-6"
        elif kolvo != cup_kolvo and promezh[1] >= 9 and promezh_kolvo[1] / (kolvo - cup_kolvo) <= 0.25:
          rec = "7-12"
        elif kolvo != cup_kolvo and promezh[2] >= 9 and promezh_kolvo[2] / (kolvo - cup_kolvo) <= 0.25:
          rec = "13-18"
        elif kolvo != cup_kolvo and red >= 9 and red_kolvo / (kolvo - cup_kolvo) <= 0.35:
          rec = "red"
        elif kolvo != cup_kolvo and black >= 9 and black_kolvo / (kolvo - cup_kolvo) <= 0.35:
          rec = "black"
        elif kolvo != cup_kolvo and grey >= 9 and grey_kolvo / (kolvo - cup_kolvo) <= 0.35:
          rec = "grey"
        elif kolvo != cup_kolvo and cup > 40 and cup_kolvo / kolvo <= 0.049 and numbers[11] >= 3 and numbers[0] >= 3 and numbers_kolvo[0] / kolvo < 0.05 and numbers_kolvo[11] / kolvo < 0.05:
          rec = "cup"
        elif kkk == 1:
          if kolvo != cup_kolvo and numbers_kolvo[nomer] / kolvo <= 0.049:
            if nomer == 0 and numbers[7] >= 3 and cup >= 3 and black_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[7] / kolvo < 0.05 and cup_kolvo / kolvo < 0.05:
              nomer += 1
              rec = "1"
            elif nomer == 1 and numbers[8] >= 3 and numbers[12] >= 3 and grey_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[8] / kolvo < 0.05 and numbers_kolvo[12] / kolvo < 0.05:
              nomer += 1
              rec = "2"
            elif nomer == 2 and numbers[9] >= 3 and numbers[13] >= 3 and red_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[9] / kolvo < 0.05 and numbers_kolvo[13] / kolvo < 0.05:
              nomer += 1
              rec = "3"
            elif nomer == 3 and numbers[14] >= 3 and numbers[10] >= 3 and black_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[10] / kolvo < 0.05 and numbers_kolvo[14] / kolvo < 0.05:
              nomer += 1
              rec = "4"
            elif nomer == 4 and numbers[15] >= 3 and numbers[11] >= 3 and grey_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[11] / kolvo < 0.05 and numbers_kolvo[15] / kolvo < 0.05:
              nomer += 1
              rec = "5"
            elif nomer == 5 and numbers[12] >= 3 and numbers[16] >= 3 and red_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[12] / kolvo < 0.05 and numbers_kolvo[16] / kolvo < 0.05:
              nomer += 1
              rec = "6"
            elif nomer == 6 and numbers[13] >= 3 and numbers[17] >= 3 and black_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[13] / kolvo < 0.05 and numbers_kolvo[17] / kolvo < 0.05:
              nomer += 1
              rec = "7"
            elif nomer == 7 and numbers[0] >= 3 and numbers[14] >= 3 and grey_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[14] / kolvo < 0.05 and numbers_kolvo[0] / kolvo < 0.05:
              nomer += 1
              rec = "8"
            elif nomer == 8 and numbers[15] >= 3 and numbers[1] >= 3 and red_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[15] / kolvo < 0.05 and numbers_kolvo[1] / kolvo < 0.05:
              nomer += 1
              rec = "9"
            elif nomer == 9 and numbers[2] >= 3 and numbers[16] >= 3 and black_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[16] / kolvo < 0.05 and numbers_kolvo[2] / kolvo < 0.05:
              nomer += 1
              rec = "10"
            elif nomer == 10 and numbers[3] >= 3 and numbers[17] >= 3 and grey_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[17] / kolvo < 0.05 and numbers_kolvo[3] / kolvo < 0.05:
              nomer += 1
              rec = "11"
            elif nomer == 11 and numbers[4] >= 3 and cup >= 3 and red_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[4] / kolvo < 0.05 and cup_kolvo / kolvo < 0.05:
              nomer += 1
              rec = "12"
            elif nomer == 12 and numbers[1] >= 3 and numbers[5] >= 3 and black_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[5] / kolvo < 0.05 and numbers_kolvo[1] / kolvo < 0.05:
              nomer += 1
              rec = "13"
            elif nomer == 13 and numbers[2] >= 3 and numbers[6] >= 3 and grey_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[6] / kolvo < 0.05 and numbers_kolvo[2] / kolvo < 0.05:
              nomer += 1
              rec = "14"
            elif nomer == 14 and numbers[3] >= 3 and numbers[7] >= 3 and red_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[7] / kolvo < 0.05 and numbers_kolvo[3] / kolvo < 0.05:
              nomer += 1
              rec = "15"
            elif nomer == 15 and numbers[4] >= 3 and numbers[8] >= 3 and black_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[8] / kolvo < 0.05 and numbers_kolvo[4] / kolvo < 0.05:
              nomer += 1
              rec = "16"
            elif nomer == 16 and numbers[5] >= 3 and numbers[9] >= 3 and grey_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[9] / kolvo < 0.05 and numbers_kolvo[5] / kolvo < 0.05:
              nomer += 1
              rec = "17"
            elif nomer == 17 and numbers[6] >= 3 and numbers[10] >= 3 and red_kolvo / (kolvo - cup_kolvo) < 0.38 and numbers_kolvo[10] / kolvo < 0.05 and numbers_kolvo[6] / kolvo < 0.05:
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
