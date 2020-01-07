#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  5 13:11:43 2018

@author: ArunRam
"""

def sortList(arr):
    print("\n", "*" * 80, "\n Length of array is =",len(arr))
    if len(arr) == 1:
        return arr
    
    maxVal = arr[0]
    pos = 0
    print("\nInitializing maxVal =", arr[0])
    print("Initial position of maxVal =", pos)

    for i in range(1,len(arr)):
        if maxVal < arr[i]:
            maxVal = arr[i]
            pos = i
        print("maxVal is:", maxVal)
        print("position of maxVal is:", pos)
        
    #swap the maxVal with the very last element in the array    
    arr[len(arr)-1], arr[pos] = arr[pos], arr[len(arr)-1]
    print("Adjusted array is:", arr)
    arr.pop()
    print("New array is:", arr)
    
    x = sortList(arr) #recursive call
    x = x + [maxVal]  #appends the maxVal from each recursive call of SortList
    print(x)
    
    return x
a = sortList([7,3,5,10,9])
print(a)