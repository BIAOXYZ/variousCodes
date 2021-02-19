class Solution(object):
    def minKBitFlips(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """

        length = len(A)
        total = 0
        diffArr = [0 for _ in range(length+1)]
        currReverseNum = 0

        # 其实没有必要每次都把A[i]里的0真的变成1，只要确定它确实可以合法的变成1就行。
        # 所以下面的实现更接近答案的实现，表现之一就是一个for循环，return -1的逻辑是：
        # 只要i+K超过了总长度（此时已经不能再翻转了），但是还有0，那就return -1。
        for i in range(length):
            currReverseNum += diffArr[i]
            if (A[i] + currReverseNum) % 2 == 0:
                if i + K > length:
                    return -1
                total += 1
                diffArr[i+K] -= 1
                currReverseNum += 1
        return total
        
"""
https://leetcode-cn.com/submissions/detail/146945322/

110 / 110 个通过测试用例
状态：通过
执行用时: 740 ms
内存消耗: 14.4 MB

执行用时：740 ms, 在所有 Python 提交中击败了52.92%的用户
内存消耗：14.4 MB, 在所有 Python 提交中击败了71.48%的用户
"""
