class MagicDictionary:

    def __init__(self):
        self.lis = []

    def buildDict(self, dictionary: List[str]) -> None:
        for d in dictionary:
            self.lis.append(Counter(d))

    def search(self, searchWord: str) -> bool:

        def compare(ctr1, ctr2):
            tmp = {k:ctr1[k]-ctr2[k] for k in ctr1.keys() | ctr2.keys() if ctr1[k] != ctr2[k]}
            return len(tmp) == 2 and 1 in tmp.values() and -1 in tmp.values()

        ctrW = Counter(searchWord)
        for ctr in self.lis:
            if compare(ctr, ctrW):
                return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)

"""
https://leetcode.cn/submissions/detail/335211127/

74 / 83 个通过测试用例
状态：解答错误

输入：
["MagicDictionary", "buildDict", "search", "search", "search", "search", "search", "search", "search", "search", "search", "search", "search", "search", "search", "search", "search"]
[[], [["a","b","ab","abc","abcabacbababdbadbfaejfoiawfjaojfaojefaowjfoawjfoawj","abcdefghijawefe","aefawoifjowajfowafjeoawjfaow","cba","cas","aaewfawi","babcda","bcd","awefj"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["ab"], ["ba"], ["abc"], ["cba"], ["abb"], ["bb"], ["aa"], ["bbc"], ["abcd"]]
输出：
[null,null,true,true,true,true,true,true,false,false,true,true,true,true,true,true,false]
预期结果：
[null,null,true,true,true,true,true,true,false,false,false,false,true,true,true,true,false]
"""
