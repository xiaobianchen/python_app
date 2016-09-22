#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenxiaobian'

L = [36, 5, -12, 9, -21]
str = ['bob', 'about', 'Zoo', 'Credit']

result = sorted(L, reverse=True)
result2 = sorted(str)
print(result)
print(result2)

scores = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 按照名字进行排序
print('按照名字排序第一种方式:', sorted(scores, key=lambda x: x[0]))
print('按照名字排序第二种方式:', sorted(scores, key=lambda x: x[0], reverse=True))
print('按成绩从高到低排序', sorted(scores, key=lambda x: x[1], reverse=True))
print('-----------------')

#按照名字排序
def by_name(t):
    return t[0].lower()

#按照成绩排序
def by_score(t):
    return t[1]


print(sorted(scores,key=by_name))
print(sorted(scores,key=by_score,reverse=True))

#定义匿名函数
result3 = list(map(lambda x:x*x,[1,2,3,4]))
print(result3)










