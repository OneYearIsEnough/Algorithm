# -*- coding: utf-8 -*-
# @Date:   2022-01-30 00:22:32
# @Last Modified time: 2022-01-30 00:22:32


"""
单路快排，时间复杂度O(nlgn)
应用非常广，因为相比mergeSort来说交换次数更少，另外不需要显式的开辟辅助数组
单路快排的一个缺点就是重复元素很多的时候效率比较低
应用：波兰国旗问题、第k大（小）的问题
"""

import random


def quickSort(nums):

    def _parition(nums, l, r):
        # 左闭右闭
        rnd_idx = random.randint(l, r)
        nums[rnd_idx], nums[l] = nums[l], nums[rnd_idx]
        e = nums[l]  # 随机找一个元素，放到最左侧
        i = l
        for j in range(l + 1, r + 1):
            if nums[j] < e:
                nums[i + 1], nums[j] = nums[j], nums[i + 1]
                i += 1
        nums[l], nums[i] = nums[i], nums[l]
        # 此时i左侧的元素全是小于e的
        return i

    def _quickSort(nums, l, r):
        if l >= r:
            return

        partition_idx = _parition(nums, l, r)
        # 后面排序的时候就不需要在考虑partition_idx位置的元素了
        _quickSort(nums, l, partition_idx - 1)
        _quickSort(nums, partition_idx + 1, r)

    return _quickSort(nums, 0, len(nums) - 1)


if __name__ == "__main__":
    from utils import checkSort

    checkSort(quickSort)