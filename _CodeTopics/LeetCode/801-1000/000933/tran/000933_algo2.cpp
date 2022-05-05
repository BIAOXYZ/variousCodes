#include <deque>
class RecentCounter {
    deque<int> q = {};
public:
    RecentCounter() {

    }
    
    int ping(int t) {
        q.push_back(t);
        while (q.front() < t - 3000)
            q.pop_front();
        return q.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */

/*
https://leetcode-cn.com/submissions/detail/309736816/

执行用时：
120 ms
, 在所有 C++ 提交中击败了
90.27%
的用户
内存消耗：
55.9 MB
, 在所有 C++ 提交中击败了
91.14%
的用户
通过测试用例：
68 / 68
*/
