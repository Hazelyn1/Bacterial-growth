"""
This file carries out the bacterial growth calculations
"""

import math

def calculation_1(n): #calculate total cell number
    print("Enter initial cell number")
    initial_cell = int(input())
    # print(initial_cell)
    print("Enter generation number")
    gen_num = int(input())
    total_cell = (pow(2, gen_num)) * initial_cell
    print("%d total cells" % total_cell)
    print("\n")

    print("Do you want to do any other calculations with this data?")
    print("1 - calculate growth rate")
    print("2 - calculate generation/doubling time")
    print("3 - exit\n")
    answer = int(input())

    if answer == 1: #growth rate
        print("Enter growth time in hours")
        time = float(input())
        growth_rate = gen_num / time
        print("Growth rate: %.2f generations per hour" % growth_rate)
        print("\n")

        print("Do you want to calculate doubling time?")
        print("1 - yes     2 - no")
        choice = int(input())

        if choice == 1: #doubling time
            doubling_time = 1 / growth_rate
            print("Doubling time: %2.f hours per generation" % doubling_time)
            print("\n")

        elif choice == 2:
            return

    elif answer == 2: #doubling time
        print("Enter growth time in hours")
        time = float(input())

        doubling_time = time / gen_num
        print("Doubling time: %.2f hours per generation" % doubling_time)

        print("Do you want to calculate growth rate?")
        print("1 - yes     2 - no")
        choice = int(input())

        if choice == 1: #growth rate
            growth_rate = gen_num / time
            print("Growth rate: %.2f generations per hour")

        elif choice == 2:
            return


def calculation_2(n): #calculate number of generations
    print("Enter initial cell number")
    initial_cell = int(input())
    print("Enter total cell number")
    total_cell = int(input())
    gen_num = (((math.log(total_cell, 10))-(math.log(initial_cell, 10))) / 0.301)
    print("%d generations" % gen_num)
    print("\n")
    #since generations aren't decimals, this rounds down

    print("Do you want to do any other calculations with this data?")
    print("1 - calculate growth rate")
    print("2 - calculate generation/doubling time")
    print("3 - exit\n")
    answer = int(input())

    if answer == 1: #growth rate
        print("Enter growth time in hours")
        time = float(input())
        growth_rate = gen_num / time
        print("Growth rate: %.2f generations per hour" % growth_rate)
        print("\n")

        print("Do you want to calculate doubling time?")
        print("1 - yes     2 - no")
        choice = int(input())

        if choice == 1:  # doubling time
            doubling_time = 1 / growth_rate
            print("Doubling time: %2.f hours per generation" % doubling_time)
            print("\n")

        elif choice == 2:
            return

    elif answer == 2:  # doubling time
        print("Enter growth time in hours")
        time = float(input())

        doubling_time = time / gen_num
        print("Doubling time: %.2f hours per generation" % doubling_time)

        print("Do you want to calculate growth rate?")
        print("1 - yes     2 - no")
        choice = int(input())

        if choice == 1:  # growth rate
            growth_rate = gen_num / time
            print("Growth rate: %.2f generations per hour")

        elif choice == 2:
            return


def calculation_3(n): #calculate doubling/generation time
    print("Enter growing time in hours")
    time = float(input())
    print("1 - enter generation number")
    print("or")
    print("2 - calculate generation number")
    choice = int(input())
    #print(choice)

    if choice == 1: #enter generation number
        print("Enter generation number")
        gen_num = int(input())
        doubling_time = time / gen_num
        print("Doubling time is %.2f hours/generation" % doubling_time)
        print("\n")

    elif choice == 2: #calculate generation number
        print("Enter initial cell number")
        initial_cell = int(input())
        print("Enter total cell number")
        total_cell = int(input())
        gen_num = (((math.log(total_cell, 10)) - (math.log(initial_cell, 10))) / 0.301)
        doubling_time = time / gen_num
        print("Doubling time is %.2f hours" % doubling_time)
        print("\n")

def calculation_4(n): #calculate growth rate
    print("Enter growing time in hours")
    time = float(input())
    print("1 - enter generation number")
    print("or")
    print("2 - calculate generation number")
    choice = int(input()) #PROBLEM: works ok, but have to input "2" twice to get it to work
                          #works fine if "1" is typed in once
                          #idk what's wrong with it

    if choice == 1:
        print("Enter generation number")
        gen_num = int(input())
        growth_rate = gen_num / time
        print("Growth rate is %.2f generations per hour" % growth_rate)
        print("\n")

    elif choice == 2:
        initial_cell = int(input())
        print("Enter total cell number")
        total_cell = int(input())
        gen_num = (((math.log(total_cell, 10)) - (math.log(initial_cell, 10))) / 0.301)
        growth_rate = gen_num / time
        print("Growth rate is %.2f generations per hour" % growth_rate)
        print("\n")

    print("Do you want to calculate doubling time with this data?")
    print("1 - yes")
    print("2 - no & exit\n")

    answer = int(input())

    if answer == 1:
        doubling_time = 1 / growth_rate
        print("Doubling time is %.2f hours" % doubling_time)
        print("\n")

    elif answer == 2:
        return
