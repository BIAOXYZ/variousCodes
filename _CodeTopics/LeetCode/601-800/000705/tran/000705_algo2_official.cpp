// 官方答案，只是试了试开头 static 那里删掉会怎么样。
class MyHashSet {
private:
    vector<list<int>> data;
    // 下面那行如果改成这样 const int base = 769; 就过不去了。如果想不用 static，那么
    // 接下来的 hash 函数以及 MyHashSet(): data(base) {} 都得改！！！
    static const int base = 769;
    static int hash(int key) {
        return key % base;
    }
public:
    /** Initialize your data structure here. */
    MyHashSet(): data(base) {}
    
    void add(int key) {
        int h = hash(key);
        for (auto it = data[h].begin(); it != data[h].end(); it++) {
            if ((*it) == key) {
                return;
            }
        }
        data[h].push_back(key);
    }
    
    void remove(int key) {
        int h = hash(key);
        for (auto it = data[h].begin(); it != data[h].end(); it++) {
            if ((*it) == key) {
                data[h].erase(it);
                return;
            }
        }
    }
    
    /** Returns true if this set contains the specified element */
    bool contains(int key) {
        int h = hash(key);
        for (auto it = data[h].begin(); it != data[h].end(); it++) {
            if ((*it) == key) {
                return true;
            }
        }
        return false;
    }
};

/*
https://leetcode-cn.com/submissions/detail/154678359/

32 / 32 个通过测试用例
状态：通过
执行用时: 80 ms
内存消耗: 40.5 MB

执行用时：80 ms, 在所有 C++ 提交中击败了99.53%的用户
内存消耗：40.5 MB, 在所有 C++ 提交中击败了62.93%的用户
*/
