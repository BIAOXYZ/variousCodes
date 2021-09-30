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
            if (it->second == 1) {
                res = it->first;
                break;
            }
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/224859955/

103 / 103 个通过测试用例
状态：通过
执行用时: 16 ms
内存消耗: 11.2 MB

执行用时：16 ms, 在所有 C++ 提交中击败了33.88%的用户
内存消耗：11.2 MB, 在所有 C++ 提交中击败了22.48%的用户
*/
