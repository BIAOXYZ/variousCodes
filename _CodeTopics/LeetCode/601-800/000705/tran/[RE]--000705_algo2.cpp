// 没看出来怎么内存错误了（就是模仿答案来的，除了里层用vector替换了list），先提交一下记着吧。。。
class MyHashSet {
private:
    int modulus = 769;
    vector<vector<int>> hs;

    int has_value(int key) {
        return key % modulus;
    }
public:
    /** Initialize your data structure here. */
    MyHashSet(): hs(modulus) {}
    
    void add(int key) {
        int h = has_value(key);
        for (auto it = hs[h].begin(); it != hs[h].end(); ++it) {
            if ((*it) == key) {
                return;
            }
        }
        hs[h].push_back(key);
    }
    
    void remove(int key) {
        int h = has_value(key);
        for (vector<int>::iterator it = hs[h].begin(); it != hs[h].end(); ++it) {
            if ((*it) == key) {
                hs[h].erase(it);
            }
        }
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        int h = has_value(key);
        for (auto hashKey : hs[h]) {
            if (hashKey == key) {
                return true;
            }
        }
        return false;
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */

/*
https://leetcode-cn.com/submissions/detail/154653898/

0 / 32 个通过测试用例
状态：执行出错

执行出错信息：
AddressSanitizer: heap-buffer-overflow on address 0x602000000094 at pc 0x000000350ed2 bp 0x7fffdf0c8b90 sp 0x7fffdf0c8b88
最后执行的输入：
["MyHashSet","add","add","contains","contains","add","contains","remove","contains"]
[[],[1],[2],[1],[3],[2],[2],[2],[2]]
*/
