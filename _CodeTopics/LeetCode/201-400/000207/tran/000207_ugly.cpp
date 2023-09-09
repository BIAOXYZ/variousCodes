// https://leetcode.cn/problems/median-of-two-sorted-arrays/submissions/316879101/
class Solution {
public:
    bool hasRing = false;
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> visited(numCourses, 0);  // 0 表示未访问过的节点
        unordered_map<int, vector<int>> edges;
        for (vector<int> info : prerequisites) {
            edges[info[1]].push_back(info[0]);
        }
        for (int i = 0; i < numCourses; i++) {
            if (!hasRing && visited[i] == 0) {
                dfs(i, visited, edges);
            }
        }
        return !hasRing;
    }
private:
    void dfs(int vertex, vector<int>& visited, unordered_map<int, vector<int>>& edges) {
        visited[vertex] = 1;  // 1 表示正在访问的节点
        for (int v : edges[vertex]) {
            if (visited[v] == 0) {
                dfs(v, visited, edges);
                if (hasRing) {
                    return;
                }
            }
            else if (visited[v] == 1) {
                hasRing = true;
                return;
            }
        }
        visited[vertex] = 2;  // 2 表示已经访问结束的节点
    }
};

/*
https://leetcode.cn/problems/course-schedule/submissions/464653813/?envType=daily-question&envId=2023-09-09

时间
详情
24ms
击败 40.03%使用 C++ 的用户
内存
详情
14.70MB
击败 8.17%使用 C++ 的用户
*/
