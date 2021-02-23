class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        
        int length = A.size();
        // C++ 初始化固定大小的二维矩阵，并全部赋值0。
        vector<vector<int>> B(length, vector<int>(length, 0));
            for (int i = 0; i < length; ++i) {
                for (int j = 0; j < length; ++j) {
                    B[i][j] = 1 - A[i][length-1-j];
                }
            }
        return B;
    }
};

/*
https://leetcode-cn.com/submissions/detail/148138844/

82 / 82 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 8.3 MB

执行用时：4 ms, 在所有 C++ 提交中击败了93.65%的用户
内存消耗：8.3 MB, 在所有 C++ 提交中击败了72.89%的用户
*/
