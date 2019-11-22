#!/usr/bin/env python3

# Created by: Jacob Bonner
# Created on: November 2019
# This program can calculate the volume of a cylinder


import math


def calculate(radius, height):
    # This function calcuculates the volume of a cylinder

    # Process
    volume = (math.pi*radius**2)*height

    return volume


def main():
    # This function takes two inputs then outputs the volume of a cylinder

    # Process
    while True:
        # Input
        user_radius = input("Enter the radius of your cylinder here (cm): ")
        user_height = input("Enter the height of your cylinder here (cm): ")

        try:
            user_radius = int(user_radius)
            user_height = int(user_height)
            volume = calculate(height=user_height, radius=user_radius)
            if user_radius == int(user_radius) and \
               user_height == int(user_height):
                print("")
                print("The volume of your cylinder is {0}cm^3".format(volume))
                break
            else:
                print("Error, unable to process inputs")
        except Exception:
            print("Error, one or both inputs not integers")
            print("")


if __name__ == "__main__":
    main()
