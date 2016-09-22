#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，
# 也就无法保证set内部“不会有重复元素”

__author__ = 'chenxiaobian'

s = set([1,2,3,4])
s.add(5)
s.remove(4)
print(s)

print('-----------')

s1 = set([1,2,3])
s2 = set([2,3,4])

result = s1&s2
print(result)

result2 = s1|s2
print(result2)

print('--------')
list1 = ['abc','def']
s3 = set(list1)
print(s3)

print('-----------')
a = ['b','c','a']
a.sort()
print(a)

print('------------')
a = 'abc'
print(a.replace('a','A'))
print(a)

print('------------')
#tuple不可变
s4 = set((1,2,3))
print(s4)

#list为可变类型 不符合key不能重复规则
s5 = set((1,4,3))
print(s5)

t1 = (1,3,4,4)
print(t1)