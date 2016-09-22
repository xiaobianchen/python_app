#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenxiaobian'

classmates = ['michal', 'bob', 'tracy']
print(classmates)
print(len(classmates))
print('--------------------')

classmates.append('andy')
print(classmates)
print('--------------------')


classmates.insert(1, 'chen')
print(classmates)

classmates.pop()
print(classmates)
print('--------------------')


# 循环
for name in classmates:
    print("name......" + name)

sum = 0
for item in range(101):
    sum = sum + item
print(sum)
print('--------------------')


L = ['Bart','Lisa','Adam']
for i in L:
    print('Hello ' + i)
print('--------------------')

