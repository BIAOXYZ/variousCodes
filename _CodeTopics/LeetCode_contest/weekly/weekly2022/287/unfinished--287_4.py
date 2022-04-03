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

class Encrypter(object):

    def __init__(self, keys, values, dictionary):
        """
        :type keys: List[str]
        :type values: List[str]
        :type dictionary: List[str]
        """
        self.kv = {keys[i]:values[i] for i in range(len(keys))}
        self.vk = defaultdict(list)
        for i in range(len(keys)):
            vk[values[i]].append(keys[i])
        self.d = Trie()
        for word in dictionary:
            self.d.insert(word)
        
    def encrypt(self, word1):
        """
        :type word1: str
        :rtype: str
        """
        res = []
        for ch in word1:
            res.append(self.kv[ch])
        return ''.join(res)

    def decrypt(self, word2):
        """
        :type word2: str
        :rtype: int
        """
        res = []
        for i in range(0, len(word2), 2):
            cipher = word2[i:i+2]
            plaintexts = self.vk[cipher]
            for plaintext in plaintexts:
                if self.d.startsWith(plaintext):
                    res.append(plaintext)
            if not res:
                return 0


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)
