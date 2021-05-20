#!/usr/bin/env python3

# Created by Brian Musembi
# Created on May 2021
# This program finds the factors of any number inputted by the user


def main():
    # This function finds the factors of any number inputted by the user

    print("This program finds the factors of any number inputted by the user.")

    while True:
        # Input
        number_string = input("Input any positive integer: ")

        # Process
        try:
            number = int(number_string)
            assert number > 0
            break
        except AssertionError:
            # Output
            print("{} is not a positive integer. Please try again!"
                  .format(number_string))
        except Exception:
            # Output
            print("{} is not a number. Please try again!"
                  .format(number_string))

    factors = []

    for loop_counter in range(number + 1):
        loop_counter = loop_counter + 1
        if number % loop_counter == 0:
            factors.append(loop_counter)

    print("The factors of {} are:".format(number), factors)


if __name__ == "__main__":
    main()
