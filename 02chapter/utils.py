# -*- coding: utf-8 -*-
# @Date:   2022-01-28 23:28:39
# @Last Modified time: 2022-01-28 23:35:20


import random


def checkSort(sort_func):
    # 检查排序算法的正确性
    nums = [random.randint(0, 10000) for _ in range(1000)]
    sort_func(nums)
    for i in range(0, len(nums) - 1):
        if nums[i] > nums[i + 1]:
            print('error.')
            return
    print('right.')
