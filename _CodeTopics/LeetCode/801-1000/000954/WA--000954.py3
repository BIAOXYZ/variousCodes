class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:

        if arr.count(0) & 1 or sum(elem < 0 for elem in arr) & 1:
            return False
        arr = filter(lambda x : x != 0, arr)
        arr = map(abs, arr)

        ctr = Counter(arr)
        deleted = defaultdict(int)
        keys = list(ctr.keys())
        keys.sort()
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
https://leetcode-cn.com/submissions/detail/292900128/

101 / 102 个通过测试用例
状态：解答错误

输入：
[-3,-4,2,6]
输出：
true
预期结果：
false
"""
