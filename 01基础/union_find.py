# -*- coding: utf-8 -*-
# @Date:   2022-01-27 02:10:23
# @Last Modified time: 2022-01-27 13:35:47


"""
并查集的原始以及优化版本
需要实现的api: union, find, connected, count(连通分量的数量)
"""

from abc import ABCMeta, abstractmethod


class Base(metaclass=ABCMeta):
    ids = []
    count = 0

    def check(self, p):
        assert 0 <= p < len(self.ids)

    def getCount():
        return self.count

    @abstractmethod
    def find(self, p):
        pass 

    @abstractmethod
    def isConnected(self, p, q):
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

    def find(p):
        # O(1)
        self.check(p)
        return self.ids[p]  # 直接找父节点，树的层数始终为1

    def isConnected(self, p, q):
        self.check(p)
        self.check(q)
        return self.ids[p] == self.ids[q]

    def union(self, p, q):
        # O(n)
        self.check(p)
        self.check(q)
        if self.isConnected():
            return
        # p_val -> q_val
        p_val = self.ids[p]
        for i in range(len(self.ids)):
            if self.ids[i] == p_val:
                self.ids[i] = self.ids[q]
        self.count -= 1


class quickUnion(Base):
    def __init__(self, n: int):
        """优化了union，但是也只是一个过度版本，性能有时还不如quickFind"""
        self.count = n
        self.ids = [i for i in range(n)]
        self.sz = [1 for _ in range(n)]

    def find(p):
        # 找到根节点，O(n)
        self.check(p)
        while self.ids[p] != p:
            p = self.ids[p]
        return p

    def isConnected(self, p, q):
        self.check(p)
        self.check(q)
        return self.find(p) == self.find(q)

    def union(self, p, q):
        # O(n)
        self.check(p)
        self.check(q)

        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        # 哪个树的个数少就是被merge的对象，即少的合到多的上，让后面操作的代价尽可能的小
        if self.sz[p_root] <= self.sz[q_root]:
            self.ids[p_root] = q_root  # p->q
            self.sz[q_root] += self.sz[p_root]  # q树元素变多了，因此需要更新
        else:
            self.ids[q_root] = p_root  # q->p
            self.sz[p_root] += self.sz[q_root]
        self.count -= 1


class quickUnionPress(Base):
    def __init__(self, n: int):
        # 带路径压缩的加权quick_union，是最优的算法了
        self.count = n
        self.ids = [i for i in range(self.count)]
        # rank可以反映树高，也是一个优化
        self.rank = [1 for _ in range(self.count)]

    def find(p):
        # find的时候要做路径压缩
        self.check(p)
        while self.ids[p] != p:
            # 更改了树的结构，树的深度变浅，将自己的父亲节点设成当前节点的爷爷节点，
            # 根节点也没事，因为根节点是指向自己的
            self.ids[p] = self.ids[self.ids[p]]  
            p = self.ids[p]
        return p

    def isConnected(self, p, q):
        self.check(p)
        self.check(q)
        return self.find(p) == self.find(q)

    def union(self, p, q):
        self.check(p)
        self.check(q)

        p_root = self.find(p)
        q_root = self.find(q)
        if p_root == q_root:
            return
        # rank不变，因为q的rank比p高，整体上树高可以认为是没有变化
        if self.rank[p_root] < self.rank[q_root]:  
            self.ids[p_root] = q_root
        elif self.rank[q_root] < self.rank[p_root]:
            self.ids[q_root] = p_root
        # 此时两棵树的”树高“相同，需要维护rank了。谁merge谁都无所谓，
        # 但是会导致rank维护上差异，即被merge的位置上的rank值需要维护 
        else:  
            self.ids[p_root] = q_root;
            self.rank[q_root] += 1


if __name__ == "__main__":
    items = [i for i in range(10)]
    test1 = quickFind(items)
    test2 = quickUnion(items)
    test3 = quickUnionPress(items)
