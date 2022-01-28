# -*- coding: utf-8 -*-
# @Date:   2022-01-29 00:21:45
# @Last Modified time: 2022-01-29 00:41:43


"""
自顶向下归并排序，O(nlgn)，需要递归，子问题规模逐渐减小
优点：快，毕竟O(nlgn)
缺点：额外空间复杂度O(n)

可以有两点优化，具体看代码
"""


def mergeSort(nums):
    aux = [0 for _ in range(len(nums))]  # 提前开好空间，后面逻辑比较顺。。。
    _mergeSort(nums, 0, len(nums) - 1, aux)


def _mergeSort(nums, l, r, aux):
    # 左闭右闭
    # 优化点1： 比一定要l<=r，可以r-l<某个值得时候(e.g. 15)，转插入排序（近乎有序数组排序O(n))
    if l >= r:
        return
    m = l + (r - l) // 2
    _mergeSort(nums, l, m, aux)
    _mergeSort(nums, m + 1, r, aux)
    # 优化点2：两个有序数组不能组成一个大的有序数组的时候，再进merge逻辑，进一步优化归并排序算法
    if nums[m] >= nums[m + 1]:
        _merge(nums, l, m, r, aux)


def _merge(nums, l, m, r, aux):
    aux[l: r + 1] = nums[l: r + 1]
    i, j = l, m + 1

    for k in range(l, r + 1):
        if i > m:
            nums[k] = aux[j]
            j += 1
        elif j > r:
            nums[k] = aux[i]
            i += 1
        elif aux[i] <= aux[j]:
            nums[k] = aux[i]
            i += 1
        else:
            nums[k] = aux[j]
            j += 1


if __name__ == "__main__":
    import utils

    utils.checkSort(mergeSort)
