#Tutorial 8

import random
import time

def display_intro():
    print("You are in the Kingdom of Dragons. In front of you, you see two caves. In one cave, the dragon is friendly and will share his treasure with you. The other dragon is hungry and will eat you on sight.")

def choose_cave():
    choice = int(input("Which cave will you go into? (1 or 2): "))
    try:
        return choice
    except ValueError:
        print(ValueError)

def check_cave(chosen_cave):
    FriendlyDragonCave = random.randint(1,2)
    if chosen_cave==FriendlyDragonCave:
        time.sleep(1)
        print('You Win!')
    else:
        time.sleep(1)
        print('You Lose!')

display_intro()
cave_number = choose_cave()
check_cave(cave_number)

class circle():
    def __init__(self,r):
        self.radius = r

    def area(self):
        return self.radius**2 * 3.14

    def perimeter(self):
        return 2*self.radius*3.14

new_circle = circle(1)
print(new_circle.area())
print(new_circle.perimeter())