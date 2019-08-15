class ListNode:
    def __init__(self, value, pnext=None):
        self.data = value
        self.next = pnext
        
class HashTable:
    '''
    选用除留余数法作为哈希函数
    选用链地址法处理冲突，链表结构为带头结点的单链表
    新插入的结点采用前插法，因为新插入的结点会更频繁地被访问
    '''
    def __init__(self, p):
        '''
        :param p: 哈希函数的除数
        '''
        self.array = [None] * p
        self._div = p
        
    def hashFun(self, key):
        # 选用除留余数法作为哈希函数
        return key % self._div
    
    def insert(self, value):
        '''
        采用前插法将value作为结点插入到哈希表的链表中，
        若当前链表不存在，则创建一个链表再继续插入该结点
        :param value: 结点的值
        '''
        key = self.hashFun(value)
        if self.array[key] is None:
            self.array[key] = ListNode(None)
            node = ListNode(value)
            self.array[key].next = node
        else:
            node = ListNode(value)
            node.next = self.array[key].next
            self.array[key].next = node
    
    def showTable(self):
        for index in range(self._div):
            if self.array[index]:
                p = self.array[index].next
                print('%d：' % index)
                while p:
                    print(p.data,end='—>')
                    p = p.next
                print('\n')
ht = HashTable(10)
ht.insert(4)
ht.insert(14)
ht.insert(3)
ht.insert(2)
ht.showTable()

class ListNode:
    def __init__(self, key=None, value=None, pnext=None, ppre=None):
        self.key = key
        self.value = value
        self.next = pnext
        self.pre = ppre
        
'''
使用哈希链表实现LRU算法
链表为带头结点的双向链表
链表尾结点为最近访问的结点
'''
class LruCache:
    
    def __init__(self, capacity=5):         # 缓冲区容量默认为5
        self.cache = dict()
        self.size = 0
        self.capacity = capacity
        self.head = ListNode()
        self.end = self.head
        
    def get(self, key):
        node = self.cache.get(key)
        if node is None:
            return
        else:
            self._refreshNode(node)
        return node.value
    
    def put(self, key, value):
        node = self.cache.get(key)
        if node is None:                  
         # 当该结点不存在于缓冲区，则加入缓冲区
            self._addNode(key, value)
        else:                              
        # 当该结点存在于缓冲区，则更新结点和其在缓冲区的位置
            node.value = value
            self._refreshNode(node)
    
    def remove(self, key):
        node = self.cache.get(key)
        if node is None:
            return
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
        self.size -= 1
        
    def _addNode(self, key, value):
        if self.capacity == self.size:        # 若缓冲区容量已满，则删除头结点
            self.head = self.head.next
            
        # 将结点作为尾结点加入缓冲区   
        newNode = ListNode(key, value, ppre=self.end) 
        self.end.next = newNode
        self.end = newNode
        self.cache[key] = newNode
        self.size += 1
    
    def _refreshNode(self, node):
        # 更新结点的位置
        node.pre.next = node.next
        node.next.pre = node.pre
        self.end.next = node
        node.pre = self.end
        self.end = node
        node.next = None
        
class Trie:
    def __init__(self):
        self.root = {}
        self.end_with = -1
        
    def insert(self,word):
        curNode = self.root
        for c in word:
            if c not in curNode:
                curNode[c] = {}
            curNode = curNode[c]
        curNode[self.end_with] = True
        
    def search(self,word):
        curNode = self.root
        for c in word:
            if c not in curNode:
                return False
            curNode = curNode[c]
            
        if self.end_with not in curNode:
            return False
        return True
    
    def start_with(self,prefix):
        curNode = self.root
        for c in prefix:
            if c not in curNode:
                return False
            curNode = curNode[c]
        return True
        
def naive_match(s,p):
    m,n = len(s),len(p)
    for i in range(m-n+1):
        if s[i:i+n] == p:
            return True
    return False
