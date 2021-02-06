class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        flag = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                flag += 1
                if flag > 1:
                    return False
        return True
        
"""
https://leetcode-cn.com/submissions/detail/144276518/

320 / 335 个通过测试用例
状态：解答错误

输入：
[3,4,2,3]
输出：
true
预期：
false
"""
"""
注：可以，这个题是真骚。。。不被骚一下还真不信 --> 因为最开始瞅了一眼，发现虽然是个简单，但是通过率很低：
`通过次数 35,998 提交次数 153,028`，首页显示的通过率是 `23.6%`。
不过其实并没有在意，没有刻意去想corner case，然后果然就中招了。。。可见数据是不会说谎的。。。
"""
