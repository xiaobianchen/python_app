#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenxiaobian'

#打印1-100所有偶数
print([x for x in range(1,101) if x%2==0])

#打印1-100所有奇数
print([x for x in range(1,10) if x%2==1])

def is_odd(n):
    return n%2 == 1

#打印出奇数
print(list(filter(is_odd,[1,2,3,4,5,6])))

#删除空字符串
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty,['A', '', 'B', None, 'C', '  '])))
