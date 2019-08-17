class TreeNode:
    def __init__(self,arg):
        self.data = arg
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self,val):
        self.root = TreeNode(val)
    
    def insert(self,root,data):
        if root == None:
            root = TreeNode(data)
        elif data < root.data:
            root.left = self.insert(root.left,data)
        elif data > root.data:
            root.right = self.insert(root.right,data)
        return root
    
    def remove(self,arg,data):
        cur = arg
        if self.search(data):
            if data<cur.data:
                cur.left = self.remove(cur.left,data)
            elif data>cur.data:
                cur.right = self.remove(cur.right,data)
            else:
                if cur.right and cur.left:
                    temp = self.find_min(cur.right)
                    cur = temp
                    self.remove(cur.right,temp)
                elif cur.right==None and cur.left == None:
                    cur = None
                elif cur.right==None:
                    cur = cur.left
                elif cur.left == None:
                    cur = cur.right
        else:
            return self
        
    def search(self,data):
        cur = self.root
        while(cur):
            if(cur.data>data):
                cur = cur.left
            elif cur.data<data:
                cur = cur.right
            else:
                return True
        return False
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self
    
    def find_min(self,root):
        if self.left:
            return self.left.find_min()
        else:
            return self
    
    def preordertraversal(self,root):
        cur = root
        if cur:
            print(cur.data,end='->')
            self.preordertraversal(cur.left)
            self.preordertraversal(cur.right)
            
    def inordertraversal(self,root):
        cur = root
        if cur:
            self.inordertraversal(cur.left)
            print(cur.data,end='->')
            self.inordertraversal(cur.right)
            
    def postordertraversal(self,root):
        cur = root
        if cur:
            self.postordertraversal(cur.left)
            self.postordertraversal(cur.right)
            print(cur.data,end='->')
            
    def layer_order(self):#借助于队列来实现,借助其先入先出的思想
        """二叉树的层次遍历即从上往下、从左至右依次打印树的节点"""
        if self.root == None:
            return
        queue = []
        queue.append(self)#将整棵树入队列
        while queue:
            now_node = queue.pop(0)#将整棵树出队列
            print(now_node.data)#输出树的根节点
            if now_node.left != None:#如果这棵树有左子树，将其左子树入队
                queue.append(now_node.left)
            if now_node.right != None:#将树的右子树入队
                queue.append(now_node.right)  
                
