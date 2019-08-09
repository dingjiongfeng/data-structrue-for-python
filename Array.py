class Array:
    def __init__(self,capacity=10):
        self.capacity = capacity #数组的大小
        self.size = 0 #已使用的大小
        self.data = [None] * capacity   
        
    def add(self,index,item):
        if (index<0 or index>self.size):
            print("非法操作！")
            return 
        #满了
        if (self.size == self.capacity):
            self.resize(self.capacity * 2)
        #移动元素
        for i in range(self.size-1, index-1, -1):
            self.data[i+1] = self.data[i]
        self.data[index] = item
        self.size += 1
        
    def resize(self,capacity):
        temp = Array(capacity)
        for i in range(self.size):
            temp.add(i,self.data[i])
        self.data = temp.data
        self.capacity = capacity
    
    def print(self):
        for i in range(self.size):
            print(self.data[i],end='\t')
           
if __name__ == '__main__':
  arr = Array(9)
  arr.add(0,1)
  arr.data
  arr.resize(18)
  arr.data
  arr.add(1,3)
  arr.print()
