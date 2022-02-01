# -*- coding: utf-8 -*-
# @Date:   2022-01-11 00:17:17
# @Last Modified time: 2022-01-11 00:17:17


"""
堆排序
此时需要借助大顶堆的shiftdown来实现，还是不叫简单的，注意区间即可
"""

def heapSort(nums):

    def _shiftdown(i, length):
        """
        Params:
            i：当前的索引
            length：数组长度
        """
        while i * 2 + 1 < length:
            j = i * 2 + 1
            if j + 1 < length and nums[j + 1] > nums[j]:
                j += 1
            if nums[j] <= nums[i]:
                break
            nums[j], nums[i] = nums[i], nums[j]
            i = j

    n = len(nums)
    # 最后一个节点的父节点是起始节点，因为单一节点不许要考虑，会被_shiftDown自动维护掉
    start_idx = (n - 1 - 1) // 2
    for i in range(start_idx, -1, -1):
        _shiftdown(i, n)
    while n > 0:
        nums[0], nums[n - 1] = nums[n - 1], nums[0]  
        _shiftdown(0, n - 1)  # 每次排好一个就需要将排好的拿掉不考虑了，所以n-1
        n -= 1


if __name__ == "__main__":
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


    checkSort(heapSort)
