class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Linkedlist:
    def __init__(self):
        self._size = 0
        self.head = None
        
    def isEmpty(self):
        return self._size == 0
    
    def add(self,node):
        if not self.head:
            self.head = node
            self._size += 1
        
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
            self._size += 1
            
    def delete(self,index):
        if not self.isEmpty():
            print("error")
            return
        
        if (index<0 or index>=self._size):
            print("index error")
            return 
        
        if index == 0:
            self.haed = self.head.next
            self._size -= 1
            
        j = 0
        prev = self.head
        node = self.head
        while node.next and j < index:
            prev = node
            node = node.next
            j += 1
            
        if  j == index:
            prev.next = node.next
            self._size -= 1
            
    def update(self,index,element):
        if index<0 or index>=self._size:
            print("index error")
            return 
        node  = self.head
        for i in range(index):
            node = node.next
        node.data = element.data
        
    def getItem(self,index):
        if self.isEmpty():
            print("no elements")
            return 
        if index<0 or index>=self._size:
            print("index error")
            return 
        else:
            node  = self.head
            for i in range(index):
                node = node.next
            return node.data
    
    def getIndex(self,data):
        if self.isEmpty():
            print("no elements")
            return 
        
        j = 0
        node  = self.head
        while node:
            if node.data == data:
                return j
            node = node.next
            j += 1
        return "no such element"
    
    def insert(self, index, data):
        if index<0 or index>=self._size:
            print("index error")
            return 
        
        if index == 0:
            data.next = self.head
            self.head = data
            self._size += 1
            
        j = 0
        prev = self.head
        node = self.head
        while node.next and j < index:
            prev = node
            node = node.next
            j += 1
            
        if  j == index:
            data.next = node
            prev.next = data
            self._size += 1
            
    def print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next
            
class CycleSingleLinkList:
    def __init__(self,node=None):
        self.head = node
        
    def isEmpty(self):
        return self.head is None
    
    def length(self):
        if self.isEmpty():
            return 0
        
        j = 1
        current = self.head
        while current.next != self.head:
            j += 1
            current = current.next
        return j
        
    def add(self,data): #头部添加
        node1 = node(data)
        if self.isEmpty():
            self.head = node1
            node1.next = node1
        
        else:
            temp = self.head
            while temp.next!=self.head:
                temp = temp.next
            temp.next = node1
            node1.next = self.head
            node1 = self.head
        
    def append(self,data): #尾部添加
        node1 = node(data)
        if self.isEmpty():
            self.head = node1
            node1.next = node1
        
        else:
            temp = self.head
            while temp.next!=self.head:
                temp = temp.next
                
            node1.next = self.head
            temp.next = node1
            
    def delete(self,item):
        if not self.isEmpty():
            print("error")
            return
            
        cur = self.head
        pre = None
        while cur.next != self.head:
            pre = cur
            cur = cur.next
            if cur.data == item:
                pre.next = cur.next
    
    def search(self,data):
        if self.isEmpty():
            print("no elements")
            return 
        
        node  = self.head
        while node.next != self.head:
            if node.data == data:
                return True
            node = node.next
        if node.data == data:
            return True
        return False
    
    def insert(self, index, data):
        if index < 0:
            self.add(data)
        if index >= self.length():
            self.append(data)
            
        cur = self.head
        count = 0
        while count < index-1: #前一个位置
            count += 1
            cur = cur.next
        node = node(data)
        node.next = cur.next
        cur.next = node
            
    def print(self):
        if self.isEmpty():
            print("空")
            return 
        node = self.head
        while node!=self.head:
            print(node.data)
            node = node.next
        print(node.data)
