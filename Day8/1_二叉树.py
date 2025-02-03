"""
Created on 2025-02-03
"""


# Your code starts here
class Node:
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class BTree:
    def __init__(self):
        self.root = None
        self.que = []  # 用于存放节点的队列

    def build_tree(self,node:Node):
        if self.root is None: # 如果树为空，直接将node赋值给根节点
            self.root = node
            self.que.append(self.root)
        else:
            self.que.append(node)
            father_node = self.que[0]
            if father_node.lchild is None:
                father_node.lchild = node
            else:
                father_node.rchild = node
                print(father_node.elem) #弹出之前打印
                self.que.pop(0)


if __name__ == '__main__':
    tree = BTree()
    for i in range(1, 11):
        new_node = Node(i)
        tree.build_tree(new_node)
    for i in tree.que: # 遍历队列中的节点
        print(i.elem)
