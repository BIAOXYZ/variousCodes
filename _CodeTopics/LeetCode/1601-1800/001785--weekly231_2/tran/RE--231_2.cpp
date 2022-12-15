class Solution {
public:
    int minElements(vector<int>& nums, int limit, int goal) {

        // 第 231 场周赛第二题
        // https://leetcode.cn/submissions/detail/151995578/

        int diff = abs(goal - std::accumulate(nums.begin(), nums.end(), 0));
        return diff / limit + (diff % limit != 0? 1 : 0);
    }
};

/*
https://leetcode.cn/submissions/detail/389363842/

65 / 77 个通过测试用例
状态：执行出错

执行出错信息：
Line 130: Char 39: runtime error: signed integer overflow: 2147000000 + 1000000 cannot be represented in type 'int' (stl_numeric.h)
SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior /usr/bin/../lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/stl_numeric.h:139:39

最后执行的输入：
*/
