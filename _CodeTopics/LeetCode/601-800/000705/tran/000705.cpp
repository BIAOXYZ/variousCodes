class MyHashSet {
public:
    set<int> hs;
    /** Initialize your data structure here. */
    MyHashSet() {
        
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
        set<int>::iterator it = hs.find(key);
        if (it != hs.end()) {
            return true;
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
https://leetcode-cn.com/submissions/detail/154491163/

32 / 32 个通过测试用例
状态：通过
执行用时: 100 ms
内存消耗: 40.5 MB

执行用时：100 ms, 在所有 C++ 提交中击败了83.79%的用户
内存消耗：40.5 MB, 在所有 C++ 提交中击败了63.12%的用户
*/
