#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenxiaobian'

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for item in d.items():
    print(item)


from collections import Iterable
# str是否可迭代
print(isinstance('abc',Iterable))

# list是否可迭代
print(isinstance([1,2,3],Iterable))

#整数是否可迭代
print(isinstance(123,Iterable))

print('-----------')

list = ['A','B','C']
list2 = [(1,1),(2,4),(3,9)]
for i,value in enumerate(list):
    print(i,value)

print('----------------')
for x,y in list2:
    print(x,y)




