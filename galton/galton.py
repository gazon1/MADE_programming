Debug=False
from math import gcd


class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self, level=0):
        ret = "  "*level+repr(self.val)+"\n"
        children = [x for x in (self.left, self.right) if x]
        for child in children:
            ret += child.__str__(level+1)
        return ret


class Tree:
    def __init__(self, root=None):
        self.root = root
        self.ans = []

    def preOrder(self, root, weight=0):
        if root:
            # if Debug:
            #     print(root)
            #     print("weight:", weight)
            self.preOrder(root.left, weight + root.val)
            self.preOrder(root.right, weight + root.val)
        else:
            self.ans.append(weight)
            # if Debug:
            #     print("returned")



def create_tree(l):
    # if Debug:
    #     print(l)
    root = Node(l[0][0])
    tree = Tree(root)
    _current_nodes = [root]
    for h_i in l[1:]:
        current_nodes = _current_nodes
        _current_nodes = []
        for idx, node in enumerate(current_nodes):
            # if Debug:
            #     print(len(current_nodes), len(h_i))
            if idx != 0:
                node.left = _current_nodes[-1]
                node.right = Node(h_i[idx + 1])
                _current_nodes.append(node.right)
            elif idx == 0:
                node.left = Node(h_i[idx])
                node.right = Node(h_i[idx + 1])
                _current_nodes.extend([node.left, node.right])
    return tree

def solve(tree, h):
    # calc num of pathes
    # sum and normalize output of preOrder tree
    num_path = 2 ** int(h - 1)
    tree.preOrder(tree.root)
    res = tree.ans[::2]
    # if Debug:
    #     print("res=", res)
    res = sum(res)
    d = gcd(res, num_path)

    # if Debug:
    #     print("not normalize res:", res)
    #     print("num_path", num_path)
    #     print("d:",d)
    num_path = num_path // d
    return f"{res // d} {num_path}"


if __name__ == "__main__":
    for i in  range(int(input())):
        h = int(input())
        l = []
        for j in range(h):
            l.append(list(map(int, input().split())))
        tree = create_tree(l)
        ans = solve(tree, h)
        print(ans)
