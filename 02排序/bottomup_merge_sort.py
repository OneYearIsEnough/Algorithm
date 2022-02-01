# -*- coding: utf-8 -*-
# @Date:   2022-01-29 00:41:56
# @Last Modified time: 2022-01-29 00:55:33


"""
topdown形式mergesort的迭代版本，采用区域逐渐扩张的方式完成整个排序操作。
时间复杂度：O(nlgn)
"""


def bottomupMergeSort(nums):

	def _merge(nums, l, m, r):
		# 左闭右闭
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

	n = len(nums)
	aux = [-1 for _ in range(n)]
	sz = 1
	while sz < n:
		i = 0
		while i < n - sz:
			_merge(nums, i, i + sz - 1, min(i + 2 * sz - 1, n - 1))
			i += 2 * sz
		sz += sz


if __name__ == "__main__":
	from utils import checkSort

	checkSort(bottomupMergeSort)


