class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        prefixMultiple = ["placeholder", 1]
        for i in range(2, n):
            prefixMultiple.append(prefixMultiple[-1] * i)

        def add_reversed_numbers_to_list(arr, n):
            for i in range(n, 0, -1):
                if n not in arr:
                    arr.append(n)

        def calculate_ith_number(i, left, arr):
            #print "i is %d, left is %d, arr is %s" % (i, left, arr)
            if i == 1:
                arr.append(left)
                return arr
            num, left = left / prefixMultiple[i-1], left % prefixMultiple[i-1]
            if left != 0:
                tmpnum = (num + 1) % n
                while tmpnum in arr:
                    tmpnum = (tmpnum + 1) % n
                arr.append(tmpnum)
                calculate_ith_number(i - 1, left, arr)
            else:
                arr.append(num)
                add_reversed_numbers_to_list(arr, n)
                return arr
            return arr
        
        res = calculate_ith_number(n, k, [])
        return ''.join('%s' % id for id in res)
        
"""
https://leetcode-cn.com/submissions/detail/105460746/

6 / 200 个通过测试用例
状态：解答错误

输入：3
     1
输出："113"
预期："123"
"""
