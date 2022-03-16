class Trie(object):
    def __init__(self):
        self.children = [None] * 26
        self.isLeaf = False
    
    def insert(self, word):
        curr = self
        for ch in word:
            ind = ord(ch) - ord('a')
            if not curr.children[ind]:
                curr.children[ind] = Trie()
            curr = curr.children[ind]
        curr.isLeaf = True
    
    def search(self, word):
        curr = self
        for ch in word:
            ind = ord(ch) - ord('a')
            if not curr.children[ind]:
                return False
            curr = curr.children[ind]
        return True if curr.isLeaf else False


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        res = ''
        for word in words:
            if all(trie.search(word[0:i]) for i in range(1, len(word)+1)):
                if len(word) > len(res) or (len(word) == len(res) and word < res):
                    res = word
        return res
        
"""
https://leetcode-cn.com/submissions/detail/284464942/

执行用时：988 ms, 在所有 Python3 提交中击败了6.04%的用户
内存消耗：16.7 MB, 在所有 Python3 提交中击败了5.10%的用户
通过测试用例：
59 / 59
"""
