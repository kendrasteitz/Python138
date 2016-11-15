#! /usr/bin/python
# Exercise No.   3
# File Name:     AntsGoMarching.py
# Programmer:    Kendra Steitz
# Date:          October 1, 2016
#
# Problem Statement:
#   Program outputs the song lyrics to "The Ants Go Marching"
#
# Overall Plan:
#   1. Create a song function that takes in two strings
#       one for the number and the other for the action of
#       the little one.
#   2. In main call upon song function inputting the two necessary
#       strings for verse.
#           ex: song("one", "suck his thumb.")
#               song("two", "tie his shoe.")
#               etc.
#



def song(number, verse):


    print("The ants go marching", number, "by", number, "hurrah! hurrah!")
    print("The ants go marching", number, "by", number, "hurrah! hurrah!")
    print("The ants go marching", number, "by", number)
    print("The little one stops to", verse)
    print("And they all go marching down...")
    print("In the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! Boom! Boom!")



def main():

    song("one", "suck his thumb.")
    print()
    song("two", "tie his shoe.")
    print()
    song("three", "take a pee.")
    print()
    song("four", "slam the door.")
    print()
    song("five", "take a sigh.")
    print()
    song("six", "pick up sticks.")
    print()
    song("seven", "pray to heaven.")
    print()
    song("eight", "roller skate.")
    print()
    song("nine", "check the time.")
    print()
    song("ten", "shout The End.")


main()

