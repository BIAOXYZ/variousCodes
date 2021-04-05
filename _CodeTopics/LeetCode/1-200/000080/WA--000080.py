class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 不符合题意，因为用了额外的空间。但是先写了再说。

        ctr = collections.Counter(nums)
        print ctr
        res = 0
        for v in ctr.values():
            if v > 2:
                res += 2
            else:
                res += v
        return res
        
"""
https://leetcode-cn.com/submissions/detail/164126491/

34 / 164 个通过测试用例
状态：解答错误

输入：
[1,1,1,2,2,3]
输出：
[1,1,1,2,2]
预期：
[1,1,2,2,3]
"""
"""
说明：

为什么返回数值是整数，但输出的答案是数组呢？

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

====================================================================================================
那你直接返回数组不就完了，在这浪费时间呢。。。
"""
