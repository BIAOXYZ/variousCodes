class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        """
        # 以输入 [7,8,9,10,11,12,0,1,2,3,4,5,6] 为例，我们把输入划分成
        ## 左半部分 leftpart = [7,8,9,10,11,12] 和右半部分 rightpart = [0,1,2,3,4,5,6]。
        ## 注意：旋转点（比如这里是 7）包含在左半部分。
        
        # 每次计算完新的 mid 后，先看 nums[mid] 是在左半部分还是在右半部分，然后根据想要的移动情况
        ## 来想象 target 应该满足什么样的大小关系，才能这样（右边界向左 或 左边界向右）移动。
        
        # 标准的二分查找，其实就是让 mid 划分成两半，然后根据 target 和 nums[mid] 的大小关系决定移动方向。
        ## 在这个场景，nums[mid] 不论是在上面提到的 leftpart，还是在 rightpart，一般来说，
        ## **都会有三个区间，但是有两个区间的移动方向是一致的**，所以会合并到一个 if 分支里，具体例子如下：
        
        ## 假定 nums[mid] 为 10，那么这三个区间分别是 [7,8,9]、[11,12]、[0,1,2,3,4,5,6]，其中
        ## target 在 [7,8,9] 的话下一步应该左移，target 在 [11,12] 或 [0,1,2,3,4,5,6] 的话应该右移。
        ## 类似的，也可以举个 nums[mid] 在右半部分的例子：
        ## 假定 nums[mid] 为 3，那么这三个区间分别是 [4,5,6]、[0,1,2]、[7,8,9,10,11,12]，其中
        ## target 在 [4,5,6] 的话下一步应该右移，target 在 [0,1,2] 或 [7,8,9,10,11,12] 的话应该左移。
        """

        n = len(nums)
        left, right = 0, n-1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            # 此时 nums[mid] >= 7，也就是 mid 位于左半部分，也就是在 [7,8,9,10,11,12] 中。
            elif nums[mid] >= nums[0]:
                # 如果 target 比 mid 小（比如假定 mid 上的值是 10，target 为 8），
                # 且又不致于特别小到跑出左半部分了（比如 target 不能是 0 到 6 之间的值），
                # 那么此时应该是把右边界往左移。
                if nums[mid] > target >= nums[0]:
                    right = mid - 1
                # 有了上面的思想，对照着完整版的输入 [7,8,9,10,11,12,0,1,2,3,4,5,6] 看，
                # 于是左边界往右移的条件（注意，不像上面的分支，这俩条件是或的关系）也很明显了：
                # 1. target 是 10 或 11，也就是 target > nums[mid]。
                # 2. target 在 0 到 6 之间，也就是 target < nums[0]。
                elif target > nums[mid] or target < nums[0]:
                    left = mid + 1
            # 此时 nums[mid] < 7，也就是 mid 位于右半部分，也就是在 [0,1,2,3,4,5,6] 中。
            elif nums[mid] < nums[0]:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                elif target < nums[mid] or target > nums[-1]:
                    right = mid - 1
        return -1
        
"""
https://leetcode.cn/submissions/detail/320749510/

执行用时：
40 ms
, 在所有 Python3 提交中击败了
45.83%
的用户
内存消耗：
15.1 MB
, 在所有 Python3 提交中击败了
83.47%
的用户
通过测试用例：
195 / 195
"""
