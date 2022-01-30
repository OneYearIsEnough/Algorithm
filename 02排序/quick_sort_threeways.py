# -*- coding: utf-8 -*-
# @Date:   2022-01-30 00:22:44
# @Last Modified time: 2022-01-30 00:22:44


"""
着重解决单路快排对于重复元素较多的排序性能较差的问题
"""

import random


def quickSortThreeWays(nums):

	def _quickSortThreeWays(nums, l, r):
		# 左闭右闭
		# 把partition函数直接写在_quickSortThreeWays函数里面
		if l >= r:
			return

		rnd_idx = random.randint(l, r)
		nums[l], nums[rnd_idx] = nums[rnd_idx], nums[l]
		e = nums[l]

		lt = l  # 右闭
		gt = r + 1  # 左闭
		i = l + 1

		while i < gt:
			if nums[i] < e:
				nums[lt + 1], nums[i] = nums[i], nums[lt + 1]
				lt += 1
				i += 1
			elif e < nums[i]:
				nums[i], nums[gt - 1] = nums[gt - 1], nums[i]
				gt -= 1
			else:
				i += 1

		nums[l], nums[lt] = nums[lt], nums[l]
		_quickSortThreeWays(nums, l, lt - 1)
		_quickSortThreeWays(nums, gt, r)

	_quickSortThreeWays(nums, 0, len(nums) - 1)


if __name__ == "__main__":
	from utils import checkSort

	checkSort(quickSortThreeWays)

