class TrieNode(object):
    def __init__(self, value):
        self.val = value
        self.isleaf = False
        self.children = {}

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
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
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for letter in word:
            if not curr.children.has_key(letter):
                return False
            curr = curr.children[letter]
        return False if not curr.isleaf else True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for letter in prefix:
            if not curr.children.has_key(letter):
                return False
            curr = curr.children[letter]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

"""
https://leetcode-cn.com/submissions/detail/95263958/

15 / 15 个通过测试用例
状态：通过
执行用时：368 ms
内存消耗：39.1 MB
"""
"""
执行用时：368 ms, 在所有 Python 提交中击败了53.45%的用户
内存消耗：39.1 MB, 在所有 Python 提交中击败了63.64%的用户
"""
