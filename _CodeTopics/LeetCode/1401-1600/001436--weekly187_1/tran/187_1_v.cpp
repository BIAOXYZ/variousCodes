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
        // 这个才是最最像 python 的写法，是偶然间在 cppreference 看到的，学习了～
        // https://en.cppreference.com/w/cpp/container/unordered_map
        for (auto [k, v] : resdic) {
            if (v == 1) {
                res = k;
                break;
            }
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/224860645/

103 / 103 个通过测试用例
状态：通过
执行用时: 4 ms
内存消耗: 10.9 MB

执行用时：4 ms, 在所有 C++ 提交中击败了100.00%的用户
内存消耗：10.9 MB, 在所有 C++ 提交中击败了45.93%的用户
*/
/*
注：本来就觉得这个遍历的写法很棒（如注释中所说，这种写法最接近python的写法），
   结果时间还这么牛叉，直接超越百分之百了～
*/
