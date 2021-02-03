# import cv2
from blog.models import Table
from blog.models import TableImage
from blog.models import MyErrors
import time
from django.utils import timezone
import requests
from bs4 import BeautifulSoup
import datetime
import threading
import face_recognition
import os
from selenium import webdriver
from time import sleep
from PIL import Image, ImageEnhance
import base64
import io
import cv2
from io import BytesIO


URL = 'https://betgames9.betgames.tv/ext/game_results/get_results_info/testpartner/2019-04-03/0/1/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0',
           'accept': '*/*'}


def get_html(url, params=None):
  r = requests.get(url, headers=HEADERS, params=params)
  return r


d1 = datetime.datetime.now().date()


def cronjob():
  global d1
  current = 0
  peremennaya = 0
  face_cascade = cv2.CascadeClassifier(
      'haarcascade_frontalface_default.xml')
  # face_count = 1
  resultaty = []
  known_faces = []
  known_names = []
  heights = []
  times = []
  new_face_found = False
  rec = "-"
  bo = 1
  last_rec = "-"
  da = 0
  do = 1
  last_ch = '-1'
  d3 = datetime.datetime.now()
  while(d3.minute % 2 == 1):
    d3 = datetime.datetime.now()
  while(d3.second < 25):
    d3 = datetime.datetime.now()
  chrome_options = webdriver.ChromeOptions()
  chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
  chrome_options.add_argument("--headless")
  chrome_options.add_argument("--disable-dev-shm-usage")
  chrome_options.add_argument("--no-sandbox")
  driver = webdriver.Chrome(executable_path=os.environ.get(
      "CHROMEDRIVER_PATH"), chrome_options=chrome_options)
  driver.get('https://demo.betgames.tv')
  sleep(1)
  driver.switch_to_frame("betgames_iframe_1")
  sleep(6)
  # element = driver.find_elements_by_css_selector(
  #    "div[data-qa='button-game-menu-7']")
  # element[0].click()
  # element = driver.find_elements_by_css_selector(
  #    "div.tabs-bar-item align-center > button[type=button")
  element = driver.find_elements_by_css_selector('.tabs-bar-item.align-center')
  driver.execute_script("arguments[0].click();", element[6])
  # element[0].click()
  sleep(10)
  screenshot_img = driver.get_screenshot_as_png()
  # encoded = base64.b64encode(screenshot_img)
  # im_bytes = base64.b64decode(encoded)
  # im_file = BytesIO(im_bytes)
  # im_file.seek(0)
  # img = Image.open(im_file)
  img = Image.open(BytesIO(screenshot_img))
  img.save('foo.png', quality=95)
  img = Image.open('foo.png')
  rgb_img = img.convert('RGB')
  area = (255, 135, 450, 300)
  rgb_img2 = rgb_img.crop(area)
  rgb_img2.save('poo.jpg', quality=95)
  sleep(1)
  driver.quit()
  img1 = cv2.imread('poo.jpg')
  gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
  cv2.imwrite('poo3.jpg', gray)

  imgjpg = Image.open("poo.jpg")

  # imgjpg = Image.open("poo.jpg")    recently
  # table1 = Imager(im=encoded)
  # table1.save()
  faces = face_cascade.detectMultiScale(gray, 1.05, 10, minSize=(21, 21))

  if len(faces) == 0:
    print('(My Error) There are 0 faces.\n')
    with open("poo.jpg", "rb") as img_file:
      encoded = base64.b64encode(img_file.read())
    table1 = MyErrors(time=timezone.now(), ime=encoded)
    table1.save()

  elif len(faces) > 1:
    print('(My Error) There are more than 1 faces.\n')
    print("The number of faces is: ")
    print(len(faces))
    print('\n')
    for(x, y, w, h) in faces:
      area = (x, y, x + w, y + h)
      img2 = imgjpg.crop(area)
      img2.save("poo2.jpg")
      with open("poo2.jpg", "rb") as img_file:
        encoded = base64.b64encode(img_file.read())
      table1 = MyErrors(time=timezone.now(), ime=encoded)
      table1.save()
      os.remove("poo2.jpg")

  for(x, y, w, h) in faces:
    area = (x - 15, y - 15, x + w + 15, y + h + 15)
    img2 = imgjpg.crop(area)
    img2 = img2.resize((85, 85))
    img2.save("poo4.jpg", quality=95)
    img3 = Image.open("poo4.jpg")
    enhancer = ImageEnhance.Sharpness(img3)
    enhanced_im = enhancer.enhance(3.4)
    enhanced_im.save("poo2.jpg")
    with open("poo2.jpg", "rb") as img_file:
      encoded = base64.b64encode(img_file.read())
    # img2 = imgjpg[y:y + h, x:x + w]
    image = face_recognition.load_image_file("poo2.jpg", mode='RGB')
    encodings = face_recognition.face_encodings(image)
    if len(encodings) == 0:
      print("No face found.")
      table1 = TableImage(firsttime=timezone.now(),
                          time=timezone.now(), byl="no face", im=encoded)
      table1.save()
      os.remove("poo2.jpg")
      os.remove("poo4.jpg")
      continue
    table1 = TableImage(firsttime=timezone.now(),
                        time=timezone.now(), byl="no", im=encoded)
    table1.save()
    encoding = encodings[0]
    print("No face recognized.\n")
    known_faces.append(encoding)
    known_names.append(peremennaya)
    heights.append(y)
    peremennaya += 1
    times.append(timezone.now())
    os.remove("poo2.jpg")
    os.remove("poo4.jpg")
  # os.remove("foo.png")
  os.remove("foo.png")
  os.remove("poo.jpg")
  os.remove("poo3.jpg")
  while(True):
    d2 = datetime.datetime.now().date()
    d3 = datetime.datetime.now()
    if (d3.minute == 28 or d3.minute == 58 or d3.minute == 0 or d3.minute == 30 or d3.minute == 2 or d3.minute == 32 or d3.minute == 4 or d3.minute == 34) and do == 2 and d3.second == 20 and new_face_found == False:
      do = 1
      chrome_options = webdriver.ChromeOptions()
      chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
      chrome_options.add_argument("--headless")
      chrome_options.add_argument("--disable-dev-shm-usage")
      chrome_options.add_argument("--no-sandbox")
      driver = webdriver.Chrome(executable_path=os.environ.get(
          "CHROMEDRIVER_PATH"), chrome_options=chrome_options)
      driver.get('https://demo.betgames.tv')
      sleep(1)
      driver.switch_to_frame("betgames_iframe_1")
      sleep(6)
      # element = driver.find_elements_by_css_selector(
      #    "div[data-qa='button-game-menu-7']")
      # element = driver.find_elements_by_css_selector(
      #    "div[class*=tabs-bar-item]")
      # element[6].click()
      element = driver.find_elements_by_css_selector(
          '.tabs-bar-item.align-center')
      driver.execute_script("arguments[0].click();", element[6])
      sleep(10)
      screenshot_img = driver.get_screenshot_as_png()
      # encoded = base64.b64encode(screenshot_img)
      # im_bytes = base64.b64decode(encoded)
      # im_file = BytesIO(im_bytes)
      # img = Image.open(im_file)
      img = Image.open(BytesIO(screenshot_img))
      img.save('foo.png', quality=95)
      img = Image.open('foo.png')
      rgb_img = img.convert('RGB')
      area = (255, 135, 450, 300)
      rgb_img2 = rgb_img.crop(area)
      rgb_img2.save('poo.jpg', quality=95)
      # face_count += 1
      # face_filename = '%s%d.png' % ('foo', face_count)
      # img.save('%s%d.png', '')
      sleep(1)
      driver.quit()
      img1 = cv2.imread('poo.jpg')
      gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
      faces = face_cascade.detectMultiScale(gray, 1.05, 9, minSize=(21, 21))

      cv2.imwrite('poo3.jpg', gray)
      imgjpg = Image.open("poo.jpg")

      if len(faces) == 0:
        print('(My Error) There are 0 faces.\n')
        with open("poo.jpg", "rb") as img_file:
          encoded = base64.b64encode(img_file.read())
        current = -1
        if (d3.minute == 34 or d3.minute == 4):
          table1 = TableImage(firsttime=timezone.now(),
                              time=timezone.now(), byl="netu lica", im=encoded)
          table1.save()
        table1 = MyErrors(time=timezone.now(), ime=encoded)
        table1.save()
        enhancer = ImageEnhance.Sharpness(imgjpg)
        enhanced_im = enhancer.enhance(3.4)
        enhanced_im.save("poo2.jpg")
        with open("poo2.jpg", "rb") as img_file:
          encoded = base64.b64encode(img_file.read())
        image = face_recognition.load_image_file("poo2.jpg", mode='RGB')
        encodings = face_recognition.face_encodings(image)
        if len(encodings) != 0:
          current = peremennaya - 1
          encoding = encodings[0]
          results = face_recognition.compare_faces(
              known_faces, encoding, 0.52)   # lower is more strict
          if True in results:
            print("But facerecognizer found. Face recognized\n")
            if(current != known_names[results.index(True)]):
              new_face_found = True
              current = known_names[results.index(True)]
              table1 = TableImage(firsttime=timezone.now(),
                                  time=timezone.now(), byl="yes", im=encoded)
              table1.firsttime = times[current]
              table1.byl = "yes"
              table1.save()
          else:
            print("But facerecognizer found. No face recognized\n")
            table1 = TableImage(firsttime=timezone.now(),
                                time=timezone.now(), byl="no", im=encoded)
            table1.save()
            new_face_found = True
            known_faces.append(encoding)
            known_names.append(peremennaya)
            current = peremennaya
            peremennaya += 1
            times.append(timezone.now())
        else:
          print("But facerecognizer found: No face found.\n")
          current = -1
        os.remove("poo2.jpg")

      elif len(faces) > 1:
        print('(My Error) There are more than 1 faces.\n')
        print("The number of faces is: ")
        print(len(faces))
        print('\n')
        for(x, y, w, h) in faces:
          area = (x, y, x + w, y + h)
          img2 = imgjpg.crop(area)
          img2.save("poo2.jpg")
          with open("poo2.jpg", "rb") as img_file:
            encoded = base64.b64encode(img_file.read())
          table1 = MyErrors(time=timezone.now(), ime=encoded)
          table1.save()
          os.remove("poo2.jpg")

      for(x, y, w, h) in faces:
        if new_face_found == True:
          continue
        # img2 = imgjpg[y:y + h, x:x + w]
        area = (x - 15, y - 15, x + w + 15, y + h + 15)
        img2 = imgjpg.crop(area)
        img2 = img2.resize((85, 85))
        img2.save("poo4.jpg", quality=95)
        img3 = Image.open("poo4.jpg")
        enhancer = ImageEnhance.Sharpness(img3)
        enhanced_im = enhancer.enhance(3.4)
        enhanced_im.save("poo2.jpg")
        with open("poo2.jpg", "rb") as img_file:
          encoded = base64.b64encode(img_file.read())
        image = face_recognition.load_image_file("poo2.jpg", mode='RGB')
        encodings = face_recognition.face_encodings(image)
        if len(encodings) != 0:
          current = peremennaya - 1
          encoding = encodings[0]
          results = face_recognition.compare_faces(
              known_faces, encoding, 0.57)   # lower is more strict
          if True in results:
            print("Face recognized\n")
            if current != known_names[results.index(True)] and abs(y - heights[results.index(True)]) < 5:
              new_face_found = True
              current = known_names[results.index(True)]
              table1 = TableImage(firsttime=timezone.now(),
                                  time=timezone.now(), byl="yes", im=encoded)
              table1.firsttime = times[current]
              table1.byl = "yes"
              table1.save()
          else:
            print("No face recognized\n")
            table1 = TableImage(firsttime=timezone.now(),
                                time=timezone.now(), byl="no", im=encoded)
            table1.save()
            new_face_found = True
            known_faces.append(encoding)
            known_names.append(peremennaya)
            heights.append(y)
            current = peremennaya
            peremennaya += 1
            times.append(timezone.now())
        else:
          print("No face found.\n")
          current = -1
          if (d3.minute == 34 or d3.minute == 4):
            table1 = TableImage(firsttime=timezone.now(),
                                time=timezone.now(), byl="nothing", im=encoded)
            table1.save()
        os.remove("poo2.jpg")
        os.remove("poo4.jpg")
      os.remove("foo.png")
      os.remove("poo.jpg")
      os.remove("poo3.jpg")
    elif(d3.minute % 2 == 1 and d3.second == 25 and bo == 1):

      bo = 2
      do = 2

      if d1 < d2:
        d1 = datetime.datetime.now().date()
        table1 = Table(number='ch',
                       recom='ch', success='e', previous='e')
        table1.save()

      html = get_html(URL)
      if html.status_code == 200 and current != -1:

        if (len(resultaty) - 1) < current:
          resi = []
          resultaty.append(resi)
          i = 0
          while i < 19:
            resi = []
            resultaty[current].append(resi)
            i2 = 0
            for i2 in range(19):
              resultaty[current][i].append(0)
            i += 1

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

        if(ch == '0' or ch == '1' or ch == '2' or ch == '3' or ch == '4' or ch == '5' or ch == '6' or ch == '7' or ch == '8' or ch == '9' or ch == '10' or ch == '11' or ch == '12' or ch == '13' or ch == '14' or ch == '15' or ch == '16' or ch == '17' or ch == '18'):

          if rec == ch:
            da = 1
          elif rec == 'cup' and ch == '0':
            da = 1
          elif rec == '-':
            da = 3
          else:
            da = 2

          chislo = int(ch)
          if last_ch != '-1':
            last_chislo = int(last_ch)
            resultaty[current][last_chislo][chislo] += 1

          last_rec = rec
          rec = '-'

          print("Current leader: ")
          print(current)
          print('\n')
          print("Last number: ")
          print(chislo)
          print('\n')

          maxi = 0
          last_maxi = 0
          maxi_czislo = -1
          i = 0

          while i < 19:
            if(resultaty[current][chislo][i] > maxi):
              last_maxi = maxi
              maxi = resultaty[current][chislo][i]
              maxi_czislo = i
            i += 1

          if(maxi_czislo != -1 and last_maxi != 0 and maxi / last_maxi >= 1.4):
            rec = str(maxi_czislo)
            print("Sootnoszenie:")
            print(maxi / last_maxi)
            print('\n')

          print("The recomended one: ")
          print(rec)
          print("\n")

          print("Peremennaya: ")
          print(peremennaya)
          print("\n")

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

          last_ch = ch

      elif current == -1:
        print("Current = -1\n")

      else:
        print('Error')

    elif d3.minute % 2 == 0 and bo != 1:
      bo = 1

    if (d3.minute == 5 or d3.minute == 35) and new_face_found != False:
      new_face_found = False
