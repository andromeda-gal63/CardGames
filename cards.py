###########################################
#
# Python Program: cards.py
# Author: Angela Peterson
#
# Contains Classes:
# - Card
# - Deck
#
###########################################
import re
from random import randint

#Constants
SPADES         = "SPADES"
CLUBS          = "CLUBS"
HEARTS         = "HEARTS"
DIAMONDS       = "DIAMONDS"
JOKERS          = "JOKER"
jokerPattern   = re.compile("JOKER")
WITHOUT_JOKERS = False;
WITH_JOKERS    = True;

#===========================================
# CLASS: Card
#===========================================
class Card(object):
  """A card. """

  #-------------------------------------
  # Method: Card.__init__()
  #-------------------------------------    
  def __init__(self, value, suit):
    """ New card. """
    self.value = value
    self.suit  = suit

  #-------------------------------------
  # Method: Card.getValue()
  #-------------------------------------  		
  def getValue(self):
    return self.value

  #-------------------------------------
  # Method: Card.getSuit()
  #-------------------------------------  	
  def getSuit(self):
    return self.suit

  #-------------------------------------
  # Method: Card.printCard()
  #-------------------------------------  
  def printCard(self):
    if (jokerPattern.match(self.suit)):
      if (self.value >0):
        print("High Joker")
      else:
        print("Low Joker")
      return
    
    if (self.value == 1):
      print("Ace of %s"%(self.suit));
    elif self.value == 11:
      print("Jack of %s"%(self.suit))
    elif (self.value == 12):
      print("Queen of %s"%(self.suit))
    elif (self.value == 13):
      print("King of %s"%(self.suit))
    elif self.value == 0:
      print("Joker");
    else:
      print("%i of %s")%(self.value, self.suit)


#===========================================
# CLASS: Deck
#===========================================
class Deck(object):
  """ A Deck of Cards. """
  #-------------------------------------
  # Method: Deck.__init__()
  #-------------------------------------  
  def __init__(self, useJokers):
    """ Initialize a new deck of cards. """
    # Set whether Jokers are used or not.
    self.jokers   = useJokers;
    self.cards    =[]

    # Create each card in the suits.
    for i in range(1, 14):
      # Create Spades suit.
      spadeCard = Card(i,SPADES)
      clubCard  = Card(i,CLUBS)
      heartCard = Card(i,HEARTS);
      diamondCard = Card(i,DIAMONDS);

      # Add the cards to the deck.
      self.cards.append(spadeCard);
      self.cards.append(clubCard);
      self.cards.append(heartCard);
      self.cards.append(diamondCard);

    # Create and add Jokers, if appropriate 
    if (useJokers):
      for i in range(0,2):
        self.cards.append(Card(i,JOKERS))


  #-------------------------------------
  # Method: Deck.getDeck()
  #-------------------------------------
  def getCards(self):
    # Return the list of cards in the deck.
    return self.cards

  #-------------------------------------
  # Method: Deck.getSuit()
  #-------------------------------------
  def getSuit(self,suit):
    # Return the list of cards in cardList matching the suit.
    suitToMatch = re.compile(suit)
    result = []
    for c in self.cards:
      if suitToMatch.match(c.getSuit()):
        result.append(c)
    return result

  #-------------------------------------
  # Method: Deck.getSize()
  #-------------------------------------
  def getSize(self):
    # Return number of cards in the deck.
    return len(self.cards)

  #-------------------------------------
  # Method: Deck.shuffleList()
  #-------------------------------------
  def shuffleList(self, cardList):
    # Return the shuffled cardList.
    newList = []
    tempList = cardList
    tempLength = len(cardList)

    # Remove a random card from the cardList and insert it into the next position in the newList
    # until all cards have been removed from the original cardList.
    for i in range(0,len(cardList)):
      ri = randint(0,tempLength-1)
      c = tempList[ri]
      tempList.remove(c)
      newList.append(c)
      tempLength -= 1  #decrease tempLength by 1
    return newList

  #-------------------------------------
  # Method: Deck.shuffleDeck()
  #-------------------------------------
  def shuffleDeck(self):
    # Return the shuffled deck.
    newList    = []
    tempList   = self.cards
    tempLength = len(self.cards)

    # Remove a random card from the cardList and insert it into the next position in the newList
    # until all cards have been removed from the original cardList.
    for i in range(0,len(self.cards)):
      ri = randint(0,tempLength-1)
      c = tempList[ri]
      tempList.remove(c)
      newList.append(c)
      tempLength -= 1  #decrease tempLength by 1
      
    # Update the Deck.cards with the newly shuffled list.
    self.cards = newList
    return self.cards

  #-------------------------------------
  # Method: Deck.printDeck()
  #-------------------------------------
  def printDeck(self):
    # Print all cards in the deck.
    for c in self.cards:
      c.printCard()

  #-------------------------------------
  # Method: Deck.printCardList()
  #-------------------------------------
  def printCardList(self, cardList):
    # Print all cards in cardList.
    for c in cardList:
      c.printCard()

  #-------------------------------------
  # Method: Deck.printCardList()
  #-------------------------------------
  def testShuffle(self):
    print("\nTest Case: Deck.testShuffle()\n")
    self.shuffleDeck()
    self.printCardList(self.getDeck())

    print("\nShuffled SPADES\n----------------")
    self.printCardList(self.getSuit(SPADES))



#===================================
# MAIN
#===================================
# Create and print a deck of cards.
#myDeck = Deck(WITH_JOKERS);  # Use Jokers
####print("Deck size = %s"%myDeck.getSize())


#myDeck.printCardList(myDeck.getSuit(SPADES))
#myDeck.printCardList(myDeck.getSuit(HEARTS))

#myDeck.printCardList(myDeck.getSuit(JOKERS))
#myJokers = myDeck.getSuit(JOKERS)
#myJokers = myDeck.shuffleList(myJokers)
#myDeck.printCardList(myJokers)


# Method Deck.shuffleList() does not shuffle the real deck.
#myHearts = myDeck.getSuit(HEARTS)
#myHearts = myDeck.shuffleList(myHearts)
#myDeck.printCardList(myHearts)

# Method Deck.shuffleDeck() replaces the deck cards with the shuffled cards.
#myDeck.testShuffle()



