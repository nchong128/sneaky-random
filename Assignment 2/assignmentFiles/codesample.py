# REPRESENTS A 5X5 BOARD- DO NOT DELETE
Board = [['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]
boardSize = len(Board)
firstMove = False
wordLocation = ["1","1","H"]
# REPRESENTS A 5X5 BOARD- DO NOT DELETE

def tilePlacer(chosenWord,location):
    row = int(location[0])
    column = int(location[1])
    
    if firstMove == True:
        pass
    elif location[2] == "H":
        for i in range(column, len(chosenWord)):
            Board[row][i] = chosenWord[i]

tilePlacer("TONE",wordLocation)
print(Board)