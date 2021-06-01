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
        dic = {nums[0]:[0]}
        for i in range(1, len(nums)):
            prefixSum.append(prefixSum[-1] + nums[i])
            remainder = prefixSum[i] % k
            if remainder == 0:
                return True
            else:
                if not dic.has_key(remainder):
                    dic[remainder] = [i]
                else:
                    if len(dic[remainder]) > 1 or abs(dic[remainder][0] - i) >= 2:
                        return True
        return False
        
"""
https://leetcode-cn.com/submissions/detail/183082155/

93 / 94 个通过测试用例
状态：解答错误

最后执行的输入：
[23,0,0]
6
"""
"""
没完了是不？就是因为又困又累，脑子不行了，结果你还来劲了。。。
"""
