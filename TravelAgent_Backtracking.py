import copy
import math
n=4 #城市个数
dnode=[[0,2,6,7],    #各结点间距离二维矩阵
       [2,0,4,4],
       [6,4,0,2],
       [7,4,2,0]]
osquence=[0]*(n+1) #最优路线
ovalue=math.inf    #最优值 默认最大
branch=1           #分支计数
ngnode=[0]*(n+1)   #已走结点初值
def TSP(cnode,gnode,order):  #cnode当前所在结点  gnode已走结点 order次序（用于代表当前分支已经经过结点的数量）
    gnode[cnode]=order                  #每经过一个结点给列表中对应结点赋次序
    global ovalue
    global branch
    global osquence
    if order==n+1:                      #满足条件代表已经回到出发点，这一分支结束，并回溯
        cvalue=0
        gnode[n] = gnode[n] - n  # 将尾值和初值一样
        for i in range(4):             #通过gnode得到的经过结点的步骤顺序根据dnode计算距离总和
            cvalue+=dnode[gnode[i]-1][gnode[i+1]-1]
        if cvalue<ovalue:               #判断是否为更优值，并覆盖
            ovalue=cvalue
            osquence=copy.deepcopy(gnode)
        print("分支:"+str(branch)+"\t路线："+str(gnode)+"\t距离成本:"+str(cvalue))
        branch+=1                      #分支+1用于下一次
    else:
        for i in range(1,n+1):
            if gnode[i]==0 and (i<n or i==order):  #判断已走结点为0的部分代表还未走过， 附加条件保证不会提前执行回到原点的步骤
                TSP(i,copy.deepcopy(gnode),order+1)
TSP(0,copy.deepcopy(ngnode),1)
print("\n最优线路:路线："+str(osquence)+"\t距离成本:"+str(ovalue))