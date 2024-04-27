from colorama import Fore, Back, Style, just_fix_windows_console
import statistics
import math
import random
from time import sleep
just_fix_windows_console()

#  Names
name1 = "Name1"
name2 = "Name2"
name3 = "Name3"

#  Numbers
num1 = random.randint(1,40)
num2 = random.randint(1,40)
num3 = random.randint(1,40)

#  Style
symbol = " "
color1 = Back.RED
color2 = Back.GREEN
color3 = Back.BLUE

#  Start

print(f'{name1} = {color1} {symbol*num1}{Style.RESET_ALL} {num1}')
print(f'{name2} = {color2} {symbol*num2}{Style.RESET_ALL} {num2}')
print(f'{name3} = {color3} {symbol*num3}{Style.RESET_ALL} {num3}')