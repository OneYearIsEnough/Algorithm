# -*- coding: utf-8 -*-
# @Date:   2022-01-28 23:35:27
# @Last Modified time: 2022-01-29 00:12:33


"""
插入排序，O(N^2)
对于近乎有序的数组时间复杂度能干到O(N)
在小规模数组排序中应用非常广泛
"""

def insertionSort(nums):
    for i in range(1, len(nums)):
        e = nums[i]
        j = i
        while j > 0 and nums[j] < nums[j - 1]:
            # 用赋值代替常用的swap，节省一些算法运行时间，而且只用了常数空间
            nums[j - 1] = nums[j]  
            j -= 1
        nums[j] = e


if __name__ == "__main__":
    import utils
    utils.checkSort(insertionSort)
