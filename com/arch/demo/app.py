#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'chenxiaobian'

# 定义模块

import sys


def app():
    args = sys.argv
    if len(args) == 1:
        print('Hello World')
    elif len(args) == 2:
        print('Hello  %s' % args[1])
    else:
        print('Too many arguments!')


if __name__=='__main__':
    app()