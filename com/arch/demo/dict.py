#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenxiaobian'

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Bob'])
print(d.get('Bob'))
print('-------------')

d.pop('Bob')
print(d)

