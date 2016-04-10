##102112014c.py
##John brook
##Class notes from 10-23-2014


##============================================================##
##============================================================##
##============================================================##

##class playerClass(object):
##   """A virtual pet"""
##   def talk(self):       #class methoid  #callable function
##       print("Hi. I'm an instance of class Critter.")
##   def __init__(self,name, HP, MP, ATK, DEF):
##       self.name = name
##       self.HP = HP
##       self.MP = MP
##       self.ATK = ATK
##       self.DEF = DEF
##       
##   def __str__(self):
##       rep = "Critter object\n"
##       rep += "Name: " + self.name + "\n"
##       rep += "HP: " + self.HP + "\n"
##       rep += "MP: " + self.MP + "\n"
##       rep += "ATK: " + self.ATK + "\n"
##       rep += "DEF: " + self.DEF + "\n"
##       return rep
##   def update_health(self, delta):
##       self.health = delta
##
##
##def main():
##    crit = playerClass("bob","6","21","22","22") #shortens class
##    crit.talk()   #class w/ fun
##    crit.update_health("+5")
##    print(crit)





##class Card(object):
##    """ A playing card. """
##    RANKS = ["A", "2", "3", "4", "5", "6", "7",
##             "8", "9", "10", "J", "Q", "K"]
##    SUITS = ["c", "d", "h", "s"]
##    
##    def __init__(self, rank, suit):
##        self.rank = rank 
##        self.suit = suit
##
##    def __str__(self):
##        rep = self.rank + self.suit
##        return rep

class Card(object):
    """ A playing card. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    
    def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Unprintable_Card(Card):
    def __str__(self):
        return "<unprintable>"


class Positionable_Card(Card):
    def __str__(self):
##        if self.is_face_up:
          rep = super(Positionable_Card, self).__str__()
##        else:
##          rep = "XX"
          return rep
##
##    def flip(self):
##     self.is_face_up = not self.is_face_up
##


class Hand(object):
    """ A hand of playing cards. """
    def __init__(self):   #constructor
        self.cards = []

    def __str__(self):
        if self.cards:
           rep = ""
           for card in self.cards:
               rep += str(card) + "  "
        else:
            rep = "<empty>"
        return rep
      
    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """ A deck of playing cards. """
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS: 
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)


    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0] #those w/ 0 in list = top
                    self.give(top_card, hand)
                else:
                    print ("Out of cards!")


def main():
   print('main')
   card1 = Card(rank = "A", suit = "c")
   card2 = Card(rank = "2", suit = "c")
   card3 = Card(rank = "3", suit = "c")
   card4 = Card(rank = "4", suit = "c")
   card5 = Card(rank = "5", suit = "c")
   print (card1)  # Ac
   print (card2)  # 2c
   print (card3)  # 3c
   print (card4)  # 4c
   print (card5)  # 5c
   my_hand = Hand()
   print (my_hand)  # <empty>
   my_hand.add(card1)
   my_hand.add(card2)
   my_hand.add(card3)
   my_hand.add(card4)
   my_hand.add(card5)
   print (my_hand)  # Ac 2c 3c 4c 5c 

   your_hand = Hand()
   my_hand.give(card1, your_hand)
   my_hand.give(card2, your_hand)
   print (your_hand)  # Ac 2c
   print (my_hand)    # 3c 4c 5c
   my_hand.clear()
   print (my_hand)    # <empty>



   deck1 = Deck()
   print (deck1)  # <empty>
   print('')

   deck1.populate()
   print (deck1)  # ordered deck
   print('')

   deck1.shuffle()
   print (deck1)  # shuffled deck
   print('')


   my_hand = Hand()
   your_hand = Hand()
   hands = [my_hand, your_hand]
   deck1.deal(hands, per_hand = 5)
   print('')
   print (my_hand )   # 5 alternating cards from deck
   print('')
   print (your_hand)  # 5 alternating cards from deck
   print('')
   print (deck1  )    # deck minus first 10 cards
   print('')
   deck1.clear()
   print (deck1 )     # <empty>

   card1 = Card("A", "c")
   card2 = Unprintable_Card("A", "d")
   card3 = Positionable_Card("A", "h")

   print (card1)    # Ac
   print (card2 )   # <unprintable>
   print (card3  )  # Ah
##   card3.flip()
   print (card3)    # XX


   


main()









    

##============================================================##
##============================================================##
##main()
##============================================================##
##============================================================##













##
##
##def main():
##    print('main')
##    bj_game1 = bj_game(x, y , z)
##
##
##main()
