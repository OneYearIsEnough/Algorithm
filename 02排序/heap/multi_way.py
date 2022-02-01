# -*- coding: utf-8 -*-
# @Date:   2022-01-11 00:16:48
# @Last Modified time: 2022-01-11 00:16:48


"""
基于优先队列的多路归并排序
可以很方便的将多个不同来源的数组进行全局排序
由于这里实现的是最大堆，所有本次排序为从大到小对元素进行排序
"""

from max_heap import MaxHeap


def multiWay(multi_nums):
    mh = MaxHeap()
    for nums in multi_nums:
        for num in nums:
            mh.insert(num)
    # output
    ret = []
    while not mh.isEmpty():
        ret.append(mh.delMax())
    return ret


if __name__ == "__main__":
    import random

    multi_nums = [[random.randint(0, 1000) for _ in range(25)] for _ in range(4)]
    sorted_nums = multiWay(multi_nums)
    print(sorted_nums)
    print(len(sorted_nums))