class MagicDictionary:

    def __init__(self):
        self.lis = []

    def buildDict(self, dictionary: List[str]) -> None:
        self.lis = dictionary

    def search(self, searchWord: str) -> bool:

        def compare(w1, w2):
            n1, n2 = len(w1), len(w2)
            if n1 != n2:
                return False
            flag = 0
            for i in range(n1):
                if w1[i] != w2[i]:
                    flag += 1
                    if flag > 1:
                        return False
            return True if flag == 1 else False

        for w in self.lis:
            if compare(w, searchWord):
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

"""
https://leetcode.cn/submissions/detail/335622430/

执行用时：
84 ms
, 在所有 Python3 提交中击败了
80.32%
的用户
内存消耗：
15.3 MB
, 在所有 Python3 提交中击败了
92.02%
的用户
通过测试用例：
83 / 83
"""
