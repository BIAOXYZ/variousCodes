// 官方答案（小改）
class MyHashSet {
private:
    vector<list<int>> data;
    /*
    // 如果硬要要删 base 变量定义前面的 static，那么首先接下来的 hash 函数要做相应修改：
       也去掉 static 或者 return key % base; 变成 return key % 769;
    // 最关键的修改是：  MyHashSet(): data(base) {} 必须改成 MyHashSet(): data(769) {}
    */
    const int base = 769;
    int hash(int key) {
        return key % base;
    }
public:
    /** Initialize your data structure here. */
    MyHashSet(): data(769) {}
    
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
https://leetcode-cn.com/submissions/detail/154683006/

32 / 32 个通过测试用例
状态：通过
执行用时: 108 ms
内存消耗: 40.7 MB

执行用时：108 ms, 在所有 C++ 提交中击败了74.50%的用户
内存消耗：40.7 MB, 在所有 C++ 提交中击败了60.56%的用户
*/
