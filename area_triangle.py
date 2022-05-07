#!/usr/bin/env python3.10

# Created by: Nicolas Riscalas
# Created on: May 2 2022
# display 5 ints in a line


def calc_area(base, height):
    area = base * height / 2
    print("Your area is {}".format(area))


def main():
    while True:
        base_str = input("What is your base: ")
        height_str = input("What is your height: ")
        try:
            base_from_usr = float(base_str)
            height_from_usr = float(height_str)
            calc_area(base_from_usr, height_from_usr)
        except:
            print("You have to input an integer")
        input("Press <enter> to restart")


if __name__ == "__main__":
    main()
