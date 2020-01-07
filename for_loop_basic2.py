#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 11:27:43 2018

@author: ArunRam
"""

def makeItBig(arr):
    for i in range(len(arr)):
        if arr[i] > 0:
            arr[i] = "big"
    return arr

x = makeItBig([-1,3,5,-5])
print(x)



def countPos(arr):
    count = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            count += 1
    arr[len(arr)-1] = count
    return arr

x = countPos([-1,1,1,1])
print(x)



def sumTotal(arr):
    sum = arr[0]
    for i in range(1,len(arr)):
        sum += arr[i]
    return sum
x = sumTotal([1,2,3,4])
print("sum total is ", x)

def average(arr):
    sum = arr[0]
    for i in range(1,len(arr)):
        sum += arr[i]
    return sum/len(arr)
x = average([1,2,3,4])
print("average is ", x)
        


def length(arr):
    count = 0
    while arr != []:
        arr.pop()
        count += 1
    return count
x = length([1,2,3,4])
print("length is ", x)
        
        
def minArray(arr):
    min = arr[0]
    for i in range(1,len(arr)):
        if min > arr[i]:
            min = arr[i]
    return min
x = minArray([-1,-2,-3])
print("minimum is ", x)



def maxArray(arr):
    max = arr[0]
    for i in range(1, len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max
x = maxArray([1,2,3,4,5])
print("maximum is ",x)


def ultimateAnalyze(arr):
    sumTotal = arr[0]
    minimum = arr[0]
    maximum = arr[0]
    for i in range(1, len(arr)):
        sumTotal += arr[i]
        if minimum > arr[i]:
            minimum = arr[i]
        if maximum < arr[i]:
            maximum = arr[i]
    return {"sumTotal":sumTotal, "average":sumTotal/len(arr), "minimum":minimum, "maximum":maximum, "length": len(arr)}

x = ultimateAnalyze([1,2,3,4,5])
print(x)


def reverseArray(arr):
    for i in range(int(len(arr)/2)):
        arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[i]
    return arr

x = reverseArray([1,2,3,4,5])
print(x)




        




