# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Traversal:
    ############### preorder 递归  ###########
    def preorder(self, root, ans):
        if root:
            ans.append(root.val)
            self.preorder(root.left, ans)
            self.preorder(root.right, ans)

    def preorderTraversal(self, root):
        ans = []
        self.preorder(root, ans)
        return ans

    ################# preorder 非递归   ######
    def preNonRecur(self, root):
        """利用堆栈前序遍历"""
        ans = []
        if root == None:
            return False
        stack = []
        node = root
        while node or stack:
            while node:  # 寻找左子树，压入栈内
                ans.append(node.val)
                stack.append(node)
                node = node.left
            node = stack.pop()
            node = node.right  # 开始寻找右子树
        return ans

    ############### inorder 递归  ###########
    def inorderTraversal(self, root):
        if root == None:
            return []
        elif root.left == None and root.right == None:
            return [root.val]
        else:
            return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)



    ############### inorder 非递归  ###########
    def inNonRecur(self, root):
        """ 利用堆栈中序遍历"""
        if root == None:
            return False
        stack = []
        ans = []
        node = root
        while node or stack:
            while node:  # 从根结点开始，寻找左子树，把它压入栈中
                stack.append(node)
                node = node.left
            node = stack.pop()  # while 结束代表前一个节点没有了左子树
            ans.append(node.val)
            node = node.right  # 然后开始寻找右子树
        return ans


    ############### postorder 递归  ###########
    def post(self, root, ans):
        if root:
            self.post(root.left, ans)
            self.post(root.right, ans)
            ans.append(root.val)

    def postorderTraversal(self, root):
        ans = []
        self.post(root, ans)
        return ans

    ############### postorder 非递归  ###########
    def postNonRecur(self, root):
        """利用堆栈后序遍历"""
        if root is None:
            return False
        stack1 = [root]
        stack2 = []
        ans= []
        while stack1:  # 找出后序遍历的逆序，存放在 stack2中
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:  # 将 stack2中的元素出栈，即是后序遍历序列
            #print(stack2.pop().value, end=' ')
            ans.append(stack2.pop().val)
        return ans

    ############### levelorder 递归  ###########
    def level(self, root, level, ans):
        if root:
            if len(ans) == level:
                ans.append([])
            ans[level].append(root.val)
            if root.left:
                self.level(root.left, level + 1, ans)
            if root.right:
                self.level(root.right, level + 1, ans)

    def levelOrder(self, root):
        ans = []
        self.level(root, 0, ans)
        return ans

    ############### levelorder 非递归  ###########
    def levelNonRecur(self, root):
        """层序遍历"""
        if root is None:
            return False
        treeList = [root]
        ans = []
        while treeList:
            node = treeList.pop(0)  # 先进先出
            ans.append(node.val)
            if node.left:
                treeList.append(node.left)
            if node.right:
                treeList.append(node.right)
        return ans

    def levelNonRecur2(self, root):
        #非递归
        tree = []
        if not root:
            return tree
        curr_level = [root]
        # print(type(root), type(curr_level))  # (<class 'precompiled.treenode.TreeNode'>, <type 'list'>)
        # print(curr_level)  # 作为list，却并不能遍历整个树
        while curr_level:
            level_list = []
            next_level = []
            for temp in curr_level:
                level_list.append(temp.val)
                if temp.left:
                    next_level.append(temp.left)
                if temp.right:
                    next_level.append(temp.right)
            tree.append(level_list)
            curr_level = next_level
        return tree


##### test

root=TreeNode(1)
r2=TreeNode(2)
r3=TreeNode(3)
r4=TreeNode(4)
r5=TreeNode(5)
r6=TreeNode(6)
r7=TreeNode(7)
r8=TreeNode(8)
r9=TreeNode(9)
r10=TreeNode(10)
root.left=r2
root.right=r3
r2.left=r4
r2.right=r5
r3.left=None
r3.right=r6
r4.left=r7
r4.right=r8
r5.left=None
r5.right=None
r6.left=r9
r6.right=r10
r7.left=None
r7.right=None
r8.left=None
r8.right=None
r9.left=None
r9.right=None
r10.left=None
r10.right=None

s = Traversal()
print(s.preorderTraversal(root))
print(s.preNonRecur(root))
print(s.inorderTraversal(root))
print(s.inNonRecur(root))
print(s.postorderTraversal(root))
print(s.postNonRecur(root))
print(s.levelOrder(root))
print(s.levelNonRecur(root))
print(s.levelNonRecur2(root))


