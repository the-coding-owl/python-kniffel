import GameObjects.Die

print("Kniffel")
print("Copyright Kevin Ditscheid")

amountOfDice = 5
dice = []
diceCounter = 0
while diceCounter < amountOfDice :
    newDie = GameObjects.Die.Die()
    dice += [newDie]
    diceCounter += 1

playerAmount = 0
while playerAmount <= 1:
    try :
        playerAmount = int(input("Wieviele Mitspieler?"))
    except ValueError :
        print("Bitte geben Sie eine ganze Zahl ein, welche größer als 1 ist.")
players = []
playerInit = 1
while playerInit <= playerAmount :
    player = GameObjects.Player.Player()
    player.setName(input("Wie heißt Spieler ", playerInit, "?"))
    players += [player]
round = 1
while round <= 13 :
    currentPlayer = 1
    while currentPlayer <= playerAmount :
        print("Player ", currentPlayer, " turn")
        allDiceRolled = false
        rerolls = 2
        print("Rolls:")
        for dieIndex in dice :
            dice[dieIndex].roll()
            print("Die ", dieIndex, ": ", dice[dieIndex].getFace())
        print("Rerolls: ", rerolls)
        
        players[currentPlayer]
