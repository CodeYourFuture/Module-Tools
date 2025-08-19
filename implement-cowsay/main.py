import cowsay
import argparse
import sys


parser = argparse.ArgumentParser(description="displays cowsay charactor with given arguments")
parser.add_argument('animal', type=str, choices=cowsay.char_names, default="cow", help= 'please enter a valid animal')
parser.add_argument('message', type=str, help= 'please enter a message')
arg = parser.parse_args()

animal_func = getattr(cowsay, arg.animal)
print(animal_func(arg.message))
