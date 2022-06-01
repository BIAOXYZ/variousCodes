class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        left, right = 0, n-1
        found = False
        res = None

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                found = True
                res = mid
                break
            elif nums[mid] >= nums[0]:
                # if target < nums[mid] and target >= nums[0]:
                # 似乎判断条件和 nums[-1] 比也可以？这里其实有些 subtle 的点可能需要未来看下。
                if target < nums[mid] and target > nums[-1]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[0]:
                # if target > nums[mid] and target <= nums[-1]:
                # 和上面类似的情况，回头再分析下（为什么这样能代替）。
                if target > nums[mid] and target < nums[0]:
                    left = mid + 1
                else:
                    right = mid - 1
        if found:
            print("res is: ", res)
            return res
        else:
            print("res is: ", -1)
            return -1
        
"""
https://leetcode.cn/submissions/detail/320757535/

187 / 195 个通过测试用例
状态：解答错误

输入：
[1,3,5]
1
输出：
-1
stdout
res is:  -1

预期结果：
0
"""
