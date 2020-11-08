class Node:
    def __init__(self,data):
        self.data=data
        self.left=self.right=None
class BST:
    def __init__(self):
        self.root=None
    def insert(self,data):
        self.root=self._insert(self.root,data)
        #print(self.root.data)
        return self.root is not None
    def _insert(self,node,val):
        if node is None:#노드가 완전 비어 있을 때
            node=Node(val)#처음 들어온 값이 root가 됨.
        else:
            if val<=node.data:
                node.left=self._insert(node.left,val)
            else:
                node.right=self._insert(node.right,val)
        return node
    def find(self,key):
        return self._find(self.root,key)
    def _find(self,node,key):
        if node is None or node.data==key:
            return node is not None
        elif key<node.data:
            return self._find(node.left,key)
        else:
            return self._find(node.right,key)
    def delete(self,target):
        return self.deleteNode(self.root,target)

    def deleteNode(self, cur, target):
        # base case
        if not cur:
            return None
        elif target < cur.data:
            cur.left = self.deleteNode(cur.left, target)
        elif target > cur.data:
            cur.right = self.deleteNode(cur.right, target)
        else :
            # 1. 삭제노드가 리프노드인 경우
            if not cur.left and not cur.right:
                cur = None

            #2. 삭제노드의 자식이 하나 일 때
            # 오른쪽 자식이 있는 경우
            elif not cur.left:
                cur = cur.right
            elif not cur.right :
                cur = cur.left

            else:
                # 대체 노드를 찾는다
                rep = cur.left
                while rep.right:
                    rep=rep.right
                    # 삭제 노드와 대체 노드의 키를 교환
                    cur.data, rep.data = rep.data, cur.data

                    cur.left = self.deleteNode(cur.left, rep.data)
        return cur

    
bst=BST()
arr=[27,14,35,10,19,31,42,31,40,45,36,37,38]
for i in arr:
    bst.insert(i)

print(bst.find(10))
print(bst.delete(10))#True가 나오면 지우려는 값이 트리에 있다는 뜻
print(bst.find(10))

