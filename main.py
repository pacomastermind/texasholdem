from itertools import product
import random

def printcard(card):
    print("[",card[0],card[1],"]")

def printplayer():
    print("--------- PLAYER ------------")
    printcard((deck[randomList[0]]))
    printcard((deck[randomList[1]]))

def printia():
    print("--------- IA ------------")
    printcard((deck[randomList[2]]))
    printcard((deck[randomList[3]]))
def printmiddle(number):
    print("---------- MESA -------------")
    for i in range(number):
        printcard((deck[randomList[i+1]]))
    for i in range(5-number):
        printcard(hiddencard)


# a list of all the suits
Suits = ["\u2663", "\u2665",
         "\u2666", "\u2660"]
# a list of all the ranks
Ranks = ['A', '2', '3', '4', '5',
         '6', '7', '8', '9', '10',
         'J', 'Q', 'K']

deck = list(product(Ranks, Suits))


# get 2 cards (player) + 5 cards (middle) + 2 cards (machine)
randomList=[]
for i in range(9):
   # generating a random number in the range 1 to 100
   r=random.randint(0,51)
   # checking whether the generated random number is not in the
   # randomList
   if r not in randomList:
      # appending the random number to the resultant list, if the condition is true
      randomList.append(r)
# Hidden card
hiddencard=['-','-']
# TEXAS HOLDEM
print("-----------------------------")
print("-----------------------------")
print("------ TEXAS HOLDEM ---------")
print("-----------------------------")
print("-----------------------------")

#------GAME------
turn=1
playerContinue=True
iaContinue=True
ganador='player'
while(turn<4 and playerContinue and iaContinue):
    print()
    print("-------- TURNO {} ------------".format(turn))
    # Print cards
    printplayer()
    printmiddle(turn+2)
    # First turn
    print("¿Quieres continuar jugando? [S/N]")
    opcion = input()
    if opcion.upper() == "S":
        iaContinue=bool(random.getrandbits(1))
        if iaContinue:
            print("La maquina decide seguir jugando")
            # Ambos jugadores continuan
            turn = turn+1
        else:
            ganador = 'player'
    else:
        playerContinue = False
        ganador = 'ia'

print()
printplayer()
printia()
print("-----------------------------")
print("----GANADOR {} -------".format(ganador))