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

    def build_tree(self, node: Node):
        if self.root is None:  # 如果树为空，直接将node赋值给根节点
            self.root = node
            self.que.append(self.root)
        else:
            self.que.append(node)
            father_node = self.que[0]
            if father_node.lchild is None:
                father_node.lchild = node
            else:
                father_node.rchild = node
                # print(father_node.elem)  # 弹出之前打印
                self.que.pop(0)

    def pre_order(self, node: Node):
        if node is None:
            return
        print(node.elem, end=' ')
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def in_order(self, node: Node):
        if node is None:
            return
        self.in_order(node.lchild)
        print(node.elem, end=' ')
        self.in_order(node.rchild)

    def post_order(self, node: Node):
        if node is None:
            return
        self.post_order(node.lchild)
        self.post_order(node.rchild)
        print(node.elem, end=' ')

    def level_order(self):
        help_queue = [self.root]
        while help_queue:
            father_node = help_queue.pop(0)
            print(father_node.elem, end=' ')
            if father_node.lchild is not None:
                help_queue.append(father_node.lchild)
            if father_node.rchild is not None:
                help_queue.append(father_node.rchild)


if __name__ == '__main__':
    tree = BTree()
    for i in range(1, 11):
        new_node = Node(i)
        tree.build_tree(new_node)
    # for i in tree.que:  # 遍历队列中的节点
    #     print(i.elem)
    tree.pre_order(tree.root)
    print()
    tree.in_order(tree.root)
    print()
    tree.post_order(tree.root)
    print()
    tree.level_order()
