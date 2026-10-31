class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        st1 = [root]
        res = []

        while st1:
            node = st1.pop()
            res.append(node.val)

            if node.left:
                st1.append(node.left)
            if node.right:
                st1.append(node.right)
        return res[::-1]