
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        deck = []
        def trav(root):
            if root :
                trav(root.left)
                deck.append(root.val)
                trav(root.right)

        trav(root)

        return deck
        
root = TreeNode(1) 

root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(3)
root.left.right = TreeNode(5)

p = Solution()
print(p.inorderTraversal(root))
