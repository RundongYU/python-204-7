import pygame as pg
import main as ma
import map as m

ma.card_name_list2 = [1, 3, 5, 7, 9]
ma.card_name_list1 = [2, 4, 6, 8, 10]
# I was trying to make plant be even
# zombies to be odd
# so when overall value is odd or even 
#we can find there is zombies or not

class Plant(): # make a list
    def __init__(self, card_name_list1):
        self = []
        self = ma.card_name_list1()
        return self
    
    def map_x(self, plant, x): #location the plant 
        plant = int()
        tem = int(m.getMapindex(self,x ))
        plant = tem
        return plant

        

    def Peashooter(self, plant):
        self = int()                    # make a exist value
        self = ma.easy_plant(0)         # it is the first value in list
        tem = map_x(self, plant, 1)     # location in map
        tem = Peashooter(self, plant)
        if Peashooter(self, plant) % 2 == 0:  # judge if it is even
            try:
                plant = self.map_x(plant)   
                return True                     # see zombies and it is a unique sulution
            except:
                print(False)# temp % 2 != 0    # see zombies but not a unique sulution
        else:
            return False

    def Wall_nut(self, plant):
        def Wall_nut(self, plant):
            self = int()
        self = ma.easy_plant(0)
        tem = map_x(self, plant, 2)
        tem = Wall_nut(self, plant)
        if Wall_nut(self, plant) % 2 == 0:
            try:
                plant = self.map_x(plant)
                return True
            except:
                print(False)# temp % 2 != 0    
        else:
            return False
    
    def Chomper(self, plant):
        def Chomper(self, plant):
            self = int()
        self = ma.easy_plant(0)
        tem = map_x(self, plant, 3)
        tem = Chomper(self, plant)
        if Chomper(self, plant) % 2 == 0:
            try:
                plant = self.map_x(plant)
                return True
            except:
                print(False)# temp % 2 != 0    
        else:
            return False


    def Reperter(self, plant):
        def Reperter(self, plant):
            self = int()
        self = ma.easy_plant(0)
        tem = map_x(self, plant, 4)
        tem = Reperter(self, plant)
        if Reperter(self, plant) % 2 == 0:
            try:
                plant = self.map_x(plant)
                return True
            except:
                print(False)# temp % 2 != 0    
        else:
            return False

    def Fume_shroom(self, plant):
        def Peashooter(self, plant):
            self = int()
        self = ma.easy_plant(0)
        tem = map_x(self, plant, 5)
        tem = Fume_shroom(self, plant)
        if Fume_shroom(self, plant) % 2 == 0:
            try:
                plant = self.map_x(plant)
                return True
            except:
                print(False)# temp % 2 != 0    
        else:
            return False




# we hope this works
# yours
# YU & Zhang & LI & Bao