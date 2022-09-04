class Solution {
public:
    int sum_of_column(vector<vector<int>>& mat, int j) {
        int ret = 0;
        for (int i = 0; i < mat.size(); ++i) {
            ret += mat[i][j];
        }
        return ret;
    }

    int numSpecial(vector<vector<int>>& mat) {

        // 第 206 场周赛第一题
        // https://leetcode-cn.com/submissions/detail/107496893/

        int m = mat.size(), n = mat[0].size();
        int res = 0;

        for (int i = 0; i < m; ++i) {
            if (std::accumulate(mat[i].begin(), mat[i].end(), 0) != 1) {
                continue;
            }
            for (int j = 0; j < n; ++j) {
                if (mat[i][j] != 1) {
                    continue;
                }
                if (sum_of_column(mat, j) == 1) {
                    res += 1;
                }
            }
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/359082129/

执行用时：
20 ms
, 在所有 C++ 提交中击败了
49.00%
的用户
内存消耗：
12.5 MB
, 在所有 C++ 提交中击败了
60.64%
的用户
通过测试用例：
95 / 95
*/
