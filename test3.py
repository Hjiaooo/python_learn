# -*- coding: utf-8 -*-
# __author__ = 'Hjia'

# Python练习题问题如下：
#
# 简述：要求输入某年某月某日
# 提问：求判断输入日期是当年中的第几天？
#Python解题思路分析：
#我们就以3月5日这一天为例。首先把前两个月的加起来，然后再加上5天即本年的第几天。这里有一种特殊的情况，就是闰月，遇到这种情况且输入月份大于2时需考虑多加一天。如果不是很明白，可以看下边的python源码。

# year = int(input('year:\n'))
# month = int(input('month:\n'))
# day = int(input('day:\n'))
#
# months=(0,31,59,90,120,151,181,212,243,273,304,334)
# if 0< month <=12:
#     sum= months[month -1]
# else:
#     print('data error')
# sum += day
# leap=0
# if (year%400 == 0) or ((year %4 ==0) and (year %100 !=0)):#判断是否闰年？
#     leap =1
# if (leap==1) and (month >2):#是闰年且月份大于2时
#     sum +=1
# print('it is the %dth day.' %sum)


#导入datatime模块
import datetime

y = int(input('请输入4位数字的年份：'))  # 获取年份
m = int(input('请输入月份：'))  # 获取月份
d = int(input('请输入是哪一天：'))  # 获取“日”

targetDay = datetime.date(y, m, d)  # 将输入的日期格式化成标准的日期
dayCount = targetDay - datetime.date(targetDay.year - 1, 12, 31)  # 减去上一年最后一天
print(dayCount)
print(dayCount.days)
print('%s是%s年的第%s天。' % (targetDay, y, dayCount.days))