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
        for (std::pair<string, int> kvpair : resdic) {
            if (kvpair.second == 1) {
                res = kvpair.first;
                break;
            }
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/224860490/

103 / 103 个通过测试用例
状态：通过
执行用时: 12 ms
内存消耗: 11.2 MB

执行用时：12 ms, 在所有 C++ 提交中击败了78.83%的用户
内存消耗：11.2 MB, 在所有 C++ 提交中击败了23.45%的用户
*/
