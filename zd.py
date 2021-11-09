#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import timeit
from functools import lru_cache

if __name__ == '__main__':
    def fib(n):
        if n == 0 or n == 1:
            return n
        else:
            return fib(n - 2) + fib(n - 1)


    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    @lru_cache
    def fibOpt(n):
        if n == 0 or n == 1:
            return n
        else:
            return fib(n - 2) + fib(n - 1)

    @lru_cache
    def factorialOpt(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)


    start_time = timeit.default_timer()

    temp = factorial(800)
    print("Факториал без оптимизации выполняется за", timeit.default_timer() - start_time, "секунд")

    start_time = timeit.default_timer()

    temp = factorialOpt(800)

    print("Факториал с оптимизацией выполняется за", timeit.default_timer() - start_time, "секунд")

    start_time = timeit.default_timer()

    print(fib(25))
    print("Фиббоначи без оптимизации выполняется за", timeit.default_timer() - start_time, "секунд")

    start_time = timeit.default_timer()

    print(fibOpt(25))
    print("Фиббоначи с оптимизацией выполняется за", timeit.default_timer() - start_time, "секунд")
