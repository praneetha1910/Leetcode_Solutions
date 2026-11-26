# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        if not inorder:
            return None
        root_val=postorder.pop()
        root=TreeNode(root_val)
        mid=inorder.index(root_val)
        root.right=self.buildTree(
            inorder[mid+1:],postorder
        )
        root.left=self.buildTree(
            inorder[:mid],postorder

        )
        return root