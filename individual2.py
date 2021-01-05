#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В списке, состоящем из вещественных элементов, вычислить:
# 1) номер минимального по модулю элемента списка;
# 2) сумму модулей элементов списка, расположенных после первого отрицательного элемента.
# Сжать список, удалив из него все элементы, величина которых находится в интервале [а, b].
# Освободившиеся в конце списка элементы заполнить нулями.

import sys

if __name__ == '__main__':
    A = list(map(float, input().split()))
    if not A:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    a_min = A[0]
    i_min = 0
    for i, item in enumerate(A):
        if abs(item) < abs(a_min):
            i_min, a_min = i, item
    print('Минимальное по модулю число: ', a_min)

    neg = -1
    for i, item in enumerate(A, 1):
        if item < 0:
            neg = i
            break

    if neg == -1:
        print('Отрицательных нет')

    else:
        print('Номер первого отриц.:', neg)
        s = 0
        for i in range(neg, len(A)):
            s += abs(A[i])

        print('Сумма модулей: ', s)

    a = int(input("Введите число а "))
    b = int(input("Введите число b, больше числа a "))
    i = 0
    n = len(A)
    N = n

    while i < n:
        if a <= A[i] <= b:
            del A[i]
            n -= 1

        else:
            i += 1
    for i in range(n, N):
        A.append(0)
    print(A)
