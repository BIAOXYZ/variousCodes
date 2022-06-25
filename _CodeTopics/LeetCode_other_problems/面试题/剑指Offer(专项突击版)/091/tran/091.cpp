class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        
        int m = costs.size(), n = costs[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        for (int x = 0; x < m; ++x) {
            for (int y = 0; y < n; ++y) {
                if (x == 0) {
                    dp[x][y] = costs[x][y];
                } else {
                    // 这里用下面这句会报错：
                    // Line 1034: Char 34: runtime error: addition of unsigned offset to 0x602000000190 overflowed to 0x60200000018c (stl_vector.h) SUMMARY: UndefinedBehaviorSanitizer: undefined-behavior /usr/bin/../lib/gcc/x86_64-linux-gnu/9/../../../../include/c++/9/bits/stl_vector.h:1043:34
                    // 所以得把 y-1 变成 y+2。 
                    // dp[x][y] = min(dp[x-1][(y-1)%3], dp[x-1][(y+1)%3]) + costs[x][y];
                    dp[x][y] = min(dp[x-1][(y+2)%3], dp[x-1][(y+1)%3]) + costs[x][y];
                }
            }
        }
        return *min_element(dp[m-1].begin(), dp[m-1].end());
    }
};

/*
https://leetcode.cn/submissions/detail/329322604/

执行用时：
12 ms
, 在所有 C++ 提交中击败了
12.90%
的用户
内存消耗：
9.8 MB
, 在所有 C++ 提交中击败了
42.66%
的用户
通过测试用例：
100 / 100
*/
