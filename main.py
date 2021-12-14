import random
from PIL import Image # to get card image, let us see card imformation clearly
import requests # to get card image, let us see card imformation clearly
import Pygame as py
import pandas as pd
from py import tool # may using some tool
from nltk import c # as a constant
from pd import sample
import map as mp # we need a map for game
import bin #as a way of judging
import plant as pl
import mainquit


# the map size is constant
# it is 3*10 map
MAP_Y_START = 0
MAP_X_START = 0
MAP_Y_FINIAL = 3
MAP_X_FINIAL = 10
CARD_LIST_NUM = 10


# Following code set up main lists uning for plant and zombies
card_name_list1 = [c.CARD_PEASHOOTER,  c.CARD_WALLNUT, c.FUMESHROOM,
                c.CARD_CHOMPER, c.CARD_TWOPEASHOOTER]
plant_name_list = [c.CARD_PEASHOOTER,  c.CARD_WALLNUT, c.FUMESHROOM,
                c.CARD_CHOMPER, c.CARD_TWOPEASHOOTER]
card_name_list2 = [c.CARD_NORMALZOMBIES, c.CARD_CONEHEADZOMBIES, c.BUCKHEADZOMBIE,
                  c.CARD_FOOTBALLZOMBIE, c.CARD_POLEVAILTINGZOMBIE]
zombies_name_list = [c.CARD_NORMALZOMBIES, c.CARD_CONEHEADZOMBIES, c.BUCKHEADZOMBIE,
                  c.CARD_FOOTBALLZOMBIE, c.CARD_POLEVAILTINGZOMBIE]

# Different round will have different level of plant and zombie
# At first, there is easy zonbies vs easy plant
easy_plant = [c.CARD_PEASHOOTER,  c.CARD_WALLNUT]
hard_plant = [c.FUMESHROOM, c.CARD_CHOMPER, c.CARD_TWOPEASHOOTER]
easy_zombies = [c.CARD_NORMALZOMBIES, c.CARD_CONEHEADZOMBIES]
hard_zombies = [c.BUCKHEADZOMBIE, c.CARD_FOOTBALLZOMBIE, c.CARD_POLEVAILTINGZOMBIE]

# applying image for cards 
# we had images in github, but maybe they 
# can't go in to our project

def image_get_rect():
    url = input()
    image = Image.open(requests.get(url, stream=True).raw)
    return image


class Card():
    def __init__(self, x, y, name_index, scale=1):  #start for card
        self.loadFrame(card_name_list1[name_index], scale) # make a form for plants
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name_index = name_index
        self.image = py.Surface((width * 1, height * 2)) # a rectangle form card
        self.select = True # done for cards

        self.loadFrame(card_name_list2[name_index], scale)# make a form for zombies 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name_index = name_index
        self.select = True # done for cards


    def canClick(self): # make cards can be click
        if self.exist:
            return True
        return False

    def canSelect(self): # make cards can be select
        return self.select

# initial the menubar for playing
# where we get plant
class MenuBar():
    def __init__(self, card_list):  # initial a card list
        self.loadFrame(c.card_name_list1, c.card_name_list2)
        self.rect = self.image_get_rect()
        self.rect.x = 10
        self.rect.y = 0
        self.setupCards(card_list)

    def loadFrame(self, name, image): # name the card and image
        frame = tool[name]
        self.image = tool.get_image(name, image)


    def getCardPool(card_pool): #make a card pool
        card_pool = []

    def createImage(self): # making a image for menubar
        img = self.image
        rect = self.image_get_rect()
        width = rect.w
        height = rect.h
        self.image = py.Surface((width * 10, height * 4)) # can hold 10 cards
        self.rect = self.image_get_rect()

    # pick card randomly from the target list
    # that means plant you get and zombies you 
    # face is all random, please pray for lucky
    def randomCard(card_name_list1, card_name_list2, name):
        plant = []
        plant = df.sample(card_name_list1)
        plant = mp.showPlant()

        zombies = []
        zombies = df.sample(card_name_list2)
        zombies = mp.showZombies()

    # because at first 10 turn, this is easy model 
    # or you can input turns you like
    # if not, we will randomly give 0-10 for easy model
    # because hard model contain 3 zombies that need 
    # unique solution plant, or died
    def turn(self, time): 
        time = ()
        if input() is True:
            time = input()
            return time
        else:
            time = (random.randint(0,10))


    def give_card(time, easy_plant, easy_zombies, hard_zombies, hard_plant):
        if time <= 10:
            card_pool = df.sample.replace(easy_plant, easy_zombies) # I suppose it should be replace 
        else:                                                       # to put it back after pick a card
            card_pool = df.sample.replace(hard_zombies, hard_plant)

    def Error(self):
        if self is False:
            Error = mainquit()
        else : 
            return True


# we hope this works
# yours
# YU & Zhang & LI & Bao


