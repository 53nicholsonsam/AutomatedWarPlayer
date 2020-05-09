### Sam Nicholson 2020
### Script to play war with itself
%reset -f
from collections import defaultdict
import random 
import statistics
import pandas as pd
import matplotlib.pyplot as plt
itteration=0
handcount=[]
for loop in range(0,100001):
  Cardvalues=[]
  IndexNumbers =list(range(1,53))
  Dummyarray =list(range(1,14))
  i=0
  while i<52:
    for ii in range(0,len(Dummyarray)):
      Cardvalues.append(Dummyarray[ii])
      #print("still working")
      i+=1
      #print(i)
  ##Merge the lists into 1 list to creat the dictionary with
  listtodict=[]
  for ii in range(0,len(Cardvalues)):
    temparray=[]
    temparray.append(IndexNumbers[ii])
    temparray.append(Cardvalues[ii])
    listtodict.append(temparray)
  #print(IndexNumbers)
  #print(Cardvalues)
  deck=dict(listtodict)
  #print(listtodict)
  ##Dealing
  Indextodealfrom=list(range(1,53))
  random.shuffle(Indextodealfrom)
  middlindex=int(len(Indextodealfrom)/2)
  Player1index=Indextodealfrom[middlindex:]
  Player2index=Indextodealfrom[:middlindex]
  #print(Player1index)
  #print(Player2index)
  #print(Indextodealfrom)
  #print(deck)
  iii=0
  Player1deck=[]
  Player2deck=[]
  while iii<26:
    Player1deck.append(deck[Player1index[iii]])
    Player2deck.append(deck[Player2index[iii]])
    iii+=1
  #print("Player 1 Deck:" + str(Player1deck))
  #print("Player 2 Deck:" + str(Player2deck))
  ##Playing war
  count=0
  while len(Player1deck)>0 and len(Player2deck)>0: #While someone still has cards
    #print("Player 1's card: " + str(Player1deck[0]) + " v "+ str(Player2deck[0])+ ": Player 2's card")
    if Player1deck[0]>Player2deck[0]: #Player 1 take the card
      Player1deck.append(Player1deck[0]) #Move the card card played to the bottem
      Player1deck.append(Player2deck[0]) #Move the taken card to the bottem
      Player1deck.pop(0) #Move the card played to the bottem
      Player2deck.pop(0) #Move the card played to the other player
    elif Player1deck[0]<Player2deck[0]: #Player 2 takes the card
      Player2deck.append(Player2deck[0])
      Player2deck.append(Player1deck[0])
      Player1deck.pop(0)
      Player2deck.pop(0)
    elif Player1deck[0]==Player2deck[0]: #There is a war
      Player1War=[]
      Player2War=[]
      test=0
      
      while test==0:
        if (len(Player1deck)<5 or len(Player2deck)<5): #Where there is a war and one player has less than 4 cards left
          for vi in range(0,max(1,min(len(Player1deck)-1,3))): #Saves 1 card to use putting in at least 1
            #print(vi)
            #print ("Player1deck len:"+str(len(Player1deck)))
            if len(Player1deck)!=1:
              Player1War.append(Player1deck[vi])
          for viii in range(0,max(1,min(len(Player1deck)-1,3))):
            #print(viii)
            #print ("Player1deck len:"+str(len(Player1deck)))
            if len(Player1deck)!=1:
              Player1deck.pop(0)
          for vii in range(0,max(1,min(len(Player2deck)-1,3))):
            #print(vii)
            #print ("Player2deck len:"+str(len(Player2deck)))
            if len(Player2deck)!=1:
              Player2War.append(Player2deck[vii])
          for ix in range(0,max(1,min(len(Player2deck)-1,3))):
            #print(ix)
            #print ("Player2deck len:"+str(len(Player2deck)))
            if len(Player2deck)!=1:
              Player2deck.pop(0)
          #print("There's a war!")
          #print("Player 1's card: " + str(Player1deck[0]) + " v "+ str(Player2deck[0])+ ": Player 2's card")
          if Player1deck[0]>Player2deck[0]: #Player 1 wins and gets the cards
            Player1deck.append(Player1deck[0]) 
            Player1deck.append(Player2deck[0]) 
            Player1deck.pop(0) 
            Player2deck.pop(0) 
            for iv in range(0,len(Player1War)):
              Player1deck.append(Player1War[iv])
            for v in range(0,len(Player2War)):
              Player1deck.append(Player2War[v])
            test=1
          elif Player1deck[0]<Player2deck[0]: #Player 2 wins and gets the cards
            Player2deck.append(Player2deck[0])
            Player2deck.append(Player1deck[0])
            Player1deck.pop(0)
            Player2deck.pop(0)
            for iv in range(0,len(Player1War)):
              Player2deck.append(Player1War[iv])
            for v in range(0,len(Player2War)):
              Player2deck.append(Player2War[v])
            test=1
        else:
          Player1War.append(Player1deck[0]) #Each are putting their turned up card and 2 more cards into the war pile
          Player1War.append(Player1deck[1])
          Player1War.append(Player1deck[2])   
          Player1deck.pop(0)
          Player1deck.pop(1)
          Player1deck.pop(2)
          Player2War.append(Player2deck[0])
          Player2War.append(Player2deck[1])
          Player2War.append(Player2deck[2])
          Player2deck.pop(0)
          Player2deck.pop(1)
          Player2deck.pop(2)
      #Checking the next card to see who wins the war
          #print("There's a war!")
          #print("Player 1's card: " + str(Player1deck[0]) + " v "+ str(Player2deck[0])+ ": Player 2's card")
          if Player1deck[0]>Player2deck[0]: #Player 1 wins and gets the cards
            Player1deck.append(Player1deck[0]) 
            Player1deck.append(Player2deck[0]) 
            Player1deck.pop(0) 
            Player2deck.pop(0) 
            for iv in range(0,len(Player1War)):
              Player1deck.append(Player1War[iv])
            for v in range(0,len(Player2War)):
              Player1deck.append(Player2War[v])
            test=1
          elif Player1deck[0]<Player2deck[0]: #Player 2 wins and gets the cards
            Player2deck.append(Player2deck[0])
            Player2deck.append(Player1deck[0])
            Player1deck.pop(0)
            Player2deck.pop(0)
            for iv in range(0,len(Player1War)):
              Player2deck.append(Player1War[iv])
            for v in range(0,len(Player2War)):
              Player2deck.append(Player2War[v])
            test=1
            #They keep playing
    count+=1
  itteration+=1
  print("Trial: "+ str(itteration))
  ### For printing results of 1 game###
  #if len(Player1deck)>0:
  #  print("Player 1 Wins!")
  #else:
  #  print("Player 2 Wins!")
  #print("It took " +str(count) + " hands to finish the game")
  ### For gathering data ###
  
  handcount.append(count)
#print(handcount)
plt.hist(handcount, bins= 75)
plt.title("Length of game in hands for 100000 War Games")
plt.xlabel("Counts")
plt.ylabel("Number of Hands")
plt.grid(axis="y",alpha=0.75)
print("Mean of Sample Game Length is % s" % (round(statistics.mean(handcount),3)))
print("Standard Deviation of Sample Game Length is % s" % (round(statistics.stdev(handcount),3)))
print("Max number of hands in Sample Game Length is % s" % (max(handcount))) 
print("Minimum number of hands in Sample Game Length is % s" % (min(handcount)))