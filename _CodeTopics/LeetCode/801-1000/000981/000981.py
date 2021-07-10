class TimeMap(object):

    # 由于 timestamp 的范围达到了 10^7，所以感觉需要二分查找。不用二分的就不写了。
    # 另外由于二分要求数组有序，所以在插入时想较小代价维持顺序，想到的就是堆——但是感觉这题就偏复杂了。
    # 然后发现条件里说时间戳是严格递增的，所以只需要简单的append就行。

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic1 = {}
        self.dic2 = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if not self.dic1.has_key(key):
            self.dic1[key] = [timestamp]
        else:
            self.dic1[key].append(timestamp)
        # 其实 self.dic2 不用再判断了，因为 self.dic1 和 self.dic2 都是同时操作的。不过从自然的逻辑上还是判断下吧。
        if not self.dic2.has_key(key):
            self.dic2[key] = {timestamp : value}
        else:
            self.dic2[key][timestamp] = value

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """

        def find_left_most_le(target, lis):
            if target < lis[0]:
                return -1
            left, right = 0, len(lis) - 1
            res = lis[left]
            while left <= right:
                # 移位运算符优先级较低，所以还得小括号括一下
                mid = left + ((right - left) >> 1)
                if lis[mid] < target:
                    res = lis[mid]
                    left = mid + 1
                elif lis[mid] > target:
                    right = mid - 1
                else:
                    res = lis[mid]
                    break
            return res

        if not self.dic1.has_key(key):
            return ""
        else:
            mostRecentTime = find_left_most_le(timestamp, self.dic1[key])
            if mostRecentTime == -1:
                return ""
            else:
                return self.dic2[key][mostRecentTime]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

"""
https://leetcode-cn.com/submissions/detail/194165316/

46 / 46 个通过测试用例
状态：通过
执行用时: 1700 ms
内存消耗: 69.3 MB

执行用时：1700 ms, 在所有 Python 提交中击败了9.09%的用户
内存消耗：69.3 MB, 在所有 Python 提交中击败了9.09%的用户
"""
