##10072014c.py
##John brook
##class notes from 10-07-2014



##============================================================##
###Base class
##
##class Critter(object):
##   """A virtual pet"""
##   def talk(self):       #class methoid  #callable function
##      print("Hi. I'm an instance of class Critter.")
##
##def main():
##    crit = Critter() #shortens class
##    crit.talk()   #class w/ fun
##
##main()


##============================================================##

##class Critter(object):
##   """A virtual pet"""
##   def talk(self):       #class methoid  #callable function
##       print("Hi. I'm an instance of class Critter.")
##   def __init__(self, legs, color, toxic, name):
##       self.name = name
##       self.legs = legs
##       self.color = color
##       self.toxic = toxic
##   def __str__(self):
##       rep = "Critter object\n"
##       rep += "name: " + self.name + "\n"
##       rep += "legs: " + self.legs + "\n"
##       rep += "color: " + self.color + "\n"
##       rep += "toxic: " + self.toxic + "\n"
##       return rep
##
##
##def main():
##    crit = Critter("6","blue","yes","frank") #shortens class
##    crit.talk()   #class w/ fun
##    print(crit)
##
##    crit1 = Critter("6","purple","no","bob") #shortens class
##    crit.talk()   #class w/ fun
##    print(crit1)
##
##main()
##============================================================##

class playerClass(object):
   """A virtual pet"""
   def talk(self):       #class methoid  #callable function
       print("Hi. I'm an instance of class Critter.")
   def __init__(self,name, HP, MP, ATK, DEF):
       self.name = name
       self.HP = HP
       self.MP = MP
       self.ATK = ATK
       self.DEF = DEF
       
   def __str__(self):
       rep = "Critter object\n"
       rep += "Name: " + self.name + "\n"
       rep += "HP: " + self.HP + "\n"
       rep += "MP: " + self.MP + "\n"
       rep += "ATK: " + self.ATK + "\n"
       rep += "DEF: " + self.DEF + "\n"
       return rep
   def update_health(self, delta):
       self.health = delta


def main():
    crit = playerClass("bob","6","21","22","22") #shortens class
    crit.talk()   #class w/ fun
    crit.update_health("+5")
    print(crit)



main()
##============================================================##
