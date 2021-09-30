class Solution {
public:
    string destCity(vector<vector<string>>& paths) {

        // 第 187 周周赛第一题
        // https://leetcode-cn.com/submissions/detail/67765940/

        unordered_map<string, int> resdic = {};
        for (auto path : paths) {
            resdic[path[0]] = 0;
            if (resdic.find(path[1]) == resdic.end()) {
                resdic[path[1]] = 1;
            }
        }
        
        string res = "";
        for (unordered_map<string, int>::iterator it = resdic.begin(); it != resdic.end(); ++it) {
            if ((*it).second == 1) {
                res = (*it).first;
                break;
            }
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/224860077/

103 / 103 个通过测试用例
状态：通过
执行用时: 8 ms
内存消耗: 11.1 MB

执行用时：8 ms, 在所有 C++ 提交中击败了96.09%的用户
内存消耗：11.1 MB, 在所有 C++ 提交中击败了32.57%的用户
*/
/*
对比这三个C++的提交（`187_1.cpp`，`187_1_ii.cpp`，`187_1_iii.cpp`），是否说明用 `(*it).first/second` 的方式是最快的？
*/
