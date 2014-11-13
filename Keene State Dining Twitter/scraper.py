__author__ = 'peiggs'

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from bs4 import BeautifulSoup
from urllib.request import urlopen
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


stack = []
for node in soup.findAll('span',attrs={'class': 'ul'}):
    food.append((node.findAll(text=True)[0]))
menuCounter = 0
flag = True
flag2 = True
for menuItem in food:
    todayMenu.append(menuItem)
    menuCounter = menuCounter +1
     #Means if the day of Week is not Saturday or Sunday (No breakfast those days!)if day != 5 and day != 6
    str(menuItem)
    if menuItem == "Scrambled Eggs": #This is the entire Day's Menu M-F
        flag = False


    if menuItem == ("French Fries" or "Curly French Fries") and flag2:

        flag2 = False

    if menuItem == "Scrambled Eggs":
        tempCounter = menuCounter - 1
        stack.append(tempCounter)




print(stack)
monday = todayMenu[stack[0]:stack[1]]

tuesday = todayMenu[stack[1]:stack[2]]
wednesday = todayMenu[stack[2]:stack[3]]
thursday = todayMenu[stack[3]:stack[4]]
friday = todayMenu[stack[4]:stack[5]]
print(monday)
print(tuesday)
print(wednesday)
print(thursday)
sunday = todayMenu
print(friday)
   # elif day == 6:

   # elif day == 5:



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
    for item in monday:
        item = str(item)
        y = len(monday)
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





