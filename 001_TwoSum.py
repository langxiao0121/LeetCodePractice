"""
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    Example:
        Given nums = [2, 7, 11, 15], target = 9

        Because nums[0] + nums[1] = 2 + 7 = 9

        return [0, 1]
"""

class Solution:

    def two_sum(self, given, target):
        # g_num = given_number
        # t_num = target_number

        g_num = given
        t_num = target

        for x, y in enumerate(g_num):
            if t_num - g_num[x] in g_num:
                if g_num.index(t_num - y) != x:
                    return x, g_num.index(t_num - y)