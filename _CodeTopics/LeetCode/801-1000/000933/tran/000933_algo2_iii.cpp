// 注意这里用的是 queue，不是 deque 了。
// queue 的push和pop没用后缀，就这俩，但是 deque 是
// 有四个的：push_back、push_front、pop_back、pop_front

#include <queue>
class RecentCounter {
    queue<int> q{};
public:
    RecentCounter() {

    }
    
    int ping(int t) {
        q.push(t);
        while (q.front() < t - 3000)
            q.pop();
        return q.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */

/*
https://leetcode-cn.com/submissions/detail/309737291/

执行用时：
132 ms
, 在所有 C++ 提交中击败了
58.81%
的用户
内存消耗：
56 MB
, 在所有 C++ 提交中击败了
50.49%
的用户
通过测试用例：
68 / 68
*/
