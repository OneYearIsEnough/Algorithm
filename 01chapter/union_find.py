# -*- coding: utf-8 -*-
# @Date:   2022-01-27 02:10:23
# @Last Modified time: 2022-01-27 02:35:07


"""
并查集的原始以及集中优化版本
需要实现的api: union, find, connected, count(连通分量的数量)
"""

from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    ids = []
    count = 0

    def check(self, p):
        assert 0 <= p < len(self.ids)

    @abstractmethod
    def getCount():
        pass

    @abstractmethod
    def find(self, p):
        pass 

    @abstractmethod
    def union(self, p, q):
        pass

    def print(self):
        print("count: ", self.count)
        print(self.ids)


class quickFind(Base):
    def __init__(self, n: int):
        self.count = n
        self.ids = [i for i in range(self.count)]  # 独立成簇

    def getCount(self):
        return self.count

    def find(p):
        # O(1)
        self.check(p)
        return self.ids[p]  # 直接找父节点，树的层数始终为1

    def union(self, p, q):
        # O(n)
        self.check(p)
        self.check(q)
        if self.ids[p] == self.ids[q]:
            return
        # p_val -> q_val
        p_val = self.ids[p]
        for i in range(len(self.ids)):
            if self.ids[i] == p_val:
                self.ids[i] = self.ids[q]
        self.count -= 1


if __name__ == "__main__":
    n = 10
    test1 = quickFind(n)
    test1.union(5, 9)
    test1.print()
    test1.union(9, 2)
    test1.print()
