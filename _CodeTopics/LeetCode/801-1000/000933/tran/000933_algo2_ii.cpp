#include <deque>
class RecentCounter {
    deque<int> q = {};
public:
    RecentCounter() {

    }
    
    int ping(int t) {
        q.push_back(t);
        // while (q.front() < t - 3000)
        // C++ 的 deque 取第一个元素除了用 .front()，也可以用 q[0]
        while (q[0] < t - 3000)
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
https://leetcode-cn.com/submissions/detail/309736965/

执行用时：
124 ms
, 在所有 C++ 提交中击败了
83.78%
的用户
内存消耗：
56 MB
, 在所有 C++ 提交中击败了
61.30%
的用户
通过测试用例：
68 / 68
*/
