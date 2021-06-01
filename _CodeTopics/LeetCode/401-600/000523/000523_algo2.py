class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """

        # 参考答案的方法：对前缀和模k的余数构建哈希表。

        if len(nums) < 2:
            return False
        
        prefixSum = [nums[0]]
        # 刚才错的那个提交其实也想到了第一个元素了，但是不知道怎么鬼使神差的觉得是不用加的。累了，赶紧搞完睡了。
        # 第二次改：这里不能直接用 nums[0]，应该再模下 k。
        dic = {nums[0] % k :[0]}
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])
            remainder = prefixSum[i] % k
            if remainder == 0:
                return True
            else:
                if not dic.has_key(remainder):
                    dic[remainder] = [i]
                # 这次是把else分支重新搞得更清晰些。
                else:
                    dic[remainder].append(i)
                    if len(dic[remainder]) > 2 or abs(dic[remainder][0] - dic[remainder][1]) >= 2:
                        return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/183082490/

94 / 94 个通过测试用例
状态：通过
执行用时: 160 ms
内存消耗: 42.7 MB

执行用时：160 ms, 在所有 Python 提交中击败了19.85%的用户
内存消耗：42.7 MB, 在所有 Python 提交中击败了5.15%的用户
"""
