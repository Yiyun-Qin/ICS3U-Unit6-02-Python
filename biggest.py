#!/usr/bin/env python3

# Created by Yiyun Qin
# Created in May 2022
# This is the math program, finding the biggest values in numbers

import random


def biggest_number(list_of_numbers):
    # This function finds the maximum value
    maximum = 0
    for loop_counter in range(len(list_of_numbers)):
        if list_of_numbers[loop_counter] > maximum:
            maximum = list_of_numbers[loop_counter]
    return maximum


def main():
    # This function gets random numbers and does output
    random_number = []

    # input
    print("Here is a list of random numbers: \n")
    for loop_counter in range(0, 10):
        single_number = random.randint(1, 100)
        random_number.append(single_number)
        print("The random number is {}".format(single_number))

    # process & output
    answer = biggest_number(random_number)
    print("\nThe largest number is {}".format(answer))
    print("\nDone.")


if __name__ == "__main__":
    main()
