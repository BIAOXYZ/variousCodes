// https://leetcode-cn.com/submissions/detail/248245338/

class Solution {
public:
    bool hasRing = false;
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        vector<int> visited(numCourses, 0);  // 0 表示未访问过的节点
        unordered_map<int, vector<int>> edges;
        for (vector<int> info : prerequisites) {
            edges[info[1]].push_back(info[0]);
        }
        
        vector<int> res;
        for (int i = 0; i < numCourses; i++) {
            if (!hasRing && visited[i] == 0) {
                dfs(i, visited, edges, res);
            }
        }
        
        if (hasRing) {
            return {};
        }
        reverse(res.begin(), res.end());
        return res;
    }
private:
    void dfs(int vertex, vector<int>& visited, unordered_map<int, vector<int>>& edges, vector<int>& res) {
        visited[vertex] = 1;  // 1 表示正在访问的节点
        for (int v : edges[vertex]) {
            if (visited[v] == 0) {
                dfs(v, visited, edges, res);
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
        res.push_back(vertex);
    }
};

/*
https://leetcode.cn/problems/course-schedule-ii/submissions/464948361/

时间
详情
24ms
击败 39.64%使用 C++ 的用户
内存
详情
14.74MB
击败 6.59%使用 C++ 的用户
*/
