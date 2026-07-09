# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # Approach 1: Breadth First Search

        # if not root:
        #     return None

        # q = [root]
        # while q:
        #     n = q.pop(0)
        #     n.left, n.right = n.right, n.left

        #     if n.left:
        #         q.append(n.left)
        #     if n.right:
        #         q.append(n.right)

        # return root


        # Approach 2: Depth First Search (Recursion)

        # if not root:
        #     return None

        # root.left, root.right = root.right, root.left

        # root.left = self.invertTree(root.left)
        # root.right = self.invertTree(root.right)

        # return root


        # Approach 3: Depth First Search (Iteration)

        if not root:
            return None

        s = [root]
        while s:
            n = s.pop()
            n.left, n.right = n.right, n.left

            if n.left:
                s.append(n.left)
            if n.right:
                s.append(n.right)
        return root