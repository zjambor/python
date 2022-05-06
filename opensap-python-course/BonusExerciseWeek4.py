"""
In the following, we play 100 consecutive games. Each player has to hand in a file consisting of one letter per line. The letters are either “R”, “P” or “S”.

Write a Python Program that reads two files player1.txt and player2.txt. 
These files are organized according to the above rules. The program should compare both inputs 
and calculate how many games have been won by player1, by player2 and how many games ended in a draw. 
The results are written into a file result.txt which looks as follows:

Player1 wins: 23
Player2 wins: 48
Draws: 29

The sum should always be 100.
"""

import random

letters = ["R", "P", "S"]

def write_file(filename):
    with open(filename, "w") as file:
        for i in range(100):
            file.write(random.choice(letters) + "\n")

write_file("player1.txt")
write_file("player2.txt")

player1_choices = []
player2_choices = []

def read_files(filename, choices):
    with open(filename, "r") as file:
        for lines in file:
            choices.append(lines.strip())

read_files("player1.txt", player1_choices)
read_files("player2.txt", player2_choices)

player1_wins = 0
player2_wins = 0
draws = 0

for choice in range(len(player1_choices)):
    if player1_choices[choice] == player2_choices[choice]:
        draws += 1
    else:
        if player1_choices[choice] == "R":
            if player2_choices[choice] == "S":
                player1_wins += 1
            elif player2_choices[choice] == "P":
                player2_wins += 1
        if player1_choices[choice] == "S":
            if player2_choices[choice] == "R":
                player2_wins += 1
            elif player2_choices[choice] == "P":
                player1_wins += 1
        if player1_choices[choice] == "P":
            if player2_choices[choice] == "S":
                player2_wins += 1
            elif player2_choices[choice] == "R":
                player1_wins += 1

print("Player1 wins: ", player1_wins)
print("Player2 wins: ", player2_wins)
print("Draws: ", draws)
print("sum:", player1_wins + player2_wins + draws)

with open("result.txt", "w") as result_file:
    result_file.write("Player1 wins: " + str(player1_wins) + "\n")
    result_file.write("Player2 wins: " + str(player2_wins) + "\n")
    result_file.write("Draws: " + str(draws) + "\n")