#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 11:00:39 2021

@author: amaancharaniya
"""

import os
import operator
import sys
os.chdir('/Users/amaancharaniya/Documents/python_summer2021/HW')


#This algorithm compares a given number in the array to the previous one and swaps the position to place them in sequential order
def insertionsort(array):
    #we iterate through the sequence
    for i in range (1, len(array)):
        #assign one element as our primary
        elem = array[i]
        #assign the element before to compare it to
        j = i-1
        while j >= 0 and elem < array[j]:
            array[j+1] = array[j] #if the element before is bigger we swap them
            j -= 1 #we reset our j
        array[j+1] = elem #we reset our element of interest before going back through

array = [4, 25, 9, 17, 33, 27, 3, 15]
insertionsort(array)
print(array)

#This is an interesting algorithm that compares two numbers in an array and swaps them if needed. It goes left to right than right to left!
def cocktailsort(array):
    begin = 0
    flag = True
    #We set the flad to default as true
    while (flag == True):
        flag = False
        #we want to compare two numbers all the way through to the last two.
        for i in range(begin, len(array)-1):
            if (array[i] > array[i+1]):
                array[i], array[i+1] = array[i+1], array[i] #swap them if one is bigger
                flag = True
        if(flag == False):
            break
        for i in range(len(array)-2, begin-1, -1):
            if (array[i] > array[i+1]):
                array[i], array[i+1] = array[i+1], array[i]
                flag = True
        begin = begin + 1 #add one to our range and start the process again

array = [4, 25, 9, 17, 33, 27, 3, 15]
cocktailsort(array)
print(array)

#Both algorithms above are on a complexity of n^2 so I opted to graph a simply exponential equation
import matplotlib.pyplot as plt
import numpy as np

def main():
    x = np.linspace(1, 9)
    y = np.exp(x)

    plt.figure()
    plt.plot(x, y)
    plt.xlabel('n')
    plt.ylabel('time')

    plt.show()

if __name__ == '__main__':
    main()
    
