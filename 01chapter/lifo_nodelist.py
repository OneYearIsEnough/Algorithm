# -*- coding: utf-8 -*-
# @Date:   2022-01-27 01:42:50
# @Last Modified time: 2022-01-27 01:50:31


"""
基于链表数据结构实现下压栈，不需要考虑动态扩缩容，有解释器
"""

class Node:
    def __init__(self, _val=-1, _next=None):
        self.val = _val
        self.next = _next


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def push(self, item):
        # 下面的代码就不需要isEmpty来check了，挺好的
        oldfirst = self.head
        self.head = Node(item)
        self.head.next = oldfirst
        self.size += 1

    def pop(self):
        assert not self.isEmpty()
        ret = self.head.val
        next_node = self.head.next
        self.head.next = None
        self.head = next_node
        self.size -= 1
        return ret

    def print(self):
        cur = self.head
        print('top: ', end='')
        while cur:
            print(cur.val, end='->')
            cur = cur.next
        print('bottom')


if __name__ == "__main__":
    items = [1, 3, 5, 7, 9, 0]
    test = Stack()
    for item in items:
        test.push(item)
    test.print()
    for i in range(6):
        test.pop()
    test.print()
