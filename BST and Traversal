class btree:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

    def insert(self,value):
        if value <self.data:
            if not self.left:
                self.left = btree(value)
            else:
                self.left.insert(value)
        if value>=self.data:
            if not self.right:
                self.right=btree(value)
            else:
                self.right.insert(value)


def inorder(node): # left node right

    if node.left:
        inorder(node.left)
    print(node.data)
    if node.right:
        inorder(node.right)

def search(node,value):
    if node.data==value:
        return True
    elif node.data>value:
        if node.left:
            return search(node.left,value)
        else:
            return False
    elif node.data<value:
        if node.right:
            return search(node.right,value)
        else:
            return  False


if __name__=='__main__':
    root = btree(2)
    root.insert(3)
    root.insert(4)
    root.insert(1)
    root.insert(0)
    inorder(root)
    print(search(root,6))
