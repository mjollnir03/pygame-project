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
        print("\n")
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
        return "Tie, no winner this round!"
    elif(local_player == "Rock" and local_computer == "Scissor"):
        local_player = "Rock Wins!"
        return local_player
    elif(local_player == "Paper" and local_computer == "Rock"):
        local_player = "Paper Wins!"
        return local_player
    elif(local_player == "Scissor" and local_computer == "Paper"):
        local_player = "Scissor Wins!"
        return local_player
    else:
        local_computer = "Computer Won, :("
        return local_computer


def main():
    cont = True
    while cont:
        print("Welcome to Rock, Paper and Scissors!", "\n")
        random_int = rdm.randint(1,3)
        user_input = 0
        while user_input == 0:
            user_input = int(input("Enter from options below: \n 1) -> ROCK\n 2) -> PAPER\n 3) -> SCISSOR\n ENTER HERE: "))
            if(user_input >= 1 and user_input <= 3): pass
            else: 
                user_input = 0
                print("Input invalid, try again!")
        
        player1 = PlayerChoice(user_input,0)
        player1.set_choices()
        player1.print_type()

        computer1 = PlayerChoice(random_int,0)
        computer1.set_choices()
        computer1.print_type()

        temp = compare_object_choices(player1, computer1)
        print("\n")
        print(temp)
        print("\n")

        a = input("Do you want to continue? - (y/n):  ")
        if(a == 'y'): cont = True
        else: cont = False



main() #main function
