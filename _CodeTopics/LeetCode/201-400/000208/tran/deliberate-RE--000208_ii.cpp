class TrieNode {
// 这里如果是private，下面 if (curr->children.empty() || curr->children.find(letter) == curr->children.end())
// 就会报错说 error: 'children' is a private member of 'TrieNode'
// 所以这里先改成 public，后面再写一个用 private 成员，但是有public的get()方法的。

// 接上，来了。
private:
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
    void get_children(unordered_map<char, TrieNode*>* chld) {
        chld = &(this->children);
    }
    void get_isleaf(bool* islf) {
        islf = &(this->isleaf);
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
        unordered_map<char, TrieNode*>* childrenDup;
        for (auto letter : word) {            
            curr->get_children(childrenDup);
            if (childrenDup->empty() || childrenDup->find(letter) == childrenDup->end()) {
                (*childrenDup)[letter] = new TrieNode(letter);
            }
            curr = (*childrenDup)[letter];
        }
        bool* isleadDup;
        curr->get_isleaf(isleadDup);
        *isleadDup = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        auto curr = this->root;
        unordered_map<char, TrieNode*>* childrenDup;
        for (auto letter : word) {            
            curr->get_children(childrenDup);
            if (childrenDup->empty() || childrenDup->find(letter) == childrenDup->end()) {
                return false;
            }
            curr = (*childrenDup)[letter];
        }
        bool* isleadDup;
        curr->get_isleaf(isleadDup);
        if (!isleadDup) {
            return false;
        } else {
            return true;
        }
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        auto curr = this->root;
        unordered_map<char, TrieNode*>* childrenDup;
        for (auto letter : prefix) {            
            curr->get_children(childrenDup);
            if (childrenDup->empty() || childrenDup->find(letter) == childrenDup->end()) {
                return false;
            }
            curr = (*childrenDup)[letter];
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
https://leetcode-cn.com/submissions/detail/167615723/

0 / 15 个通过测试用例
状态：执行出错

执行出错信息：
Line 44: Char 30: runtime error: member call on address 0x606000000140 with insufficient space for an object of type 'std::unordered_map<char, TrieNode *, std::hash<char>, std::equal_to<char>, std::allocator<std::pair<const char, TrieNode *>>>' (solution.cpp)
最后执行的输入：
["Trie","insert","search","search","startsWith","insert","search"]
[[],["apple"],["apple"],["app"],["app"],["app"],["app"]]
*/
// 故意写错了，记个`TODO`回头再写了。感觉写得太丑陋了。。。关键还RE。。。
