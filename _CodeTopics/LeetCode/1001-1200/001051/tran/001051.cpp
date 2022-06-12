class Solution {
public:
    int heightChecker(vector<int>& heights) {

        // 也可以用： vector<int> expected = heights;
        // 或者： vector<int> expected(heights);
        vector<int> expected{heights};
        sort(expected.begin(), expected.end());
        int res = 0;
        for (int i = 0; i < heights.size(); ++i) {
            if (heights[i] != expected[i]) {
                ++res;
            }
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/324580203/

执行用时：
0 ms
, 在所有 C++ 提交中击败了
100.00%
的用户
内存消耗：
8 MB
, 在所有 C++ 提交中击败了
32.62%
的用户
通过测试用例：
81 / 81
*/
