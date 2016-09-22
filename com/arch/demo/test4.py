#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenxiaobian'

L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [ s.lower() for s in L1 if isinstance(s,str)]
print(L2)

#列表式生成数组
L = [x*x for x in range(1,10)]
print(L)

#通过生成器生成
g = (x*x for x in range(1,10))
for n in g:
    print(n)
print('-------------')

#斐波拉契数列
def fibo(n):
    if n<=1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
print(fibo(5))
