class TrieNode {
// 这里如果是private，下面 if (curr->children.empty() || curr->children.find(letter) == curr->children.end())
// 就会报错说 error: 'children' is a private member of 'TrieNode'
// 所以这里先改成 public，后面再写一个用 private 成员，但是有public的get()方法的。
public:
    char val;
    bool isleaf;
    unordered_map<char, TrieNode*> children;
public:
    TrieNode () {
        this->isleaf = false;
        children = {};
    }
    TrieNode (char value) {
        this->val = value;
        this->isleaf = false;
        children = {};
    }
};

class Trie {
private:
    TrieNode* root;
public:
    /** Initialize your data structure here. */
    Trie() {
        this->root = new TrieNode();
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        auto curr = this->root;
        for (auto letter : word) {
            // 这里python的写法可以不用判断map是否为空，但是C++的不能省。。。
            if (curr->children.empty() || curr->children.find(letter) == curr->children.end()) {
                curr->children[letter] = new TrieNode(letter);
            }
            curr = curr->children[letter];
        }
        curr->isleaf = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        auto curr = this->root;
        for (auto letter : word) {
            if (curr->children.empty() || curr->children.find(letter) == curr->children.end()) {
                return false;
            }
            curr = curr->children[letter];
        }
        if (!curr->isleaf) {
            return false;
        } else {
            return true;
        }
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        auto curr = this->root;
        for (auto letter : prefix) {
            if (curr->children.empty() || curr->children.find(letter) == curr->children.end()) {
                return false;
            }
            curr = curr->children[letter];
        }
        return true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */

/*
https://leetcode-cn.com/submissions/detail/167614468/

15 / 15 个通过测试用例
状态：通过
执行用时: 100 ms
内存消耗: 42 MB

执行用时：100 ms, 在所有 C++ 提交中击败了21.77%的用户
内存消耗：42 MB, 在所有 C++ 提交中击败了88.50%的用户
*/
