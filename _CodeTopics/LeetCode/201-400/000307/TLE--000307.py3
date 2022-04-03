class NumArray:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.nums = nums
        self.prefixSum = [0]
        for num in nums:
            self.prefixSum.append(self.prefixSum[-1] + num)

    def update(self, index: int, val: int) -> None:
        for i in range(index+1, self.n+1):
            self.prefixSum[i] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right+1] - self.prefixSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

"""
https://leetcode-cn.com/submissions/detail/294394941/

9 / 15 个通过测试用例
状态：超出时间限制
"""
