#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenxiaobian'
import functools

#偏函数的应用
#字符串转换为整数
t1 = int('12345')
print(t1)

#base默认是10进制
t2 = int('12345',base=8)
print(t2)

t3 = int('12345',base=16)
print(t3)

#functions.partial作用就是把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数
int2 = functools.partial(int,base=2)
print(int2('100000'))

