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
        for (auto kvpair : resdic) {
            if (kvpair.second == 1)
                res = kvpair.first;
                break;
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/224858174/

22 / 103 个通过测试用例
状态：解答错误

输入：
[["pYyNGfBYbm","wxAscRuzOl"],["kzwEQHfwce","pYyNGfBYbm"]]
输出：
""
预期结果：
"wxAscRuzOl"
*/
