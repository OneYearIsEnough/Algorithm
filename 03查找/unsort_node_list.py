# -*- coding: utf-8 -*-
# @Date:   2022-02-02 00:03:12
# @Last Modified time: 2022-02-02 00:03:12


"""
基于无序链表的查找，效率较低
236页
"""


class Node:
    def __init__(self, _key, _val, _next=None):
        self.key = _key
        self.val = _val
        self.next = _next


class SequentialSearchST:
    def __init__(self):
        self.head = None
        self._size = 0

    def contains(self, item):
        return self.get(item) != None

    @property
    def size(self):
        return self._size

    def get(self, _key):
        cur = self.head
        while cur is not None:
            if cur.key == _key:
                return cur.val
            cur = cur.next
        return None

    def put(self, _key, _val):
        cur = self.head
        while cur is not None:
            if cur.key == _key:
                cur.val = _val
                return
            cur = cur.next
        self.head = Node(_key, _val, self.head)  # 头插
        self._size += 1

    def delete(self, _key):
        cur = self.head
        ret = None
        if not self.head:
            return ret
        elif cur and cur.key == _key:
            ret = cur.val
            new_head = cur.next
            cur.next = None
            self.head = new_head
        else:
            while cur.next is not None and cur.next.key != _key:
                cur = cur.next
            if not cur.next:
                return None
            del_node = cur.next
            ret = del_node.val
            cur.next = del_node.next
            del_node.next = None
        self._size -= 1
        return ret



if __name__ == "__main__":
    from utils import checkFind

    test = SequentialSearchST()
    checkFind(test)