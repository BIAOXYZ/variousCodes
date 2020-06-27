class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def loopAndDelete(l):
            length = len(l)
            for i in range(length-1,-1,-1):
                if l[i] <= 0 or l[i] >= length + 1:
                    l.pop(i)

        # 该算法其实是看到官方答案里这张图偶然想到的：
        # https://assets.leetcode-cn.com/solution-static/41/41_fig1.png
        # 但是其实不满足时间复杂度为O(n)，只是确实也比较巧妙，就记一下：
        """
        核心思想是每次都把不在[1,length]范围的数删除掉，直到把整个nums数组都删空；
        或者完全删不动了为止。
        1. nums都被删空，说明肯定没有1，所以此时应返回1。
        2. 删不动了，比如[1,2,3,4]，此时应返回当前的length加上1。
        """
        # 不去重的话对于输入[1,1]会返回3，而正确的结果应该是2。。。
        nums = set(nums)
        nums = list(nums)

        while len(nums) > 0:
            currlength = len(nums)
            loopAndDelete(nums)
            # 如果经过loopAndDelete函数后一个元素都没少，说明已经删不动了。
            if currlength == len(nums):
                return currlength + 1
        return 1
        
"""
https://leetcode-cn.com/submissions/detail/82487799/

165 / 165 个通过测试用例
状态：通过
执行用时：12 ms
内存消耗：12.6 MB
"""
"""
# 我就感觉这个算法应该很快，尽管理论上复杂度应该是O(N^2)——因为最坏情况一轮只能删除一个元素。
## 这就是理论和实际的差距啊。。。
# 而且实际上这个是写起来最简洁的，当然，前提是已经适应了循环中删除。

执行用时：12 ms, 在所有 Python 提交中击败了98.25%的用户
内存消耗：12.6 MB, 在所有 Python 提交中击败了16.67%的用户
"""
