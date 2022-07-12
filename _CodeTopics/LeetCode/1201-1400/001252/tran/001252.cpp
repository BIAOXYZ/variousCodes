class Solution {
public:
    int oddCells(int m, int n, vector<vector<int>>& indices) {

        vector<vector<int>> matrix(m, vector<int>(n, 0));
        for (int ind = 0; ind < indices.size(); ++ind) {
            int row = indices[ind][0], col = indices[ind][1];
            for (int i = 0; i < m; ++i) {
                matrix[i][col] += 1;
            }
            for (int j = 0; j < n; ++j) {
                matrix[row][j] += 1;
            }
        }

        int res = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (matrix[i][j] & 1 == 1)
                    res += 1;
            }
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/336040991/

执行用时：
4 ms
, 在所有 C++ 提交中击败了
71.37%
的用户
内存消耗：
7.8 MB
, 在所有 C++ 提交中击败了
33.06%
的用户
通过测试用例：
44 / 44
*/
