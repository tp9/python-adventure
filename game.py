from player import *
from room import *

class Game():
    def __init__(self):
        self.create_rooms()

    def play(self):
        self.print_welcome()
        
    def print_welcome(self):
        player_name = input("Who are you: ")
        self.the_player = Player(name=player_name, room=self.outside)
        print("Welcome", self.the_player.name, ", your HP is at", self.the_player.hp)
        print("You are standing", self.the_player.current_room.description)
    
    def create_rooms(self):
        self.outside = Room("outside your front door")

        
