# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """

        """
        # 比如我们可以利用两个 Rand7() 相乘，分别可以得到结果如下：
            1	2	3	4	5	6	7
        1	1	2	3	4	5	6	7
        2	2	4	6	8	10	12	14
        3	3	6	9	12	15	18	21
        4	4	8	12	16	20	24	28
        5	5	10	15	20	25	30	35
        6	6	12	18	24	30	36	42
        7	7	14	21	28	35	42	49
        """
        """
        # 我们可以得到每个数生成的概率为:
            1	    2	    3	    4	    5	    6	    7	    8	    9
        P	1/49	2/49	2/49	3/49	2/49	4/49	2/49	2/49	4/49
            10	    12	    14	    15	    16	    18	    20	    21	    24
        P	2/49	1/49	2/49	2/49	2/49	1/49	2/49	2/49	2/49
            25	    28	    30	    35	    36	    42	    49		
        P	1/49	2/49	2/49	2/49	1/49	2/49	1/49	
        """
        
        """
        擦，原来是官方答案概率表算错了：16是1/49。。。其实还有9和12的概率也反了- -
        """

        se = set([2,3,5,7,8,10,14,15,21,20])
        dic = {
            2:1, 3:2, 5:3, 7:4, 8:5, 10:6, 14:7, 15:8, 21:9, 20:10
        }
        while True:
            first, second = rand7(), rand7()
            if first * second not in se:
                continue
            else:
                return dic[first * second]
        
"""
https://leetcode-cn.com/submissions/detail/215603898/

12 / 12 个通过测试用例
状态：通过
执行用时: 560 ms
内存消耗: 17.9 MB

执行用时：560 ms, 在所有 Python 提交中击败了10.35%的用户
内存消耗：17.9 MB, 在所有 Python 提交中击败了62.07%的用户
"""
