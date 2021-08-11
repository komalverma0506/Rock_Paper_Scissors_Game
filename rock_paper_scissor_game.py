"""
    Rock Paper Scissor Game
"""
import os
import sys
from getpass import getpass
import time
from random import choice, randint

WIDTH = os.get_terminal_size().columns

if sys.platform == 'win32' or sys.platform == 'win64':
    os.system('cls')# windows
else:
    os.system('clear') # linux, macos

print("_"*WIDTH)
print('\n\n')
print(time.ctime())
print("Welcome to Rock Paper Scissor Game".center(WIDTH))
print('\n\n')
print("_"*WIDTH)
print('\n\n')

choices = ['rock', 'paper', 'scissor']

ch = input("Do you want to play with computer yes/no :").strip().lower()
if ch in ('yes', 'y', 'yo', 'true'):
    name1 = input("Enter Player Name: ").strip().upper()
    name2 = "Computer"
    print("\n\n")
    p1_ch = getpass(f"{name1:>20} Choice (Rock, Paper, Scissor): ").strip().lower()
    p2_ch = choice(choices)
else:
    name1 = input("Enter Player-1 Name: ").strip().upper()
    name2 = input("Enter Player-2 Name: ").strip().upper()
    print("\n\n")
    p1_ch = getpass(f"{name1:>20} Choice (Rock, Paper, Scissor): ").strip().lower()
    p2_ch = getpass(f"{name2:>20} Choice (Rock, Paper, Scissor): ").strip().lower()


print("\n\n")

if p1_ch not in choices or p2_ch not in choices:
    # this is invalid input condition
    print("Error!!!Mind your Input!! only Rock or Paper or Scissor is allowed."\
    .center(WIDTH))
    print("\n\n")
    print("_"*WIDTH)
    print('\n\n')
    sys.exit(1) # stop executing your program and return to shell / terminal
    # with exit code - 1 (Error Code, Status Code)
print(f"{name1:>20} Choice : {p1_ch.upper():<8}".center(WIDTH))
print(f"{name2:>20} Choice : {p2_ch.upper():<8}".center(WIDTH))
print("\n\n")
print(".........................Processing...............", end='', flush=True)
for _ in range(randint(3, 10)):
    print('.', end='', flush=True) # lazy execution / evaluation
    time.sleep(1)
print("\n\n")

p1_win = [('rock', 'scissor'), ('paper', 'rock'), ('scissor', 'paper')]

if p1_ch == p2_ch:
    print("!!!!MATCH TIE!!!!".center(WIDTH))
elif (p1_ch, p2_ch) in p1_win:
    print(f"!!!!{name1} HAS WON THE GAME!!!!".center(WIDTH))
else:
    print(f"!!!!{name2} HAS WON THE GAME!!!!".center(WIDTH))

print('\n\n')
print("_"*WIDTH)
print("\n")
sys.exit(0)
