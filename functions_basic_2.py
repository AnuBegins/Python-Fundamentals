#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 18:32:06 2018

@author: ArunRam
"""

def countdown(num):
    arr = []
    while num >= 0:
        arr.append(num)
        num -= 1
    return arr
x = countdown(10)
print(x)
        


def printReturn(arr):
    print(arr[0])
    return arr[1]
printReturn([1,3])


def firstPlusLength(arr):
    return arr[0] + len(arr)

x = firstPlusLength([1,3,5])
print(x)



def valGreaterThan(arr, n):
    newArr = []
    print("length is ", len(arr))
    if n > len(arr):
        return False
    for count in range(len(arr)):
        if (arr[count] > arr[n - 1]):
            newArr.append(arr[count])
    print(len(newArr))
    return newArr

x = valGreaterThan([1,2, 3, 4, 5], 1)
print (x)


def lengthByValues (num1, num2):
    if (num1 == num2):
        print("Jinx!")
    newArr = []
    for count in range(num1):
        newArr.append(num2)
    return newArr

x = lengthByValues(10,5)
print(x)
        