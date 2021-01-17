class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        # 回溯应该可以但是估计很慢会超时，比较保险的做法应该是排序后二分。
        # 由于四个数均不相等，故假定大小关系为 a < c < d < b。另外直接把它们当index用了。
        """
        
        # nums = list(set(nums)) --> 这句没必要了，因为条件里说了所有元素互不相同。。。
        nums.sort()
        length = len(nums)
        if length <= 3:
            return 0
        
        a, b = 0, length - 1
        c, d = 1, length - 2
        res = []
        
        def test_res(a, b, c, d):
            # while a <= length - 4 and c <= length - 3 and d >= 2 and b >= 3:
            #     if a >= c:
            #         c += 1; continue
            #     if c >= d:
            #         return
            #     if d >= b:
            #         d -= 1; continue
            if not (a < c < d < b):
                return
            if nums[a] * nums[b] == nums[c] * nums[d]:
                res.append(1)
                test_res(a+1, b, c+1, d)
                test_res(a, b-1, c, d-1)
            elif nums[a] * nums[b] < nums[c] * nums[d]:
                test_res(a+1, b, c, d)
                test_res(a, b, c, d-1)
            else:
                test_res(a, b, c+1, d)
                test_res(a, b-1, c, d)
        
        test_res(a, b, c, d)
        return len(res) * 8
    
"""
https://leetcode-cn.com/submissions/detail/139021219/

8 / 37 个通过测试用例
状态：解答错误

输入：
[2,3,4,6,8,12]
输出：
24
预期：
40
"""
