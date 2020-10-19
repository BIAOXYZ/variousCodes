class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        """
        # 1.每次所有数都右移一位，一共做k次的暴力法，超时。
        # 2.使用额外数组的办法空间复杂度O(n)不符合，我根本就没试。答案里好多人用这种的改进版，空间
        #   复杂度是O(k)，其实也不对。
        # 3.环状替换，如果有公约数形成封闭小组，就在小组内环状替换完后跳到下一个小组——这个尼玛还给我
        #   TLE我就真是服了。。。python在效率上没人权。

        # 于是本次用三次翻转法。再超时就sun了狗了。
        """

        length = len(nums)
        if k >= length:
            k = k % length    
        if k == 0 or length == 1:
            return nums

        def reverseList(l):
            length = len(l)
            if length == 1:
                return l
            else:
                # 不需要区分length是奇数还是偶数，因为：
                # length等于4时，相当于[0][3]互换，[1][2]互换。
                # length等于5时，相当于[0][4]互换，[1][3]互换，虽然下标是[2]的元素没有动，
                #   但是它本来也不需要动。
                for i in range(length/2):
                    l[i], l[length-1-i] = l[length-1-i], l[i]
            return l
        
        # 第一次整体翻转
        reverseList(nums)
        print nums
        # 第二次翻转前k个元素
        nums[:k] = reverseList(nums[:k])
        print nums
        # 最后翻转后length-k个元素
        nums[k:] = reverseList(nums[k:])
        print nums
        return nums
        
"""
# https://leetcode-cn.com/submissions/detail/73261291/

35 / 35 个通过测试用例
状态：通过
执行用时：56 ms
内存消耗：13.6 MB
"""
