class Solution(object):
    def maxScoreSightseeingPair(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # 本来上一个算法复杂度控制到了2000*n，但是还是超时了。
        # 看了下答案的思路还是挺巧的，虽说并不太难，但是一般估计也想不到：
        # 核心思想是遍历时候每走过一个A[i] + i，都看一下和当前最大的A[i] + i哪个大，
        # 把最大的更新进去，这样对于一个新的A[j] - j来说，它只管和前面最大的A[i] + i
        # 去配对就行。 

        length = len(A)
        if length == 2:
            return A[0] + A[1] - 1

        currMaxScore = 1
        preMaxPlace = A[0] + 0
        for i in range(1,length):
            currMaxScore = max(currMaxScore, preMaxPlace + A[i] - i)
            preMaxPlace = max(preMaxPlace, A[i] + i)
        return currMaxScore
        
"""
https://leetcode-cn.com/submissions/detail/79810907/

52 / 52 个通过测试用例
状态：通过
执行用时：500 ms
内存消耗：17.5 MB
"""
