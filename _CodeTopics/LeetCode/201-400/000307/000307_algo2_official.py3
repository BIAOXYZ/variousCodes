class NumArray:

    # 基本类似官方答案的分块法，这个感觉没见过也不好想出来。。。
    
    def __init__(self, nums: List[int]):
        n = len(nums)
        blockSize = int(n**0.5)
        sums = [0] * ((n + blockSize - 1) // blockSize)  # 除完向上取整的常用技巧
        for i, num in enumerate(nums):
            sums[i // blockSize] += num
        self.nums = nums
        self.sums = sums
        self.blockSize = blockSize

    def update(self, index: int, val: int) -> None:
        self.sums[index // self.blockSize] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        b1, b2 = left // self.blockSize, right // self.blockSize
        if b1 == b2:
            return sum(self.nums[left : right+1])
        else:
            # 比如，假定 blockSize 为 5，那么第二个块的末尾的 index 是 9，
            # 所以这里 self.blockSize * (b1 + 1) 已经是一个开的区间了，如果再加 1 反而错了。
            leftSummation = sum(self.nums[left : self.blockSize * (b1 + 1)])
            # 这里用的是 self.sums，不是 self.nums。
            midSummation = sum(self.sums[b1 + 1 : b2])
            rightSummation = sum(self.nums[self.blockSize * b2 : right + 1])
            return leftSummation + midSummation + rightSummation


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

"""
https://leetcode-cn.com/submissions/detail/294407085/

执行用时：780 ms, 在所有 Python3 提交中击败了94.47%的用户
内存消耗：30.5 MB, 在所有 Python3 提交中击败了59.13%的用户
通过测试用例：
15 / 15
"""
