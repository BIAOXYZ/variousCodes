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

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right+1] - self.prefixSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

"""
https://leetcode-cn.com/submissions/detail/294394102/

7 / 15 个通过测试用例
状态：解答错误

输入：
["NumArray","update","update","update","sumRange","update","sumRange","update","sumRange","sumRange","update"]
[[[7,2,7,2,0]],[4,6],[0,2],[0,9],[4,4],[3,8],[0,4],[4,1],[0,3],[0,4],[0,4]]
输出：
[null,null,null,null,6,null,27,null,21,28,null]
预期结果：
[null,null,null,null,6,null,32,null,26,27,null]
"""
