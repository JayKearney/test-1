from random import randint
import sys

    
#Create a dictionary


def printBoard(board):
    print(board['top-left'] + '|'+board['top-center']+'|'+board['top-right'])
    print('-+-+-')
    print(board['mid-left'] + '|'+board['mid-center']+'|' + board['mid-right'])
    print('-+-+-')
    print(board['lower-left'] + '|'+board['lower-center']+'|' + board['lower-right'])

def player_input():

    value = ""

    while not (value == "X" or value == "O"):
        value = input("Please pick a value 'X' or 'O': ")
    return (value)

def goes_first():
    print(["Player","Computer"][randint(0,1)])
    
def main():
    print("Tic Tac Toe")

    person, computer = '',''

#printBoard(theBoard)

    while True:
        # Set up the board
        Board = { 'top-left': ' ', 'top-center': ' ', 'top-rigt': ' ',
        'mid-left': ' ', 'mid-center': ' ', 'mid-right': ' ',
         'lower-left': ' ', 'lower-center': ' ', 'lower-right': ' '} 
        player = player_input()

        # Determine who will go first
        turn = goes_first()
        print(turn + " will go first")