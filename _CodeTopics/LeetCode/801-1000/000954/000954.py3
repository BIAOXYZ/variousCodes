class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:

        if arr.count(0) & 1:
            return False

        ctr = Counter(arr)
        deleted = defaultdict(int)
        keys = list(ctr.keys())
        # 上一个提交无法处理 [-3,-4,2,6] 这个用例，因为全部转成正数后这个用例就合法了
        # 但实际上应该是负数和负数去匹配才对。所以按照答案的技巧：按数的绝对值去sort。
        keys.sort(key=abs)
        for key in keys:
            # 说明 key 已经做为 pair 中较大的那个，被之前更小的匹配完了，所以直接跳过。
            # 比如，[2,4,6,12] 中的 4 和 12 都是这种情况。
            if ctr[key] == deleted[key]:
                continue
            doubleKey = 2 * key
            # 对于 [2,4,4,8]，当 for 循环到 4 时，此时可用的 4 的数目应该是一个，因为
            # 虽然一共有两个 4，但是已经有一个和前面的 2 匹配用掉了。
            numOfKeyLeft = ctr[key] - deleted[key]
            if ctr[doubleKey] < numOfKeyLeft:
                return False
            else:
                deleted[doubleKey] += numOfKeyLeft
        return True
        
"""
https://leetcode-cn.com/submissions/detail/292901643/

执行用时：
68 ms
, 在所有 Python3 提交中击败了
99.30%
的用户
内存消耗：
16.8 MB
, 在所有 Python3 提交中击败了
80.42%
的用户
通过测试用例：
102 / 102
"""
