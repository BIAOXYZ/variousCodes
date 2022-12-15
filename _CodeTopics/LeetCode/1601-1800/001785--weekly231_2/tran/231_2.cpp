class Solution {
public:
    int minElements(vector<int>& nums, int limit, int goal) {

        // 第 231 场周赛第二题
        // https://leetcode.cn/submissions/detail/151995578/

        long long diff = abs(goal - std::accumulate(nums.begin(), nums.end(), 0LL));
        return diff / limit + (diff % limit != 0? 1 : 0);
    }
};

/*
https://leetcode.cn/submissions/detail/389364694/

执行用时：
88 ms
, 在所有 C++ 提交中击败了
92.20%
的用户
内存消耗：
71.8 MB
, 在所有 C++ 提交中击败了
13.48%
的用户
通过测试用例：
77 / 77
*/
