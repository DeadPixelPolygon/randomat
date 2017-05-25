"""
Randomat game engine Alpha 1.0
Written by Matias Z in Python 3.x

Randomat is a (very primitive)
game engine for text based
adventure games.

=================================

Usage:
main game file as main.py
	Should contain a class
	player with attributes
	px and py.
	
tiles as tiles.py

=================================
"""

#imports
import time	#used for pausing the program
from main import *		#main  game  and player attributes
from tiles import *	#world tiles

#main engine loop
def engine():
	
