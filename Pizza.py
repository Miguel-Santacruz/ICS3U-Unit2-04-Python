#!/usr/bin/env python3

# Created by: Miguel Santacruz
# Created on: March 2022
# This program calculates the cost of a pizza
#    with diameter inputted by the user

import Constants


def main():
    # this function calculates cost of pizza

    # input
    diameter = int(input("Enter diamter of the pizza you would like (inches): "))

    # process
    sub_total = Constants.Rent + Constants.Labor + (Constants.Cost_per_inch * diameter)
    HST = sub_total * Constants.HST
    Total = sub_total + HST

    # output
    print("")
    print("The cost for a {0} inch pizza is: ${1:,.2f}".format(diameter, Total))

    print("\nDone.")


if __name__ == "__main__":
    main()
