# Card Game #1
#
from cards import Deck
from cards import Card

WITH_JOKERS = True
WITHOUT_JOKERS = False


class Game1(object):
  def __init__(self, numberOfPlayers):
    # initialize local variables
    deck = Deck(WITHOUT_JOKERS)
    deck.shuffleDeck()

    # initialize class variables
    self.deck = deck
    self.numberOfPlayers = numberOfPlayers
    self.dealer = deck.getCards() # dealer gets all cards
    self.players = []
    for i in range(0, numberOfPlayers):
      self.players.append([]) # players get no cards

  #-------------------------------------
  # Method: Game.deal(roundsToDeal)
  #-------------------------------------
  def deal(self, roundsToDeal):
    # Check if dealer has enough cards to deal equally to all players
    totalCardsToDeal = roundsToDeal * self.numberOfPlayers
    dealerCards = self.dealer
    if totalCardsToDeal > len(dealerCards):
      print("*** Error: not enough cards in deck to deal.");
      print("    totalToDeal= %s and dealer's cards= %s"%(totalCardsToDeal, len(dealerCards)))
      return

    # Deal top card to each player for each round.
    for i in range(0, roundsToDeal):
      for p in range(0, self.numberOfPlayers):
        c = dealerCards[0]         # get top card
        self.players[p].append(c)  # give card to player[p]
        dealerCards.remove(c)      # remove card from dealer's deck

  #---------------------------
  # Method: Play()
  #---------------------------
  def play(self):
    print("Play next turn:")
    gameOver = False

    #while not gameOver: take another turn
    for t in range(0,501):
      # Get cards for this turn from each player
      cardsThisTurn =[]

      if gameOver:
        print("GameOver")
        break

      # Get each player's top card for this turn.
      for p in range(0, self.numberOfPlayers):
        print("Player %s has %s cards."%(p,len(self.players[p])))
        if len(self.players[p]) <= 0:
          print("Player #%s has no more cards to play."%p)
          gameOver = True
          exit
        else:
          playersCard = self.takeTurn(p)
          cardsThisTurn.append(playersCard) # 
          #playersCard.printCard()  # print card to play

      # Find player with highest card.
      if not gameOver:
        winnerThisTurn = self.findWinnerThisTurn(cardsThisTurn)
        if len(winnerThisTurn) <=0:
          print("### Error: Could not find a winner. ###")
          gameOver = True
        elif len(winnerThisTurn) >1:
          print("War!")
          self.players[0].append(cardsThisTurn[0])
          self.players[1].append(cardsThisTurn[1])
        else:
          # Add all cards in this turn to the winning player's hand.
          playerNumber = winnerThisTurn[0]
          for i in range(0, len(cardsThisTurn)):
            self.players[playerNumber].append(cardsThisTurn[i])
          #self.players[playerNumber] = self.deck.shuffleList(self.players[playerNumber])
          print("Winner #%s this turn has %s cards."%(playerNumber, len(self.players[playerNumber])))
      gameOver = self.isGameOver()
    

  def isGameOver(self):
    playersStillPlaying = 0
    for p in range(0, self.numberOfPlayers):
      if len(self.players[p]) > 0:
        playersStillPlaying = playersStillPlaying+1
      if playersStillPlaying > 1:
        #print("Continue playing.")
        return False
    return (playersStillPlaying <= 1)

  def takeTurn(self, playerNumber):
    if len(self.players[playerNumber]) <= 0:
        return
    nextCard = self.players[playerNumber][0]
    self.players[playerNumber].remove(nextCard)
    return nextCard

  def findWinnerThisTurn(self, cards):
    winner = []
    highestCard = 0
    for i in range(0, len(cards)):
      nextCard = cards[i].getValue()
      if nextCard < highestCard:
        break
      if nextCard == highestCard:
        winner.append(i) # so far we have a tie for highest card
      elif nextCard > highestCard:
        highestCard = nextCard
        winner = [] #### Empty the winner list ####
        winner.append(i)
      print("Card Value= %s"%cards[i].getValue())
    return winner
      
    
  def getDeck(self):
    return self.deck

  def getHand(self, player):
    #if len(self.players)
    if player ==1:
      return self.players[0]
    else:
      return self.players[1]



#============
# MAIN
#============
numberOfPlayers =2

print("Starting Game...")
game = Game1(numberOfPlayers); # 2-players
gameDeck = game.getDeck()
print("Game deck size = %s"%gameDeck.getSize())

# Deal Hands
numberToDeal = gameDeck.getSize()/numberOfPlayers
#numberToDeal = 2
game.deal(numberToDeal) # Deal whole deck

# Test: Verify each player has correct number of unique cards.
p1 = game.getHand(1)
print("Player1 hand size = %s"%len(p1))
for i in range(0,len(p1)):
  p1[i].printCard()
p2 = game.getHand(2)
print("Player2 hand size = %s"%len(p2))
for i in range(0,len(p1)):
  p2[i].printCard()

# Play Turns
game.play()


