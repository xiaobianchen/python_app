#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenxiaobian'

param1 = input('身高:')
param2 = input('体重:')

bmi = (float)(param2)/(float)(param1)/(float)(param1)

if bmi<18.5:
    print("过轻")
elif 18.5<=bmi<25:
    print("正常")

elif 25<=bmi<28:
    print("肥胖")

else:
    print("严重肥胖")