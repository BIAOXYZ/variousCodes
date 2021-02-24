class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {

        int rows = matrix.size(), cols = matrix[0].size();
        vector<vector <int>> transposedMatrix;
        // vector<vector <int>> transposedMatrix(cols, vector<int>(rows, 0));
        // 这里使用resize()函数来初始化新申请的二维矩阵，而不是像上一个实现一样直接初始化。
        // 其实后面肯定是用直接初始化的方式，这里就是练练手。
        transposedMatrix.resize(cols);
        for (int i = 0; i < cols; ++i) {
            transposedMatrix[i].resize(rows, 0);
        }
        
        for (int i = 0; i < cols; ++i) {
            for (int j = 0; j < rows; ++j) {
                transposedMatrix[i][j] = matrix[j][i];
            }
        }
        return transposedMatrix;
    }
};

/*
https://leetcode-cn.com/submissions/detail/148456767/

36 / 36 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 10.3 MB

执行用时：12 ms, 在所有 C++ 提交中击败了90.68%的用户
内存消耗：10.3 MB, 在所有 C++ 提交中击败了9.81%的用户
*/
