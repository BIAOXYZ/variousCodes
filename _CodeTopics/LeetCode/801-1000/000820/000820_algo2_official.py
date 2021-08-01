class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        # 字典树实现，官方 Python3 版本的答案

        words = list(set(words)) #remove duplicates
        #Trie is a nested dictionary with nodes created when fetched entries are missing
        Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()

        #reduce(..., S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
        nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]

        #Add word to the answer if it's node has no neighbors
        return sum(len(word) + 1
            for i, word in enumerate(words)
            if len(nodes[i]) == 0)
        
"""
https://leetcode-cn.com/submissions/detail/202129908/

36 / 36 个通过测试用例
状态：通过
执行用时: 100 ms
内存消耗: 15.6 MB

执行用时：100 ms, 在所有 Python 提交中击败了48.65%的用户
内存消耗：15.6 MB, 在所有 Python 提交中击败了21.62%的用户
"""
