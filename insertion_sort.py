#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 19:44:56 2018

@author: ArunRam
"""
arr = [50,32,2,77,25]


def insertionSort(arr):
    for i in range(1,len(arr)):
        print("\n", "*"*80, "\n Iteration i =",i)
        temp = arr[i]
        print("\n temp is ",arr[i])
        j = i - 1
        print("\n initialize j at ", j)
        while j>=0 and arr[j] > temp:
            print("\n", "*"*80, "\n Iteration j =", j)
            print("arr[j] is ", arr[j])
            arr[j+1] = arr[j]
            print("arr is", arr)
            j = j-1
            print("new j is", j)
        arr[j+1] = temp
        print("arr is", arr)
    return arr
print(insertionSort(arr))

        