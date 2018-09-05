class Solution:

    def two_sum(self, g_num, t_num):
        # g_num = given_number
        # t_num = target_number

        for x, y in enumerate(g_num):
            if t_num - g_num[x] in g_num:
                if g_num.index(t_num - y) != x:
                    return x, g_num.index(t_num - y)
