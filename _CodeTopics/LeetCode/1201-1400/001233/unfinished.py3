class TrieNode(object):

    def __init__(self, val='', isLeaf=False, children={}):
        self.isLeaf = isLeaf
        self.val = val
        self.children = children
    
class Trie(object):

    def __init__(self):
        self.root = TrieNode('')
    
    def insert(self, folder_str):
        curr = self.root
        # folder_lis = folder_str.split('/')
        folder_lis = folder_str.split('/')[1:]
        sub_folder_str = ''
        for folder in folder_lis:
            sub_folder_str += '/' + folder
            if folder not in curr.children:
                curr.children[folder] = TrieNode(val=sub_folder_str, children={folder})
            curr = curr.children[folder]
        curr.isLeaf = True
    
    def find_nearest_leaf(self):
        res = []
        for child in self.root.children.values():
            if child.isLeaf:
                res.append(child.val)
                continue
            currLevel = [child]
            while currLevel:
                nextLevel = []
                for node in currLevel:
                    if node.isLeaf:
                        res.append(node.val)
                        nextLevel.clear()
                    else:
                        nextLevel.extend(node.children.values())    
                currLevel = nextLevel
        print(res)
        return res

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:

        # 实际上只需要构建出字典树，然后沿着字典树根节点下的每个分支找到最短的那条路径即可。
        # 所以实际上这里的 Trie 不需要常规的 search 或者 startsWith 方法，
        # 而是一个新的、能满足上述描述的方法。

        tr = Trie()
        for path in folder:
            tr.insert(path)
        return tr.find_nearest_leaf()
