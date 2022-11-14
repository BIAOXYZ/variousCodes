class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {

        // 第 222 场周赛第一题
        // https://leetcode.cn/submissions/detail/135536963/

        std::sort(
            boxTypes.begin(),
            boxTypes.end(), 
            [](const vector<int>& v1, const vector<int>& v2){return v1[1] > v2[1];}
        );
        int res = 0;

        for (int i = 0; i < boxTypes.size(); ++i) {
            if (truckSize >= boxTypes[i][0]) {
                truckSize -= boxTypes[i][0];
                res += boxTypes[i][0] * boxTypes[i][1];
            } else {
                res += truckSize * boxTypes[i][1];
                break;
            }
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/382088297/

执行用时：
40 ms
, 在所有 C++ 提交中击败了
59.08%
的用户
内存消耗：
15.4 MB
, 在所有 C++ 提交中击败了
84.98%
的用户
通过测试用例：
76 / 76
*/
