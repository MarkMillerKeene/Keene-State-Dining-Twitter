__author__ = 'peiggs'

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageFilter
import random
from bs4 import BeautifulSoup
import io
from urllib.request import urlopen
import glob, os
import time
import datetime

site = "https://keenestatedining.sodexomyway.com/images/WeeklyMenu_tcm575-2231.htm"
page = urlopen(site) #Sets url to the command Ello profile
soup = BeautifulSoup(page) #uses beautiful soup module to arrange html data
food = []
todayMenu = []


day = datetime.datetime.today().weekday()
week=['Monday',
      'Tuesday',
      'Wednesday',
      'Thursday',
      'Friday',
      'Saturday',
      'Sunday']



for node in soup.findAll('span',attrs={'class': 'ul'}):
    #print(food.join(node.findAll(text=True)[0]))
    #print(node.findAll(text=True))
    #print(type(node))
    food.append((node.findAll(text=True)[0]))
todayMenu.append(week[day])
menuCounter = 0
def menuFiller(todayMenu, menuCounter):
    flag = True
    flag2 = True
    for menuItem in todayMenu:
        todayMenu.append(menuItem)
        menuCounter = menuCounter +1
         #Means if the day of Week is not Saturday or Sunday (No breakfast those days!)if day != 5 and day != 6
        str(menuItem)
        if menuItem == "Scrambled Eggs": #This is the entire Day's Menu M-F
            flag = False
        if menuItem == "Omelet Bar":
            todayMenu.append("Lunch:")
            menuCounter = menuCounter +1
        if menuItem =="French Fries" and flag2:
            todayMenu.append("Dinner:")
            menuCounter = menuCounter +1
            flag2 = False
        if menuItem == "Scrambled Eggs" and not flag:
                break


        todayMenu.append(menuItem)





   # elif day == 6:

   # elif day == 5:



menuFiller(todayMenu, menuCounter)


if __name__ == '__main__':

    fontname = "Arial.ttf"
    fontsize = 18



    colorText = "black"
    colorOutline = "red"
    colorBackground = "white"


    font = ImageFont.truetype(fontname, fontsize)
    width, height = 1000, 1000
    img = Image.new('RGB', (width+4, height+4), colorBackground)
    d = ImageDraw.Draw(img)
    count = 0
    for item in todayMenu:
        item = str(item)
        y = len(todayMenu)
        x= 20
        if item not in week:
            x = x+200
            fontsize = 40
        if item == "Lunch:":
            x = 20
        if item == "Dinner:":
            x = 20
        count = count +28 #spacing between the menu items
        d.text((x, height/y+count), item, fill=colorText, font=font)
    d.rectangle((0, 0, width+3, height+3), outline=colorOutline)

    img.save("D:/image.png")


    img.show()





