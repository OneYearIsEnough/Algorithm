# -*- coding: utf-8 -*-
# @Date:   2022-02-02 00:03:12
# @Last Modified time: 2022-02-02 00:03:12


def checkFind(find_class):
    nums = [(i, i + 1) for i in range(100)]
    for num in nums:
        find_class.put(*num)
    print(find_class.size)
    print(find_class.contains(30))
    print(find_class.contains(100))
    print(find_class.delete(99))
    print(find_class.delete(10))
    print(find_class.delete(0))
    print(find_class.delete(110))
    print(find_class.size)