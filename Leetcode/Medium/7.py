#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time   :  2022/3/17 20:05
# @Author :  Allen
# 整数反转
# 给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
#
# 如果反转后整数超过 32 位的有符号整数的范围 [−2^31, 2^31− 1] ，就返回 0。
#
# 假设环境不允许存储 64 位整数（有符号或无符号）。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/reverse-integer

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = -int(str(x)[::-1][:-1]) if x < 0 else int(str(x)[::-1])
        x = 0 if abs(x) > 2**31-1 else x
        return x


if __name__ == '__main__':
    pass
