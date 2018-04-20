#!/usr/bin/env python

from __future__ import print_function

row1=['R','N','B','K','Q','B','N','R']
row2=['P','P','P','P','P','P','P','P']
row3=['','','','','','','','']
row4=list(row3)
row5=list(row3)
row6=list(row3)
row7=['p','p','p','p','p','p','p','p']
row8=['r','n','b','q','k','b','n','r']

board=[row1,row2,row3,row4,row5,row6,row7,row8]

def printBoard(board):
     row = 7
     while row != -1:
             column = 0
             while column != 8:
                     print(board[row][column], end='')
                     column = column + 1
             print()
             row = row - 1
             
printBoard(board)