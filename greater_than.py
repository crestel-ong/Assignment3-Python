#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Sept 2021
# This is the greater than program


def main():
    # this function displays the larger number out of two integers

    # tell user what to do
    print("Print two different numbers to see which is the greater number.")

    # input
    first_as_string = input("Enter the first number (integer): ")
    second_as_string = input("Enter the second number (integer): ")

    try:
        # convert these strings into integers
        first_as_integer = int(first_as_string)
        second_as_integer = int(second_as_string)

        # process and output
        if first_as_integer < second_as_integer:
            print("The greater number is {0}.".format(second_as_integer))
        else:
            print("The greater number is {0}.".format(first_as_integer))
    except Exception:
        print("Invalid input.")
    print("\nDone.")


if __name__ == "__main__":
    main()
