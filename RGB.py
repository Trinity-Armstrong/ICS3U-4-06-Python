#!/usr/bin/env python3

# Created by: Trinity Armstrong
# Created on: November 2019
# This program outputs all the RGB colour codes


def main():
    # This function outputs all the RGB colour codes

    red = 0
    green = 0
    blue = 0

    # process & output
    for red in range(256):
        for green in range(256):
            for blue in range(256):
                print("RGB: {0},{1},{2}"
                      .format(red, green, blue))


if __name__ == "__main__":
    main()
