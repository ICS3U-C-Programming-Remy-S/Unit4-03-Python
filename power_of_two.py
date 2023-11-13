#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Nov 8, 2023
# This program will ask the user for a whole number
# and it will tell them the product
# from 0 to their number put the power of 2.


def main():
    # initialize counter and power variables
    power = 1

    # Get the user number as a string and display message about program
    print(
        "This program will ask the user for a whole number and it will tell them the product"
    )
    print("from 0 to their number put the power of 2.")
    user_num_str = input("Please enter a whole integer: ")

    # Catch if the user number is something wrong
    try:
        # Convert user number as a string to int
        user_num_int = int(user_num_str)

        if user_num_int < 0:
            # Message for negative user number
            print("\n{} is not a positive int.".format(user_num_int))

        # loop for factorial of user_number_as_int
        else:
            for counter in range(user_num_int + 1):
                # calculation for the power of 2
                power = counter**2

                # display power
                print("{0} ^ 2 = {1}.".format(counter, power))

    # Display a message to the user if they entered something that is not valid
    except Exception:
        # Message for invalid user number
        print("\n{} is not a valid whole number.".format(user_num_str))


if __name__ == "__main__":
    main()
