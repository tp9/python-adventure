#!/usr/bin/env python
# -*- coding: utf-8 -*-
from game import *
import sys, os

def main():
    new_game = Game()
        
    while new_game.play != False:
        new_game.play()
    
        keep_playing = input("Would you like to play again (y or n)?").lower()
        while not keep_playing in ("yn"):
            print("Please enter y or n")
            keep_playing = input("Would you like to play again (y or n)?").lower()
        else:
            if keep_playing == 'n':
                input("Thanks for playing!")
                new_game.play = False
    os._exit(1)        
        
        
#test area
if __name__ == '__main__':
    main()