# -*- coding: utf-8 -*-
# @Date:   2022-01-25 02:11:12
# @Last Modified time: 2022-01-25 02:14:20


"""
这里的bag其实就是无需集合，即底层数据结构为hash表的set而已
"""
import math


def calu_avg_std(nums):
    n = len(nums)
    _sum = 0
    for num in nums:
        _sum += num
    avg = _sum / n

    _sum = 0
    for num in nums:
        _sum += (num - avg) ** 2
    std = math.sqrt(_sum / (n - 1))

    return avg, std


if __name__ == "__main__":
    nums = [100, 99, 101, 120, 98, 107, 109, 81, 101, 90]
    print(calu_avg_std(nums))