#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 15:51:42 2018

@author: ArunRam
"""

x = [ [5,2,3], [10,8,9] ] 


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]


sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]



x[1][0] = 15
print(x) 
print("\n", "*"*80)



students[0]["last_name"] = "Bryant"
#print(students)


for key,val in sports_directory.items():
    print(key," = ",val)
print("\n", "*"*80)

    
#print(sports_directory.keys())
    
sports_directory.get('soccer')[0] = 'Andres'

print(sports_directory.get('soccer'))
print("\n", "*"*80)

    
    
z[0]['y'] = 30
print(z[0]['y'])
print("\n", "*"*80)




students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


def iterateDictionary(listt):
    for dict in listt:
        for key,val in dict.items():
            print(key, "-", val)
iterateDictionary(students)
print("\n", "*"*80)



def iterateDict2(key_name,listt):
    for dict in listt:
        print(dict.get(key_name))     #returns the value of the given key in the dictionary
iterateDict2("first_name",students)
print("\n", "*"*80)



dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printDojoInfo(dict):
    for key in dict.keys():
        print(len(dict.get(key)), " - ", key)  #returns number of elements in array assigned as a value to the key
        for val in dict.get(key):
            print(val)
        print("\n")

printDojoInfo(dojo)
print("\n", "*"*80)

    
    
    




        
