#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 18:33:02 2018

@author: ArunRam
"""


arr = [50,32,2,77,25]

def selectionSort(arr):    
    for i in range(0,len(arr)):
        print("\n", "*"*80, "\n Iteration i =",i)
        min_idx = i  # we only need to track the position value of the minimum, not the actual minimum value
        print("\n", "*"*80, "\n min_idx, is ",i)

        for j in range(i + 1, len(arr)):
            print("\n", "*"*80, "\n Iteration j =",j)
            if arr[min_idx] > arr[j]:
                min_idx = j
                print("min_idx is ", min_idx)
            else: 
                print("no need to swap", arr[min_idx], arr[j])
                print("array is still:", arr)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print("swapping new min of ", arr[i], "with", arr[min_idx])
        print("array is now:", arr)

    return arr
print(selectionSort(arr))
        
