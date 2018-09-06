# -*- coding: utf-8 -*-
# __author__ = 'Hjia'

# 题目：斐波那契数列。
# 程序分析：斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
# 在数学上，费波那契数列是以递归的方法来定义：
# F0 = 0     (n=0)
# F1 = 1    (n=1)
# Fn = F[n-1]+ F[n-2](n=>2)

# 使用递归
     #PS:递归有很多重复计算，比方说你计算f(5)时要去计算f(4)和f(3)，
     #而计算f(4)时又要去计算f(3)，这样f(3)就重复计算了
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

print(fib(10))

# for a in range(fib(10)):
#     print(a)
#
# print()
