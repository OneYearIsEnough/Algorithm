# -*- coding: utf-8 -*-
# @Date:   2022-01-26 03:15:04
# @Last Modified time: 2022-01-26 03:33:52


"""
基于list实现能够自动扩缩容的下压栈
"""

class ResizingArrayStack:
    def __init__(self):
        self.size = 0
        self.capacity = 10  # 最小的capacity
        self.stack = [None for _ in range(self.capacity)]

    def getRetio(self):
        return self.size / self.capacity

    def resize(self):
        # 7的意义是防止在小size的时候总是进行元素复制
        if self.size < 7:
            pass
        if self.getRetio() <= 0.25:
            self.capacity = max(self.capacity // 2, 10)
        elif self.getRetio() >= 0.75:
            self.capacity *= 2
        new_stack = [self.stack[i] if i < self.size else None for i in range(self.capacity)]
        self.stack = new_stack

    def isEmpty(self):
        return self.size == 0

    def push(self, item):
        self.stack.append(item)
        self.size += 1
        self.resize()

    def pop(self):
        assert not self.isEmpty()
        ret = self.stack.pop()
        self.size -= 1
        self.resize()
        return ret


if __name__ == "__main__":
    import random
    test = ResizingArrayStack()
    elems = [random.randint(10, 100) for _ in range(200)]
    for elem in elems:
        test.push(elem)
    print(test.capacity)
    for i in range(197):
        test.pop()
    print(test.capacity)
