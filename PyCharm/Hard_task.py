#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    m = tuple(int(i) for i in input('введите элементы кортеджа: \n').split())
    n = tuple(item * (i + 1) if (i + 1) % 2 != 0 else item / (i + 1) for i, item in enumerate(m))

    print(n)
