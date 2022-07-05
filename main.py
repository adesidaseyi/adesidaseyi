#This program is meant to run in the CLI... 
#GUI mode would be made available using the pygame module very soon :)

import random as rd

#This text is first displayed when the game is loaded
welcomeMsg = "TIC-TAC-TOE!!!\n\nGame Rules:\n- Can’t play where someone else has played\n- Play is one at a time\n- First to complete vertical, horizontal, or diagonal Wins!\n\nINPUT YOUR POSITION AS TWO DIGIT NUMBER FOR ROW AND COLUMN e.g 01 FOR ROW 0, COLUMN 1\nPress Enter to start game..."


class GridElement:      #GridElement represents each slot in the grid as an object with properties
    value = None
    display = ' '   #CLI display
    def __init__(self, row, column):
        self.row = row
        self.column = column


#This is the defined grid for the game
gameGrid = [[GridElement(0,0), GridElement(0,1), GridElement(0,2)],
            [GridElement(1,0), GridElement(1,1), GridElement(1,2)],
            [GridElement(2,0), GridElement(2,1), GridElement(2,2)]]


#list of all possible winning positions
winningPosition = [[[0,0],[0,1],[0,2]],[[1,0],[1,1],[1,2]],[[2,0],[2,1],[2,2]],[[0,0],[1,0],[2,0]],[[0,1],[1,1],[2,1]],[[0,2],[1,2],[2,2]],[[0,0],[1,1],[2,2]],[[0,2],[1,1],[2,0]]]

                
def clearGrid():    #clears grid
        for i in range(3):
            for j in range(3):
                gameGrid[i][j].value = None
                gameGrid[i][j].display = ' '  


def nextPlayer(currentPlayer):  #Players are represented in UpperCase
    if currentPlayer == 'X':
        return 'O'
    return 'X'


def randomizePlayers():
    #Returns a random player to make first move
    if rd.randint(0,1) == 0:
        return 'O'
    return 'X'


def freeSlot():
#checks if there is still an unassigned GridEleement (slot) in the gameGrid
    for i in range(3):
        for j in range(3):
            #print(gameGrid[i][j].value)
            if gameGrid[i][j].value == None:
                return True
    return False    


def checkWin(player):
    #Checks if the player from argument is in any winning position
    wp = winningPosition 
    for i in range(8):
        for j in range(3):
            if gameGrid[wp[i][j][0]][wp[i][j][1]].value != player:
                break
            if j == 2:
                return True    
    return False


def validInput(input):
    #validates a two lettered input and converts it to int type. Returns false in case of unexpected error
    try:    
        if len(input) == 2 and int(input[0])>=0 and int(input[0])<3 and int(input[1])>=0 and int(input[1])<3:
            return [int(input[0]),int(input[1])]
        return False
    except:
      return False


#CLI for game display
displayCLI = '\n   0 | 1 | 2\n  ~~~~~~~~~~~~\n0| {} | {} | {}\n  ~~~~~~~~~~~~\n1| {} | {} | {}\n  ~~~~~~~~~~~~\n2| {} | {} | {} \n'

def updateDisplayCLI():
    #Update and returns the CLI display with what it gets from each grid element
    newCLI = displayCLI.format(gameGrid[0][0].display,gameGrid[0][1].display,gameGrid[0][2].display,gameGrid[1][0].display,gameGrid[1][1].display,gameGrid[1][2].display,gameGrid[2][0].display,gameGrid[2][1].display,gameGrid[2][2].display)
    return newCLI


def main():
    #Entry for the game -- focus is on CLI 
    print(welcomeMsg)
    input() 
    firstPlayer = randomizePlayers()    #sets the first player randomly
    print('First Player => {}'.format(firstPlayer))
    scores = {'X':0,'O':0}      #stores scores for each player in the game
    print(displayCLI.format(gameGrid[0][0].display,gameGrid[0][1].display,gameGrid[0][2].display,gameGrid[1][0].display,gameGrid[1][1].display,gameGrid[1][2].display,gameGrid[2][0].display,gameGrid[2][1].display,gameGrid[2][2].display))
    currentPlayer = firstPlayer     #sets the current player for every turn
    print('\nScores:\nX->{} O->{}'.format(scores['X'],scores['O']))
    while True:     #game loop
        #print('\nScores:\nX->{} O->{}'.format(scores['X'],scores['O']))
        position = validInput(input())  #gets, validates, and stores the position in the grid a player decides to move to
        if position == False:
            print('Invalid Position')
        elif gameGrid[position[0]][position[1]].value != None:  #checks if the input position is taken. If taken, dosen't allow that play at that position
            print('Unallowed Position.')
        else:
            #set current value in gameGrid
            gameGrid[position[0]][position[1]].value = currentPlayer
            gameGrid[position[0]][position[1]].display = currentPlayer
            print(updateDisplayCLI())
            #() check win and decide to end game loop; update scores: fit in freeslot
            if checkWin(currentPlayer) == True:
                scores[currentPlayer] = scores[currentPlayer] + 1   #increment score of winner
                print('Player {} wins.\nContinue Playing? (y/n)'.format(currentPlayer))
                if input() == 'n':
                    print('\nScores:\nX->{} O->{}'.format(scores['X'],scores['O']))
                    break
                else:
                    clearGrid()
                    print(displayCLI.format(gameGrid[0][0].display,gameGrid[0][1].display,gameGrid[0][2].display,gameGrid[1][0].display,gameGrid[1][1].display,gameGrid[1][2].display,gameGrid[2][0].display,gameGrid[2][1].display,gameGrid[2][2].display))
            elif freeSlot() == False:
                print('Game Draw.\nContinue Playing? (y/n)')
                if input() == 'n':
                    print('\nScores:\nX->{} O->{}'.format(scores['X'],scores['O']))
                    break
                else:
                    clearGrid()
                    print(displayCLI.format(gameGrid[0][0].display,gameGrid[0][1].display,gameGrid[0][2].display,gameGrid[1][0].display,gameGrid[1][1].display,gameGrid[1][2].display,gameGrid[2][0].display,gameGrid[2][1].display,gameGrid[2][2].display))
            currentPlayer = nextPlayer(currentPlayer)
            print('\nScores:\nX->{} O->{}'.format(scores['X'],scores['O']))
            print('\nNext Player: {}'.format(currentPlayer))

main()