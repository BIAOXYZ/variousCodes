class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """

        # 解释一下上一版的手动狗头题。。。
        """
        l = [1,2,3]
        num = int(''.join([str(elem) for elem in l]))
        print num, type(num)

        num = 456
        print [int(elem) for elem in list(str(num))]
        --------------------------------------------------
        123 <type 'int'>
        [4, 5, 6]
        """

        def list_to_int(lis):
            return int(''.join([str(elem) for elem in lis]))
        def int_to_list(num):
            return [int(elem) for elem in list(str(num))]

        # 所以上一版这句等价于下面两个函数调用那句。
        # return [int(elem) for elem in list(str( int(''.join([str(elem) for elem in A])) + K ))]
        return int_to_list(list_to_int(A) + K)
        
"""
https://leetcode-cn.com/submissions/detail/140211342/

156 / 156 个通过测试用例
状态：通过
执行用时: 288 ms
内存消耗: 13.7 MB

# 破笔记本卡了，导致排名，百分比那个网页没出来，看不了了。。。
"""
