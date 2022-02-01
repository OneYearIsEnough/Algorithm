# -*- coding: utf-8 -*-
# @Date:   2022-01-11 00:16:13
# @Last Modified time: 2022-01-11 00:16:13


"""
最大堆，优先队列的底层数据结构
"""


class MaxHeap:
    def __init__(self):
        # 有效索引从0开始
        # 本质上是索引优先队列
        self._size = 0
        self._data = []

    def _parent(self, idx):
        return (idx - 1) // 2

    def _left_child(self, idx):
        return idx * 2 + 1

    def _right_child(self, idx):
        return (idx + 1) * 2

    def _swap(self, idx1, idx2):
        self._data[idx1], self._data[idx2] = self._data[idx2], self._data[idx1]

    def _shiftDown(self, idx):
        # 下沉操作
        while idx * 2 + 1 < self._size:
            j = idx * 2 + 1
            if j + 1 < self._size and self._data[j + 1] > self._data[j]:
                j += 1
            if self._data[idx] >= self._data[j]:
                break
            self._swap(idx, j)
            idx = j

    def _shiftUp(self, idx):
        # 上浮
        while idx > 0:
            p_idx = self._parent(idx)
            if self._data[p_idx] >= self._data[idx]:
                break
            self._swap(idx, p_idx)
            idx = p_idx

    def isEmpty(self):
        return self._size == 0

    @property
    def size(self):
        return self._size

    def insert(self, item):
        # 插入元素
        self._data.append(item)
        self._shiftUp(self._size)
        self._size += 1

    def delMax(self):
        # 删除最大的元素
        assert not self.isEmpty()
        self._swap(0, self._size - 1)
        ret = self._data.pop()
        # _size一定要在_shiftDown之前维护，因为_shiftDown里面的逻辑用到了更新后的_size
        self._size -= 1  
        self._shiftDown(0)
        return ret

    @property
    def max(self):
        assert not self.isEmpty()
        return self._data[0]

    def contains(self, idx):
        # 是否存在索引为idx的元素
        return idx < self._size

    @property
    def maxIndex(self):
        return self._data[0]

    
if __name__ == "__main__":
    import random
    elems = [random.randint(1, 100) for _ in range(20)]
    print(sorted(elems))
    test = MaxHeap()
    for elem in elems:
        test.insert(elem)
    print(test.max)
    test.delMax()
    test.delMax()
    print(test.max)  # 第三大
    print(test.size)
