#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenxiaobian'
import os

L = list(range(1, 11))
print(L)

l1 = []
for item in range(1, 11):
    l1.append(item * item)
print(l1)

print([x*x for x in range(1,11)])

#选出仅为偶数的平方
print([x*x for x in range(1,11) if x%2 == 0])

#找出1-100之间所有的偶数
print([x for x in range(1,101) if x%2 == 0])
print([x for x in range(1,101) if x%2 != 0])

print('-----------------')

#列出当前目录下的所有文件和文件名
print('当前目录下所有文件:' , [d for d in os.listdir('.')])

d = {'x':'A','y':'B','z':'C'}
for key,v in d.items():
    print(key,"=",v)

#把list中所有字符串变成小写
e1 = ['Hello','World','IBM','Apple']
print([s.lower() for s in e1])