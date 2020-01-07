#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 17:53:54 2018

@author: ArunRam
"""

arr = [1,5,3,2,0,8]

def bubbleSort(arr):
    for j in range(len(arr)-1):
#        print("\n", "*"*80, "\n Iteration j =",j)
        for i in range(len(arr)-1-j):
#            print("\n", "*"*80, "\n comparing", arr[i], arr[i + 1])
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
#                print("swapped", arr[i + 1], arr[i])
#                print("array is now:", arr)
#            else: 
#                print("no need to swap", arr[i], arr[i + 1])
#                print("array is still:", arr)
    return arr
print(bubbleSort(arr))




arr = [1,5,3,2,0,8]

def bubbleSortRecursive(arr, num):
    if len(arr) == 1 or num == 1:
        return arr
    for i in range(len(arr)-1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i+1], arr[i]
    return bubbleSortRecursive(arr, num-1)
            
print(bubbleSortRecursive(arr, len(arr)))   
        