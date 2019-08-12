def BinarySearch(nums,x):
    if not nums:
        return 
    l,r = 0,len(nums)-1
    while(l<=r):
        mid = (l+r)//2
        if nums[mid]<x:
            l = mid+1
        elif nums[mid]>x:
            r = mid-1
        else:
            return mid
    return -1
    
nums=[10,9,8,7,6,5,4,3,2,1]
BinarySearch(nums,6)

def mysqrt(x):
    r = x
    while r*r>x:
        r = int((r+x/r)/2)
    return r
mysqrt(100)

def partition(nums,left,right):
    pivot = nums[left]
    while(left<right):
        while(left<right and nums[right]>pivot): 
            right -= 1
        while(left<right and nums[left]<pivot): 
            left += 1
        nums[left] , nums[right] = nums[right] , nums[left]
        
    nums[left] = pivot
    return left
   
def Find(Array,left,right,k):
        index = partition(Array,left,right)
        if(index == k):
            return Array[index]
        elif(index < k):
            return Find(Array,index+1,right,k)
        else:
            return Find(Array,left,index-1,k)

pai = [10,9,8,7,6,5]
 
print(Find(pai,0,len(pai)-1,0))
