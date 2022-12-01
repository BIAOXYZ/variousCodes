class Solution {
public:
    int nearestValidPoint(int x, int y, vector<vector<int>>& points) {

        // 第 47 场双周赛第一题
        // https://leetcode.cn/submissions/detail/151894984/

        int n = points.size();
        int res = -1;
        int currDistance = INT_MAX;
        for (int i = 0; i < n; ++i) {
            if (points[i][0] == x || points[i][1] == y) {
                int newDistance = abs(points[i][0] - x) + abs(points[i][1] - y);
                if (newDistance < currDistance) {
                    res = i;
                    currDistance = newDistance;
                }
            }
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/386372470/

执行用时：
148 ms
, 在所有 C++ 提交中击败了
55.13%
的用户
内存消耗：
58 MB
, 在所有 C++ 提交中击败了
20.53%
的用户
通过测试用例：
101 / 101
*/
