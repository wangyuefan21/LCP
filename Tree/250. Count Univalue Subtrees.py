# Given the root of a binary tree, return the number of uni-value subtrees.
# A uni-value subtree means all nodes of the subtree have the same value.

# traverse down the tree
# check the left and right subtree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def countUnivalSubtrees(root):
    ans = 0
    def check(root):
        nonlocal ans
        if root is None:
            return None
        # reach to leaf node
        if not root.left and not root.right:
            ans += 1
            return root.val
        # check both left and right subtree
        if root.left and root.right:
            left = check(root.left)
            right = check(root.right)
            if left == right == root.val:
                ans += 1
                return left
            return None
        # only left subtree
        if root.left:
            left = check(root.left)
            if left == root.val:
                ans += 1
                return left
            return None
        # only right subtree
        if root.right:
            right = check(root.right)
            if right == root.val:
                ans += 1
                return right
            return None
    check(root)
    return ans

if __name__ == '__main__':
    root = TreeNode(9)
    root.left = TreeNode(0)
    root.right = TreeNode(0)
    root.left.right = TreeNode(8)
    root.left.right.left = TreeNode(89)
    root.left.right.right = TreeNode(-38)
    root.right.left = TreeNode(8)
    root.right.left.left = TreeNode(-38)
    root.right.left.right = TreeNode(89)
    assert countUnivalSubtrees(root) == 4

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(5)
    root.right = TreeNode(5)
    root.right.right = TreeNode(5)
    assert countUnivalSubtrees(root) == 4

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.left.left.left = TreeNode(1)
    root.right = TreeNode(5)
    root.right.right = TreeNode(5)
    countUnivalSubtrees(root)
    assert countUnivalSubtrees(root) == 6

# solution from LC
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        if root is None:
            return 0
        self.check(root, root.val)
        return self.count

    def check(self, node, val):
        if node is None: return True
        left = self.check(node.left, node.val)
        right = self.check(node.right, node.val)
        if not (left and right):
            return False
        self.count += 1
        return node.val == val