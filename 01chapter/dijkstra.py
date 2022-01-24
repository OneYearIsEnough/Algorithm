# -*- coding: utf-8 -*-
# @Date:   2022-01-25 02:18:13
# @Last Modified time: 2022-01-25 02:32:33


"""
双栈的应用：求带括号的算术表达式的值，支持+-*/sqrt()
求解前提条件：不能省略任何括号，即不能依赖运算符的优先级
另外本算法没有检验算式的合法性
"""

from typing import List
import math


def dijkstraFunc(s: List[str]) -> int:
    vals = []
    ops = []
    for _s in s:
        if _s == '(':
            continue
        if _s in {'+', '-', '*', '/', 'sqrt'}:
            ops.append(_s)
        elif _s == ')':
            val = vals.pop()
            op = ops.pop()
            num = 0
            if op == '+':
                num = vals.pop() + val
            elif op == '-':
                num = vals.pop() - val  # 注意顺序
            elif op == '*':
                num = vals.pop() * val
            elif op == '/':
                num = vals.pop() / val
            elif op == 'sqrt':
                num = math.sqrt(val)
            vals.append(num)
        else:
            vals.append(float(_s))
    return vals[0]


if __name__ == "__main__":
    s = '( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )'.split(' ')
    print(dijkstraFunc(s))
    s = '( ( 1 + sqrt ( 5.0 ) ) / 2.0 )'.split(' ')
    print(dijkstraFunc(s))