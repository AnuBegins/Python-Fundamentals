# -*- coding: utf-8 -*-
"""
Spyder Editor

"""

def basic(num):
    for count in range(0,num + 1):
        print(count)
basic(150)


def multiples (divisor,num):
    mult = divisor
    while mult <= num:
        print(mult)
        mult += divisor
        
multiples(5,1000)


def counting (num, divisor1, divisor2):
    for count in range(1, num + 1 ):
        if count % divisor2 == 0:
            print("Coding Dojo")
        elif count % divisor1 == 0:
            print ("Coding")
        else:
            print(count)
  
counting(100, 5, 10)


def addOdds(num):
    sum = 0
    for count in range(1,num):
        if (count % 2) == 1:
#            print(count)
            sum += count
#            print("Sum is ", sum)
    print("Sum is ", sum)
addOdds(500000)

            
def countdown(num, dist):
    print(num)
    while num > dist:
        num -= dist
        print(num)
countdown(2018, 4)



def distWithinRange(lowNum, highNum, dist):
    for count in range(lowNum, highNum + 1):
        if count % dist == 0:
            print(count)
    
distWithinRange(3, 20, 3)
    

list = [3,5,1,2]
for i in list:
    print(i)
    
list = [3,5,1,2]
for i in range(list):
    print(i)

list = [3,5,1,2]
for i in range(len(list)):
#    print(len(list))
    print(i)

    