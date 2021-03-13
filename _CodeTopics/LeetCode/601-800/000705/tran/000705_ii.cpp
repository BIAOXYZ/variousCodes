class MyHashSet {
public:
    set<int> hs;
    /** Initialize your data structure here. */
    MyHashSet() {
        ;
    }
    
    void add(int key) {
        hs.insert(key);
    }
    
    void remove(int key) {
        set<int>::iterator it = hs.find(key);
        if (it != hs.end()) {
            hs.erase(it);
        }
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        return hs.find(key) != hs.end();
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
https://leetcode-cn.com/submissions/detail/154612415/

32 / 32 个通过测试用例
状态：通过
执行用时: 132 ms
内存消耗: 40.7 MB

执行用时：132 ms, 在所有 C++ 提交中击败了60.38%的用户
内存消耗：40.7 MB, 在所有 C++ 提交中击败了60.66%的用户
*/
