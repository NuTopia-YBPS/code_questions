class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def getHeight(self,root):
        
        def search_height(n, head):
            
            # If head is at an end node
            if not head:
                return n
            
            # If on a intermediate node
            left_val = search_height(n + 1, head.left)
            right_val = search_height(n + 1, head.right)
            
            # returning the max branches found
            if left_val >= right_val: return left_val
            else : return right_val

        #return search_height(0, root) - 1


if __name__ == "__main__":
    T=int(input())
    myTree=Solution()
    root=None
    for i in range(T):
        data=int(input())
        root=myTree.insert(root,data)
    height=myTree.getHeight(root)
    print(height)      