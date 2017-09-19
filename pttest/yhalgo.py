# -*- coding: utf-8 -*-
#
# a=[1,1,2,2,3,3,5,5,4,4,4]
#
# temp =a[0]
# for i in range(1,len(a)):
#     temp = temp ^ a[i]
#
# print temp
def bag(n,c,w,v):
    res=[[-1 for j in range(c+1)] for i in range(n+1)]
    for j in range(c+1):
        res[0][j]=0
    for i in range(1,n+1):
        for j in range(1,c+1):
            res[i][j]=res[i-1][j]
            if j>=w[i-1] and res[i][j]<res[i-1][j-w[i-1]]+v[i-1]:
                res[i][j]=res[i-1][j-w[i-1]]+v[i-1]
    return res

def f(n,w,p=[2,2,6,5,4],g=[6,3,5,4,6]):
    # if i ==0 or w==0:
    #     return 0
    if n<=1 and w<p[0]:
        return 0
    elif n==1 and w>=p[0]:
        return g[0]
    elif n>1 and w<p[n-1]:
        return f(n-1,w)
    else:
        return max(f(n-1,w),f(n-1,w-p[n-1])+g[n-1])


def show(n,c,w,res):
    print('最大价值为:',res[n][c])
    x=[False for i in range(n)]
    j=c
    for i in range(1,n+1):
        if res[i][j]>res[i-1][j]:
            x[i-1]=True
            j-=w[i-1]
    print('选择的物品为:')
    for i in range(n):
        if x[i]:
            print'第',i,'个,'



if __name__=='__main__':

    n=5  # n=5是物品的数量，
    c=10  # c=10是书包能承受的重量
    w=[2,2,6,5,4]  # w=[2,2,6,5,4]是每个物品的重量
    v=[6,3,5,4,6]  # v=[6,3,5,4,6]是每个物品的价值
    res=bag(n,c,w,v)
    print res
    print f(5,10)
    show(n,c,w,res)
    
