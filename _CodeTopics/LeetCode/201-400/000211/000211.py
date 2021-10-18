####################################################################################################
# 下述内嵌字典树的代码参考了： https://leetcode-cn.com/submissions/detail/95263958/
# 但是有两点不一样：
## 1） .search() 方法要考虑通配符。
## 2） 不需要实现 .startsWith() 方法。
####################################################################################################

class TrieNode(object):
    def __init__(self, value):
        self.val = value
        self.isleaf = False
        self.children = {}

class WordDictionary(object):

    def __init__(self):
        self.root = TrieNode(None)

    def addWord(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for letter in word:
            if not curr.children.has_key(letter):
                curr.children[letter] = TrieNode(letter)
            curr = curr.children[letter]
        curr.isleaf = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        
        def search_from_node(node, subWord):
            curr = node
            for i, letter in enumerate(subWord):
                if letter != '.':
                    if not curr.children.has_key(letter):
                        return False
                    curr = curr.children[letter]
                else:
                    res = False
                    for letter in curr.children.keys():
                        nextNode = curr.children[letter]
                        res = res or search_from_node(nextNode, subWord[i+1:])
                    return res
            return False if not curr.isleaf else True
        
        return search_from_node(self.root, word)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

"""
https://leetcode-cn.com/submissions/detail/230159088/

13 / 13 个通过测试用例
状态：通过
执行用时: 520 ms
内存消耗: 36.4 MB

执行用时：520 ms, 在所有 Python 提交中击败了30.86%的用户
内存消耗：36.4 MB, 在所有 Python 提交中击败了45.68%的用户
"""
