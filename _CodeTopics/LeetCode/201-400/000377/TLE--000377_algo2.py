class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 这个是 `000377.py` 记忆化搜索实现对应的dp实现，但是还是有一丢丢不一样。
        # `000377.py` 里只计数，这里直接把新组成的 tuple 加进去了。
        # 相同点就是都用 set 来控制重复——但是参考官方答案后就知道其实没必要。。。

        basicList = [0 for _ in range(len(nums))]
        basicSet = set()
        basicSet.add(tuple(basicList))
        dp = [basicSet] + [set() for _ in range(target)]

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    for elem in dp[i-num]:
                        newElem = list(elem)
                        newElem.append(num)
                        dp[i].add(tuple(newElem))
        return len(dp[target])
        
"""
https://leetcode-cn.com/submissions/detail/171488006/

8 / 15 个通过测试用例
状态：超出时间限制

最后执行的输入：
[4,2,1]
32
"""
