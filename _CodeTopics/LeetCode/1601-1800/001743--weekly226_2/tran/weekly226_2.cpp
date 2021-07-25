class Solution {
public:
    vector<int> restoreArray(vector<vector<int>>& adjacentPairs) {

        // 此题为第 226 周周赛第二题。待翻译的原始提交为：
        // https://leetcode-cn.com/submissions/detail/142480473/

        unordered_map<int, int> dic1;
        unordered_map<int, vector<int>> dic2;
        for (int i = 0; i < adjacentPairs.size(); ++i) {
            vector<int> pair = adjacentPairs[i]; 
            if (dic1.find(pair[0]) != dic1.end()) dic1[pair[0]] += 1;
            else dic1[pair[0]] = 1;
            if (dic1.find(pair[1]) != dic1.end()) dic1[pair[1]] += 1;
            else dic1[pair[1]] = 1;
            if (dic2.find(pair[0]) != dic2.end()) dic2[pair[0]].push_back(i);
            else dic2[pair[0]] = vector{i};
            if (dic2.find(pair[1]) != dic2.end()) dic2[pair[1]].push_back(i);
            else dic2[pair[1]] = vector{i};
        }

        vector<int> res;
        for (std::pair<int, int> kvpair : dic1) {
            if (kvpair.second == 1) {
                res.push_back(kvpair.first);
                break;
            }
        }

        unordered_set<int> resFast{res[0]};
        int currLen = 1;
        while (currLen < adjacentPairs.size() + 1) {
            int currElem = res.back();
            for (int ind : dic2[currElem]) {
                vector pair = adjacentPairs[ind];
                if (resFast.find(pair[0]) == resFast.end()) {
                    res.push_back(pair[0]);
                    resFast.insert(pair[0]);
                    break;
                }
                if (resFast.find(pair[1]) == resFast.end()) {
                    res.push_back(pair[1]);
                    resFast.insert(pair[1]);
                    break;
                }
            }
            currLen += 1;
        }
        return res;
    }
};

/*
https://leetcode-cn.com/submissions/detail/199582627/

46 / 46 个通过测试用例
状态：通过
执行用时: 688 ms
内存消耗: 147.7 MB

执行用时：688 ms, 在所有 C++ 提交中击败了53.69%的用户
内存消耗：147.7 MB, 在所有 C++ 提交中击败了14.77%的用户
*/
