import cv2
from blog.models import Table
import time
import requests
from bs4 import BeautifulSoup
import datetime
import threading
import face_recognition
import numpy as np
import os
from selenium import webdriver
from time import sleep
from PIL import Image




URL = 'https://betgames9.betgames.tv/ext/game_results/get_results_info/testpartner/2019-04-03/0/1/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
           'accept': '*/*'}


def get_html(url, params=None):
  r = requests.get(url, headers=HEADERS, params=params)
  return r


def stringToRGB(base64_string):
    imgdata = base64.b64decode(str(base64_string))
    image = Image.open(io.BytesIO(imgdata))
    return cv2.cvtColor(np.array(image), cv2.COLOR_BGR2RGB)



d1 = datetime.datetime.now().date()


def cronjob():
  global d1
  known_faces = []
  known_names = []
  peremennaya = 0
  current = -1
  rec = "-"
  bo = 1
  last_rec = "-"
  da = 0
  do = 1
  while(True):
    d2 = datetime.datetime.now().date()
    d3 = datetime.datetime.now()
    if (d3.minute == 46 or d3.minute == 48) and do == 2:
      do = 1
      chrome_options = webdriver.ChromeOptions()
      chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
      chrome_options.add_argument("--headless")
      chrome_options.add_argument("--disable-dev-shm-usage")
      chrome_options.add_argument("--no-sandbox")
      driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
      driver.get('https://air2.parimatch.com/ru/betgames/')
      sleep(10)
      driver.find_elements_by_xpath("//*[contains(text(), 'Колесо')]").click()
      sleep(10)
      screenshot_img = driver.get_screenshot_as_png()
      screenshot = base64.encodestring(screenshot_img)
      image1 = stringToRGB(screenshot)
      driver.quit()
      image = face_recognition.load_image_file(image1)
      location = face_recognition.face_locations(image, "cnn")[0]
      encoding = face_locations.face_encodings(image,loctions)[0]
      table1 = Table(number='w',
                       recom='w', success='w', previous='w', image = screenshot)
      table1.save()
      results = face_recognition.compare_faces(known_faces, encoding, 0.6)
      if True in results:
        current = known_names[results.index(True)]
      else:
        known_faces.append(encoding)
        known_names.append(peremennaya)
        peremennaya += 1
    if (d3.hour == 5 and d3.minute == 59) or d3.hour == 6:
      if bo == 2:
        table1 = Table(number='w',
                       recom='w', success='w', previous='w', image = 'w')
        table1.save()
        bo = 3
    elif(d3.minute % 2 == 1 and d3.second == 25 and bo == 1):
      bo = 2
      if d1 < d2:
        d1 = datetime.datetime.now().date()
        table1 = Table(number='ch',
                       recom='ch', success='e', previous='e', image = 'e')
        table1.save()
      html = get_html(URL)
      if html.status_code == 200:
        do = 2
        ch = ""
        htmlu = html.text
        k = htmlu.find('"game_id":"7"')
        if(htmlu[k + 150] == '"' and htmlu[k + 161] == 'g'):
          ch = htmlu[k + 149]
        elif(htmlu[k + 150] == '"' and htmlu[k + 161] == 'r'):
          ch = htmlu[k + 149]
        elif(htmlu[k + 150] == '"' and htmlu[k + 161] == 'b'):
          ch = htmlu[k + 149]
        elif(htmlu[k + 149] == '0'):
          ch = htmlu[k + 149]
        elif(htmlu[k + 162] == 'r'):
          ch = htmlu[k + 149] + htmlu[k + 150]
        elif(htmlu[k + 162] == 'b'):
          ch = htmlu[k + 149] + htmlu[k + 150]
        elif(htmlu[k + 162] == 'g'):
          ch = htmlu[k + 149] + htmlu[k + 150]
        if rec ==  ch:
          da = 1
        elif rec == 'cup' and ch == '0':
          da = 1
        elif rec == '-':
          da = 3
        else:
          da = 2
        if da == 1:
          table1 = Table(number=ch, recom=rec,
                         previous=last_rec, success='t', image = 'e')
          table1.save()
        elif da == 2:
          table1 = Table(number=ch, recom=rec,
                         previous=last_rec, success='f', image = 'e')
          table1.save()
        else:
          table1 = Table(number=ch, recom=rec,
                         previous=last_rec, success='n', image = 'e')
          table1.save()
        last_rec = rec
      else:
        print('Error')
    elif d3.minute % 2 == 0 and bo != 1:
      bo = 1
