#!/usr/bin/env python

from __future__ import print_function
import string

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
  pass

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
  
def checkNextMove(command):
  current_row = 8 - (ord(command[0]) - ord('0'))
  current_col = ord(command[1]) - ord('a')
  current_piece = board[current_row][current_col]
  

def checkKnightMove(command):
  current_row = 8 - (ord(command[0]) - ord('0'))
  current_col = ord(command[1]) - ord('a')
  next_row = 8 - (ord(command[2]) - ord('0'))
  next_col = ord(command[3]) - ord('a')
  if next_row == current_row + 2 \
     and next_col == current_col - 1:
      return True
  elif next_row == current_row + 2 \
     and next_col == current_col + 1:
      return True
  elif next_row == current_row + 1 \
     and next_col == current_col + 2:
      return True
  elif next_row == current_row + 1 \
     and next_col == current_col - 2:
      return True
  elif next_row == current_row - 1 \
     and next_col == current_col - 2:
      return True
  elif next_row == current_row - 2 \
     and next_col == current_col - 1:
      return True
  elif next_row == current_row - 2 \
     and next_col == current_col + 1:
      return True
  elif next_row == current_row - 1 \
     and next_col == current_col + 2:
      return True
  else:
      return False

# 2c4c
def makeNextMove(command):
  current_row = 8 - (ord(command[0]) - ord('0'))
  current_col = ord(command[1]) - ord('a')
  current_piece = board[current_row][current_col]
  next_row = 8 - (ord(command[2]) - ord('0'))
  next_col = ord(command[3]) - ord('a')
  board[next_row][next_col] = current_piece
  board[current_row][current_col] = ' '

print("Let's play chess!")
command = 0
while command != 'quit':
  askNextMove()
  command = raw_input()
  if command == 'quit':
    break
  elif checkCommand(command):
    makeNextMove(command)
  else:
    pass
  
  
  
