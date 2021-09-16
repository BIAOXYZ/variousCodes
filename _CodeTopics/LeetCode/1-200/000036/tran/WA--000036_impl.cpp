class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {

        function<bool(int)> check_row = [&](int i) -> bool {
            unordered_set<int> se = {};
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] == '.')
                    continue;
                if (se.find(board[i][j]) != se.end())
                    return false;
                else
                    se.insert(board[i][j]);
            }
            return true;
        };

        function<bool(int)> check_column = [&](int j) -> bool {
            unordered_set<int> se = {};
            for (int i = 0; i < 9; ++i) {
                if (board[i][j] == '.')
                    continue;
                if (se.find(board[i][j]) != se.end())
                    return false;
                else
                    se.insert(board[i][j]);
            }
            return true;
        };

        function<bool(int, int)> check_square = [&](int x, int y) -> bool {
            unordered_set<int> se = {};
            for (int i = x; i < x+3; ++i) {
                for (int j = y; j < y+3; ++j) {
                    if (board[i][j] == '.')
                        continue;
                    if (se.find(board[i][j]) != se.end())
                        return false;
                    else
                        se.insert(board[i][j]);
                }
            } 
            return true;
        };

        for (int i = 0; i < 9; ++i) {
            if (!check_row(i) || !check_row(i))
                return false;
        }
        vector<vector<int>> upLeftCoors = {{0,0},{0,3},{0,6},{3,0},{3,3},{3,6},{6,0},{6,3},{6,6}};
        for (auto coor : upLeftCoors) {
            if (!check_square(coor[0], coor[1])) 
                return false;
        }
        return true;
    }
};

/*
https://leetcode-cn.com/submissions/detail/220210619/

452 / 507 个通过测试用例
状态：解答错误

最后执行的输入：
[[".",".","4",".",".",".","6","3","."],[".",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".","9","."],[".",".",".","5","6",".",".",".","."],["4",".","3",".",".",".",".",".","1"],[".",".",".","7",".",".",".",".","."],[".",".",".","5",".",".",".",".","."],[".",".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".",".","."]]
输出：
true
预期结果：
false
*/
