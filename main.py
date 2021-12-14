import random
from PIL import Image
import requests
import Pygame as py
import pandas as pd
from py import tool
from nltk import c #as a constant
from pd import sample
import map as mp
import bin

MAP_Y_START = 0
MAP_X_START = 0
MAP_Y_FINIAL = 3
MAP_X_FINIAL = 10
CARD_LIST_NUM = 10

card_name_list1 = [c.CARD_PEASHOOTER,  c.CARD_WALLNUT, c.FUMESHROOM, 
                c.CARD_CHOMPER, c.CARD_TWOPEASHOOTER]
plant_name_list = [c.CARD_PEASHOOTER,  c.CARD_WALLNUT, c.FUMESHROOM, 
                c.CARD_CHOMPER, c.CARD_TWOPEASHOOTER]
card_name_list2 = [c.CARD_NORMALZOMBIES, c.CARD_CONEHEADZOMBIES, c.BUCKHEADZOMBIE, 
                  c.CARD_FOOTBALLZOMBIE, c.CARD_POLEVAILTINGZOMBIE]
zombies_name_list = [c.CARD_NORMALZOMBIES, c.CARD_CONEHEADZOMBIES, c.BUCKHEADZOMBIE, 
                  c.CARD_FOOTBALLZOMBIE, c.CARD_POLEVAILTINGZOMBIE]
easy_plant = [c.CARD_PEASHOOTER,  c.CARD_WALLNUT]
hard_plant = [c.FUMESHROOM, c.CARD_CHOMPER, c.CARD_TWOPEASHOOTER]
easy_zombies = [c.CARD_NORMALZOMBIES, c.CARD_CONEHEADZOMBIES]
hard_zombies = [c.BUCKHEADZOMBIE, c.CARD_FOOTBALLZOMBIE, c.CARD_POLEVAILTINGZOMBIE]

def image_get_rect():
    url = input()
    image = Image.open(requests.get(url, stream=True).raw)
    return image


class Card():
    def __init__(self, x, y, name_index, scale=1): #数据可以改
        self.loadFrame(card_name_list1[name_index], scale)
        self.rect = self.image.get_rect()#记得补照片
        self.rect.x = x
        self.rect.y = y
        self.name_index = name_index
        self.select = True

        self.loadFrame(card_name_list2[name_index], scale)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name_index = name_index
        self.select = True


    def canClick(self):
        if self.exist:
            return True
        return False

    def canSelect(self):
        return self.select


class MenuBar():
    def __init__(self, card_list):
        self.loadFrame(c.card_name_list1, c.card_name_list2)
        self.rect = self.image_get_rect()
        self.rect.x = 10
        self.rect.y = 0
        self.setupCards(card_list)

    def loadFrame(self, name, image):#命名卡牌
        frame = tool[name]
        self.image = tool.get_image(name, image)


    def createImage(self):
        img = self.image
        rect = self.image_get_rect()
        width = rect.w
        height = rect.h
        self.image = py.Surface((width * 1, height)) #从Pygame 库里直接调用
        self.rect = self.image_get_rect()


    def randomCard(card_name_list1, card_name_list2, name):
        plant = []
        plant = df.sample(card_name_list1)
        plant = mp.showPlant()

        zombies = []
        zombies = df.sample(card_name_list2)
        zombies = mp.showZombies()

    def turn(self, time):
        time = ()
        if input() is True:
            time = input()
            return time
        else:
            time = (random.randint(0,10))


    def getCardPool(card_pool):
        card_pool = []


    def give_card(time, easy_plant, easy_zombies, hard_zombies, hard_plant):
        if time <= 10:
            card_pool = df.sample.replace(easy_plant, easy_zombies)#replace or not?
        else:
            card_pool = df.sample.replace(hard_zombies, hard_plant)
    

        




#if want add card   
#def getCardPool(data):
#   card_pool = []
#    for card in data:
#      tmp = card['name']
#      for i,name in enumerate(plant_name_list):
 #           if name == tmp:
 #               card_pool.append(i)
 #               break
#      for i,name in enumerate(zombies_name_list):
 #           if name == tmp:
  #              card_pool.append(i)
   #             break
 #   return card_pool
