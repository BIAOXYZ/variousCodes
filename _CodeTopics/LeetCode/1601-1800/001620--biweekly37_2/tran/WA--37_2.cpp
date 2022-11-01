class Solution {
public:
    vector<int> bestCoordinate(vector<vector<int>>& towers, int radius) {

        // 第 37 场双周赛第二题
        // https://leetcode.cn/submissions/detail/116509110/

        std::function<int(int, int)> calculate_signal = [&](int x, int y) -> int {
            int total = 0;
            for (auto tower : towers) {
                float distance = sqrt(pow((tower[0]-x), 2) + pow((tower[1]-y), 2));
                if (distance < (float)radius) {
                    total += floor(tower[2] / (1+distance));
                }
            }
            return total;
        };

        int maxX = towers[0][0], maxY = towers[0][1];
        int minX = towers[0][0], minY = towers[0][1];
        for (auto tower : towers) {
            maxX = max(maxX, tower[0]);
            maxY = max(maxY, tower[1]);
            minX = min(minX, tower[0]);
            minY = min(minY, tower[1]);
        }
        int totalSignal = calculate_signal(towers[0][0], towers[0][1]);
        vector<int> res = {towers[0][0], towers[0][1]};
        for (int x = minX; x < maxX + 1; ++x) {
            for (int y = minY; y < maxY + 1; ++y) {
                int tmp = calculate_signal(x,y);
                if (totalSignal < tmp) {
                    totalSignal = tmp;
                    res = vector<int>{x, y};
                } else if (totalSignal == tmp) {
                    if (x < res[0]) {
                        res = vector<int>{x, y};
                    } else if (x == res[0]) {
                        if (y < res[1]) {
                            res = vector<int>{x, y};
                        }
                    } 
                }
            }
        }
        return res;
    }
};

/*
https://leetcode.cn/submissions/detail/378542159/

95 / 100 个通过测试用例
状态：解答错误

输入：
[[42,0,0]]
7
输出：
[42,0]
预期结果：
[0,0]
*/
