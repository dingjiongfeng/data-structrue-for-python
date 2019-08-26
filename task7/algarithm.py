def climb_stair(n):
    if n==1:
        return 1
    if n==2:
        return 2
    return climb_stair(n-1)+climb_stair(n-2)
    
climb_stair(4)

def queen(queen_list, current_column=0):
    
    for row in range(len(queen_list)):
        # 如果已至最后一列，则打印结果，跳出递归
        if current_column == len(queen_list):
            for i in range(len(queen_list)):
                print("(%d, %d)" % (i, queen_list[i]), end=" ")
            print("")
            return 
 
        # 假设当前列能够放置一个皇后，用queen_list的index记录列标，value记录行标
        # flag为可行性的标记
        queen_list[current_column],flag = row,True
        # 对当前列之前的各列进行遍历
        for column in range(current_column):
            # 排除同行及对角线上的位置，将flag设置为False
            if (queen_list[column] == row) or (abs(row - queen_list[column]) == current_column - column):
                flag = False
                # 只要有一个不满足的条件，就跳出遍历
                break
        # 如果可以放置，则递归调用自身，对下一列进行筛选
        if flag:
            queen(queen_list, current_column + 1)
 
queen([None]*8)

bestV=0
curW=0
curV=0
bestx=None
 
def backtrack(i):
    global bestV,curW,curV,x,bestx
    if i>=n:
        if bestV<curV:
            bestV=curV
            bestx=x[:]
    else:
            if curW+w[i]<=c:
                x[i]=True
                curW+=w[i]
                curV+=v[i]
                backtrack(i+1)
                curW-=w[i]
                curV-=v[i]
            x[i]=False
            backtrack(i+1)

if __name__=='__main__':
    n=5
    c=10
    w=[2,2,6,5,4]
    v=[6,3,5,4,6]
    x=[False for i in range(n)]
    backtrack(0)
    print(bestV)
    print(bestx)
    
def InversePairs(data):
        #冒牌排序法，时间复杂度太高，时间复杂度为O（n^2）。采用归并排序的思想,时间复杂度为O（nlogn）
        global count
        count=0
        def A(array):
            global count
            if len(array)<=1:
                return array
            k=int(len(array)/2)
            left=A(array[:k])
            right=A(array[k:])
            l=0
            r=0
            result=[]
            while l<len(left) and r<len(right):
                if left[l]<right[r]:
                    result.append(left[l])
                    l+=1
                else:
                    result.append(right[r])
                    r+=1
                    count+=len(left)-l
            result+=left[l:]
            result+=right[r:]
            return result
        A(data)
        return count
InversePairs([3,2,1,4,6])

def bag(n, c, w, v):
    """
    测试数据：
    n = 6  物品的数量，
    c = 10 书包能承受的重量，
    w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
    v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    """
    # 置零，表示初始状态
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            value[i][j] = value[i - 1][j]
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]
    for x in value:
        print(x)
    return value

def show(n, c, w, value):
    print('最大价值为:', value[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if value[i][j] > value[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('背包中所装物品为:')
    for i in range(n):
        if x[i]:
            print('第', i+1, '个,', end='')

def bag1(n, c, w, v):
    values = [0 for i in range(c+1)]
    for i in range(1, n + 1):
        for j in range(c, 0, -1):
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            if j >= w[i-1]:
                values[j] = max(values[j-w[i-1]]+v[i-1], values[j])
    return values


if __name__ == '__main__':
    n = 6
    c = 10
    w = [2, 2, 3, 1, 5, 2]
    v = [2, 3, 1, 5, 4, 3]
    value = bag(n, c, w, v)
    # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # [0, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    # [0, 0, 3, 3, 5, 5, 5, 5, 5, 5, 5]
    # [0, 0, 3, 3, 5, 5, 5, 6, 6, 6, 6]
    # [0, 5, 5, 8, 8, 10, 10, 10, 11, 11, 11]
    # [0, 5, 5, 8, 8, 10, 10, 10, 12, 12, 14]
    # [0, 5, 5, 8, 8, 11, 11, 13, 13, 13, 15]
    show(n, c, w, value)
    # 最大价值为: 15
    # 背包中所装物品为:
    # 第 2 个,第 4 个,第 5 个,第 6 个,
    print('\n空间复杂度优化为N(c)结果:', bag1(n, c, w, v))
    #空间复杂度优化为N(c)结果: [0, 5, 5, 8, 8, 11, 11, 13, 13, 13, 15]
