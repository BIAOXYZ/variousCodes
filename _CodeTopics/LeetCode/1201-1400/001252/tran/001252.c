int oddCells(int m, int n, int** indices, int indicesSize, int* indicesColSize){

    int** matrix = (int**)malloc(sizeof(int*) * m);
    for (int i = 0; i < m; ++i) {
        matrix[i] = (int*)malloc(sizeof(int) * n);
        memset(matrix[i], 0, sizeof(int) * n);
    }
    
    for (int ind = 0; ind < indicesSize; ++ind) {
        int row = indices[ind][0], col = indices[ind][1];
        for (int i = 0; i < m; ++i) {
            matrix[i][col]++;
        }
        for (int j = 0; j < n; ++j) {
            matrix[row][j]++;
        }
    }

    int res = 0;
    for (int i = 0; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (matrix[i][j] & 1)
                res++;
        }
        free(matrix[i]);
    }
    free(matrix);
    return res;
}

/*
https://leetcode.cn/submissions/detail/336085466/

执行用时：
4 ms
, 在所有 C 提交中击败了
94.00%
的用户
内存消耗：
6.3 MB
, 在所有 C 提交中击败了
10.00%
的用户
通过测试用例：
44 / 44
*/
