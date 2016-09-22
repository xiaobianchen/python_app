#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenxiaobian'


# 利用递归函数计算阶乘
# N!=1*2*3*....N

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


result = fact(5)
print(result)
print('--------------')


# 利用递归函数移动汉诺塔
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
        return
    move(n - 1, a, '-->,',c)
    print('move', a, '-->', c)
    move(n - 1, b, a, c)

move(4,'A','B','C')