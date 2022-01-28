# -*- coding: utf-8 -*-
# @Date:   2022-01-29 00:03:45
# @Last Modified time: 2022-01-29 00:14:07


"""
希尔排序是插入排序的一种改进，复杂度不是很好分析，可以理解成也是O(n^2)的算法

插入排序极端情况下会出现针对每个位置，都会依次向前最终找到第一个交换的位置，此时非常耗时。
希尔排序的思想是先将数组排成h有序，h逐渐递减到1，即最后是一遍插入排序，因为前面h>1的左右操作
会让数组变得近乎有序，此时能大幅节省插排时间。

数组规模越大，希尔排序的收益就越大，速度大幅快于插入排序
"""

def shellSort(nums):
    n = len(nums)
    h = 1
    while h * 3 < n:
        h = 3 * h + 1  # 为什么这么设不是很理解，记住就行，h每次dowsample 3倍

    # h排序 -> 插排，几乎和插排差不多的
    while h >= 1:
        # 要理解i的步长为什么是1，而不是h，因为要对于数组的每一个数，
        # 它都是位于h有序的数组中，所以步长是1
        for i in range(h, n):  
            e = nums[i]
            j = i
            while j >= h and nums[j] < nums[j - h]:
                nums[j - h] = nums[j]
                j -= h
            nums[j] = e
        h //= 3


if __name__ == "__main__":
    import utils

    utils.checkSort(shellSort)