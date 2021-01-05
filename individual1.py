#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти наибольший элемент и переставить его с первым
# элементом. Преобразованный массив вывести.


import sys

if __name__ == '__main__':
    A = list(map(float, input("Введите список из 10 элементов ").split()))
    a_max = A[0]
    i_max = 0
    for i, item in enumerate(A):
        if abs(item) >= abs(a_max):
            i_max, a_max = i, item
    A.insert(i_max, A[0])
    A.pop(i_max+1)
    A.insert(0, a_max)
    A.pop(1)
    print(A)

