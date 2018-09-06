# -*- coding: utf-8 -*-
# __author__ = 'Hjia'

#题目：输入三个整数x,y,z，请把这三个数由小到大输出。

#程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

#解法参考一：
# l = []
# for i in range(3):
#     x = int(input('请分别输入三个整数x,y,z:'))
#     l.append(x)
#     l.sort()
#     print(l)

#解法参考二：

D = input('请连续输入三个整型x,y,z，格式以，分割：')
li =D.split(',')
li1= [int(i) for i in li]
li1.sort()
print(li1)