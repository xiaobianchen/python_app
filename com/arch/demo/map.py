#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenxiaobian'
from functools import reduce


def f(x):
    return x * x


r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

# 把list所有元素转换为字符串
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def add(x, y):
    return x + y


result = reduce(add, [1, 3, 5, 7, 9])
print(result)


def fn(x, y):
    return x * 10 + y


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print(reduce(fn, [1, 3, 5, 7, 9]))
print(reduce(fn, map(char2num, '13579')))


# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']

def normalize(name):
    # 这里用切片
    return name[0].upper() + name[1:].lower()


r1 = map(normalize, ['adam', 'LISA', 'barT'])
print(list(r1))

print('--------------')


#reduce求积
def prod(L):
    return reduce(lambda x,y:x*y,L)

print(prod([1,2,3,4]))

#把字符串转换成浮点数
def str2float(s):
    return {'0':0.0,'1':1.0,'2':2.0,'3':3.0}



