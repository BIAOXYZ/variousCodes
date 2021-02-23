class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        
        int length = A.size();
        for (int i = 0; i < length; ++i) {
            if (length % 2 == 1) {
                for (int j = 0; j < length/2 + 1; ++j) {
                    swap(A[i][j], A[i][length-1-j]);
                    A[i][j] = 1 - A[i][j];
                    if (j != length - j - 1)
                        A[i][length-1-j] = 1 - A[i][length-1-j];
                }
            } 
            else {
                for (int j = 0; j < length/2; ++j) {
                    swap(A[i][j], A[i][length-1-j]);
                    A[i][j] = 1 - A[i][j];
                    A[i][length-1-j] = 1 - A[i][length-1-j];
                }
            }
        }
        return A;
    }
};

/*
https://leetcode-cn.com/submissions/detail/148143278/

82 / 82 个通过测试用例
状态：通过
执行用时: 0 ms
内存消耗: 8.3 MB

执行用时：0 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：8.3 MB, 在所有 C++ 提交中击败了77.36%的用户
*/
/*
呃，好像是第一次（非copy答案的情况下）C++出0毫秒，果然直接击败100%。。。
*/
