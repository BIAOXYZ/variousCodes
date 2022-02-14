class Solution {
public:
    vector<int> luckyNumbers (vector<vector<int>>& matrix) {

        // 第 180 场周赛第一题
        // https://leetcode-cn.com/submissions/detail/53863331/
        
        int m = matrix.size(), n = matrix[0].size();
        vector<int> lucknumberlist;
        for (int i = 0; i < m; ++i) {
            vector<int> curr_row = matrix[i];
            int curr_row_min = *min_element(curr_row.begin(), curr_row.end());
            vector<int>::iterator it = find(curr_row.begin(), curr_row.end(), curr_row_min);
            int ind = std::distance(curr_row.begin(), it);
            
            bool flag = true;
            for (int j = 0; j < m; ++j) {
                if (curr_row_min < matrix[j][ind]) {
                    flag = false;
                    break;
                }
            }
            if (flag) {
                lucknumberlist.push_back(curr_row_min);
            } else {
                flag = true;
            }
        }
        return lucknumberlist;
    }
};

/*
https://leetcode-cn.com/submissions/detail/268441735/

执行用时：16 ms, 在所有 C++ 提交中击败了92.96%的用户
内存消耗：11.7 MB, 在所有 C++ 提交中击败了8.45%的用户
通过测试用例：
104 / 104
*/
