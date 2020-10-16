/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}
    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}
    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    Node* connect(Node* root) {

        if (root == nullptr) {
            return root;
        }

        vector<Node*> stack = {root};
        while (stack.size() != 0){
            int length = stack.size(); vector<Node*> nextLevel = {};
            for (int i = 0; i < length; i++) {
                Node* node = stack[i];
                Node* preNode; 
                if (node->left != nullptr) nextLevel.push_back(node->left);
                if (node->right != nullptr) nextLevel.push_back(node->right);
                if (i == 0) {
                    preNode = node;
                }
                else if (i != length-1) {
                    preNode->next = node;
                    preNode = node;
                }
                else {
                    preNode->next = node;
                }  
            }
            stack.clear();
            for (int j = 0; j < nextLevel.size(); j++){
                stack.push_back(nextLevel[j]);
            }
        }
        return root;
    }
};

/*
https://leetcode-cn.com/submissions/detail/116298532/

58 / 58 个通过测试用例
状态：通过
执行用时: 24 ms
内存消耗: 17.6 MB

执行用时：24 ms, 在所有 C++ 提交中击败了97.20%的用户
内存消耗：17.6 MB, 在所有 C++ 提交中击败了5.02%的用户
*/
