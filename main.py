
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
  one = 0
  two = 0
  three = 0
  four = 0
  five = 0
  six = 0
  seven = 0
  eight = 0
  nine = 0
  ten = 0
  eleven = 0
  twelve = 0
  thirteen = 0
  fourteen = 0
  fiveteen = 0
  sixteen = 0
  seventeen = 0
  eighteen = 0
  one_kolvo = 0
  two_kolvo = 0
  three_kolvo = 0
  four_kolvo = 0
  five_kolvo = 0
  six_kolvo = 0
  seven_kolvo = 0
  eight_kolvo = 0
  nine_kolvo = 0
  ten_kolvo = 0
  eleven_kolvo = 0
  twelve_kolvo = 0
  thirteen_kolvo = 0
  fourteen_kolvo = 0
  fiveteen_kolvo = 0
  sixteen_kolvo = 0
  seventeen_kolvo = 0
  eighteen_kolvo = 0
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
        one += 1
        two += 1
        three += 1
        four += 1
        five += 1
        six += 1
        seven += 1
        eight += 1
        nine += 1
        ten += 1
        eleven += 1
        twelve += 1
        thirteen += 1
        fourteen += 1
        fiveteen += 1
        sixteen += 1
        seventeen += 1
        eighteen += 1
        if ch == '2':
          two = 0
          two_kolvo += 1
        elif ch == '8':
          eight = 0
          eight_kolvo += 1
        elif ch == '5':
          five = 0
          five_kolvo += 1
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
        one += 1
        two += 1
        three += 1
        four += 1
        five += 1
        six += 1
        seven += 1
        eight += 1
        nine += 1
        ten += 1
        eleven += 1
        twelve += 1
        thirteen += 1
        fourteen += 1
        fiveteen += 1
        sixteen += 1
        seventeen += 1
        eighteen += 1
        if ch == '3':
          three = 0
          three_kolvo += 1
        elif ch == '9':
          nine = 0
          nine_kolvo += 1
        elif ch == '6':
          six = 0
          six_kolvo += 1
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
        one += 1
        two += 1
        three += 1
        four += 1
        five += 1
        six += 1
        seven += 1
        eight += 1
        nine += 1
        ten += 1
        eleven += 1
        twelve += 1
        thirteen += 1
        fourteen += 1
        fiveteen += 1
        sixteen += 1
        seventeen += 1
        eighteen += 1
        if ch == '1':
          one = 0
          one_kolvo += 1
        elif ch == '4':
          four = 0
          four_kolvo += 1
        elif ch == '7':
          seven = 0
          seven_kolvo += 1
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
        one += 1
        two += 1
        three += 1
        four += 1
        five += 1
        six += 1
        seven += 1
        eight += 1
        nine += 1
        ten += 1
        eleven += 1
        twelve += 1
        thirteen += 1
        fourteen += 1
        fiveteen += 1
        sixteen += 1
        seventeen += 1
        eighteen += 1
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
        one += 1
        two += 1
        three += 1
        four += 1
        five += 1
        six += 1
        seven += 1
        eight += 1
        nine += 1
        ten += 1
        eleven += 1
        twelve += 1
        thirteen += 1
        fourteen += 1
        fiveteen += 1
        sixteen += 1
        seventeen += 1
        eighteen += 1
        if ch == '12':
          twelve = 0
          twelve_kolvo += 1
        elif ch == '18':
          eighteen = 0
          eighteen_kolvo += 1
        elif ch == '15':
          fiveteen = 0
          fiveteen_kolvo += 1
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
        one += 1
        two += 1
        three += 1
        four += 1
        five += 1
        six += 1
        seven += 1
        eight += 1
        nine += 1
        ten += 1
        eleven += 1
        twelve += 1
        thirteen += 1
        fourteen += 1
        fiveteen += 1
        sixteen += 1
        seventeen += 1
        eighteen += 1
        if ch == '10':
          ten = 0
          ten_kolvo += 1
        elif ch == '13':
          thirteen = 0
          thirteen_kolvo += 1
        elif ch == '16':
          sixteen = 0
          sixteen_kolvo += 1
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
        one += 1
        two += 1
        three += 1
        four += 1
        five += 1
        six += 1
        seven += 1
        eight += 1
        nine += 1
        ten += 1
        eleven += 1
        twelve += 1
        thirteen += 1
        fourteen += 1
        fiveteen += 1
        sixteen += 1
        seventeen += 1
        eighteen += 1
        if ch == '11':
          eleven = 0
          eleven_kolvo += 1
        elif ch == '14':
          fourteen = 0
          fourteen_kolvo += 1
        elif ch == '17':
          seventeen = 0
          seventeen_kolvo += 1
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
    time.sleep(119.7405)
