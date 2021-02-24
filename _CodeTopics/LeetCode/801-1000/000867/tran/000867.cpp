class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {

        int rows = matrix.size(), cols = matrix[0].size();
        vector<vector <int>> transposedMatrix(cols, vector<int>(rows, 0));
        for (int i = 0; i < cols; ++i) {
            for (int j = 0; j < rows; ++j) {
                transposedMatrix[i][j] = matrix[j][i];
            }
        }
        return transposedMatrix;
    }
};

/*
https://leetcode-cn.com/submissions/detail/148455959/

36 / 36 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 10.4 MB

执行用时：16 ms, 在所有 C++ 提交中击败了69.40%的用户
内存消耗：10.4 MB, 在所有 C++ 提交中击败了8.45%的用户
*/
