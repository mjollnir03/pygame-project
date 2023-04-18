#Ellmaer Ranbjer

import random as rdm
#import pygame as pg #will use later

class PlayerChoice:

    rock_string_ascii = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

    paper_string_ascii = """ 
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

    scissor_string_ascii = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    """

    def __init__(self, choice, player_type):
        self.choice = choice
        self.player_type = player_type

    def set_choices(self):
        if self.choice == 1: 
            self.choice = self.rock_string_ascii
            self.player_type = "Rock"
        elif self.choice == 2: 
            self.choice = self.paper_string_ascii
            self.player_type = "Paper"
        elif self.choice == 3: 
            self.choice = self.scissor_string_ascii
            self.player_type = "Scissor"

    def get_choices(self):
        return self.player_type

    def print_type(self):
        print("Chosen:", self.player_type )
        print(self.choice)



def compare_object_choices(a,b):
    '''
    local_player = a.player_type        #this works but looks funny lol
    local_computer = b.player_type
    '''
    local_player = a.get_choices()
    local_computer = b.get_choices()
    if(local_player == local_computer):
        return "Tie"
    elif(local_player == "Rock" and local_computer == "Scissor"):
        return local_player
    elif(local_player == "Paper" and local_computer == "Rock"):
        return local_player
    elif(local_player == "Scissor" and local_computer == "Paper"):
        return local_player
    else:
        return local_computer






def main():
    random_int = rdm.randint(1,3)
    user_input = int(input("Enter from options below: \n 1) -> ROCK\n 2) -> PAPER\n 3) -> SCISSOR\n ENTER HERE: "))
    print("\n")
    player1 = PlayerChoice(user_input,0)
    player1.set_choices()
    player1.print_type()

    computer1 = PlayerChoice(random_int,0)
    computer1.set_choices()
    computer1.print_type()

    temp = compare_object_choices(player1, computer1)
    print(temp)



main() #main function