"""
Hazelyn Cates
This program calculates number of generations, number of cells, growth rate, and generation time of bacteria
Started 11/20/20
Finished 12/12/20
"""

import Calculations

print("Pick a calculation:")
print("1 - calculate total number of cells")
print("2 - calculate number of generations")
print("3 - calculate generation/doubling time")
print("4 - calculate growth rate")
print("5 - exit\n")

answer = int(input())
#print(answer)

while answer != 5:
    if answer == 1:
        Calculations.calculation_1(1)
        print("Pick a calculation:")
        print("1 - calculate total number of cells")
        print("2 - calculate number of generations")
        print("3 - calculate growth rate")
        print("4 - calculate generation/doubling time")
        print("5 - exit\n")

    elif answer == 2:
        Calculations.calculation_2(1)
        print("Pick a calculation:")
        print("1 - calculate total number of cells")
        print("2 - calculate number of generations")
        print("3 - calculate growth rate")
        print("4 - calculate generation/doubling time")
        print("5 - exit\n")

    elif answer == 3:
        Calculations.calculation_3(1)
        print("Pick a calculation:")
        print("1 - calculate total number of cells")
        print("2 - calculate number of generations")
        print("3 - calculate growth rate")
        print("4 - calculate generation/doubling time")
        print("5 - exit\n")

    elif answer == 4:
        Calculations.calculation_4(1)
        print("Pick a calculation:")
        print("1 - calculate total number of cells")
        print("2 - calculate number of generations")
        print("3 - calculate growth rate")
        print("4 - calculate generation/doubling time")
        print("5 - exit\n")

    answer = int(input())




