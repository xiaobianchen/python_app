#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenxiaobian'

import math


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


result = my_abs(-10)
print(result)

print('----------')


# 如果想定义一个什么事也不做的空函数 可以用pass语句,pass可以用来作占位符
def nop():
    pass


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
print('-----------------')


def power(x):
    return x * x


result = power(15)
print(result)
print('---------------')


def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

results = fact(5)
print(results)


