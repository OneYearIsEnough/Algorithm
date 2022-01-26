# -*- coding: utf-8 -*-
# @Date:   2022-01-27 01:55:27
# @Last Modified time: 2022-01-27 02:05:24


"""
基于链表数据结构实现队列
此时需要头指针和尾指针才能完成全都是O(1)的操作
"""


class Node:
    def __init__(self, _val=-1, _next=None):
        self.val = _val
        self.next = _next


class Queue:
    def __init__(self):
        self.first = None  # 指向最早加入的节点
        self.last = None  # 指向最后加入的节点
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def enqueue(self, item):
        # 队尾
        old_last = self.last
        self.last = Node(item)
        if self.isEmpty():  # 此时last还是None，即old_last是None
            self.first = self.last
        else:
            old_last.next = self.last
        self.size += 1

    def dequeue(self):
        # 队首
        assert not self.isEmpty()
        ret = self.first.val
        next_node = self.first.next
        self.first.next = None
        self.first = next_node
        self.size -= 1
        if self.isEmpty():
            self.last = None
        return ret

    def print(self):
        print('front: ', end='')
        cur = self.first
        while cur:
            print(cur.val, end='->')
            cur = cur.next
        print('last')


if __name__ == "__main__":
    items = [1, 3, 5, 7, 9, 0]
    test = Queue()
    for item in items:
        test.enqueue(item)
    test.print()
    for i in range(6):
        print(test.dequeue())
    test.print()