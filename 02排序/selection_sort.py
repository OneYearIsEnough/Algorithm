# -*- coding: utf-8 -*-
# @Date:   2022-01-27 13:50:40
# @Last Modified time: 2022-01-29 00:12:42


"""
选择排序：每次确定最小的元素
O(n^2)
特点：虽说是O(n^2)的复杂度，但是他是移动元素次数最少的排序算法，固定移动n次（n=数组长度）
      其他排序算法没有这个性质
"""

def selectionSort(nums):
    n = len(nums)
    for i in range(n):
        _min_idx = i
        for j in range(i + 1, n):
            if nums[j] < nums[_min_idx]:
                _min_idx = j
        nums[_min_idx], nums[i] = nums[i], nums[_min_idx]


if __name__ == "__main__":
    import utils
    utils.checkSort(selectionSort)
