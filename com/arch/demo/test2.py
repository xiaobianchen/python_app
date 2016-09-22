#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 切片

__author__ = 'chenxiaobian'

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2

print(n)

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
r = []
for l in range(5):
    r.append(L[l])
print(r)
# 从索引0开始 直到3结束,不包括索引3
print(L[0:3])
print(L[:3])
print(L[1:3])
print(L[-1])
print(L[-2])

print('----------------')

#创建一个0-99的数组
L = list(range(100))
print(L)
print(L[0:10])
print(L[-10:])
print(L[11:21])
print(L[:10:2])
print('-------------------')

print('ABCDEF'[:3])
print('ABCDEF'[::2])