class NoArvore:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class ArvoreBinaria:
    def __init__(self, data=None):
        if data:
            node = NoArvore(data)
            self.root = node
        else:
            self.root = None

    def simetric_traversal(self,node=None):
        if node is None:
            node = self.root
        if node.left:
            print('(', end="")    
            self.simetric_traversal(node.left)
        print(node, end='')
        if node.right:
            self.simetric_traversal(node.right)
            print(")", end="")
        print('')    

if __name__ == "__main__":
    tree = ArvoreBinaria(7)
    tree.root.left = NoArvore(14)
    tree.root.right = NoArvore(18)

    print(tree.root)
    print(tree.root.left)
    print(tree.root.right)