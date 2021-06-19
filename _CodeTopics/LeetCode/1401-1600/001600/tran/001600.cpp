class Node {
public:
    string name;
    vector<Node*> sons;
    bool alive;
public:
    Node(string name) {
        this->name = name;
        this->sons = vector<Node*>{};
        this->alive = true;
    }
};

class ThroneInheritance {
public:
    Node* kingNode;
    unordered_map<string, Node*> dic;
public:
    ThroneInheritance(string kingName) {
        this->kingNode = new Node(kingName);
        this->dic[kingName] = this->kingNode;
    }
    
    void birth(string parentName, string childName) {
        Node* childNode = new Node(childName);
        this->dic[childName] = childNode;
        this->dic[parentName]->sons.push_back(childNode);
    }
    
    void death(string name) {
        this->dic[name]->alive = false;
    }
    
    void dfs(Node* currNode, vector<string>& res) {
        if (currNode->alive) {
            res.push_back(currNode->name);
        }
        for (auto childNode : currNode->sons) {
            dfs(childNode, res);
        }
    }

    vector<string> getInheritanceOrder() {
        vector<string> res;
        dfs(this->kingNode, res);
        return res;
    }
};

/**
 * Your ThroneInheritance object will be instantiated and called as such:
 * ThroneInheritance* obj = new ThroneInheritance(kingName);
 * obj->birth(parentName,childName);
 * obj->death(name);
 * vector<string> param_3 = obj->getInheritanceOrder();
 */

/*
https://leetcode-cn.com/submissions/detail/188099432/

49 / 49 个通过测试用例
状态：通过
执行用时: 476 ms
内存消耗: 163.3 MB

执行用时：476 ms, 在所有 C++ 提交中击败了98.51%的用户
内存消耗：163.3 MB, 在所有 C++ 提交中击败了79.85%的用户
*/
