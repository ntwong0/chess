#!/usr/bin/env python

from __future__ import print_function

#      0   1   2   3   4   5   6   7
row1=['R','N','B','K','Q','B','N','R']
row2=['P','P','P','P','P','P','P','P']
row3=[' ',' ',' ',' ',' ',' ',' ',' ']
row4=list(row3)
row5=list(row3)
row6=list(row3)
row7=['p','p','p','p','p','p','p','p']
row8=['r','n','b','q','k','b','n','r']

board=[row1,row2,row3,row4,row5,row6,row7,row8]

def printChessPiece(letter):
  

def printRow(row):
  column = 0
  while column != 8:
    print(row[column], end='')
    print(" | ", end='')
    column = column + 1
    
def printBoard(board):
  row = 0
  print("   | a | b | c | d | e | f | g | h |")
  print("---+---+---+---+---+---+---+---+---+---")
  while row != 8:
    # print(row[column], end='')
    print(" ", end='')
    print(8-row, end='')
    print(" | ", end='')
    printRow(board[row])
    print(8-row, end='')
    print()
    print("---+---+---+---+---+---+---+---+---+---")
    row = row + 1
  print("   | a | b | c | d | e | f | g | h |")

def checkCommand(command):
  if len(command) != 4 \
    or command[0] < '1' or command[0] > '8' \
    or command[1] < 'a' or command[1] > 'h' \
    or command[2] < '1' or command[2] > '8' \
    or command[3] < 'a' or command[3] > 'h':
      print("Sorry, try again.")
      print("Example: if you'd like to move a piece")
      print("  from Row 2, Column a")
      print("  to   Row 4, Column a")
      print("then enter: 2a4a")
      return False
  else:
      return True

def askNextMove():
  print()
  printBoard(board)
  print("What's your move?")
  print(">>> ", end='')
    
print("Let's play chess!")
command = 0
while command != 'quit':
  askNextMove()
  command = raw_input()
  if command == 'quit':
    break
  elif checkCommand(command):
    pass
  else:
    pass
  
  
  
