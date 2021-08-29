# -*- coding: utf-8 -*-

def fact(n):
    fact_loop(n, 1)

def fact_loop(num, product):
    if num == 1 :
        print('Result is %d' % (product,))
        return product
    print('fact_loop(%d,%d)' % (num, product))
    return fact_loop(num - 1, num * product)

if __name__ == '__main__' :
    print('call this method from console')
    fact(5)
    