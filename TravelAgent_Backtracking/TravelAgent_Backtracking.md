# 用Python实现旅行商问题

### 问题描述：

&emsp;&emsp;有一个旅行商由某市出发，经过所有给定的n个城市后，再回到出发的城市。除了出发的城市外，其它城市只经过一回。这样的回路可能有多个，求其中路径成本最小的回路。

### 问题分析：

&emsp;&emsp;假设城市数量n=4，V={A,B,C,D}，设出发城市为A，问题的解空间为{A→{B，C，D三者的全排列}→A}，列出所有可能路线

![image](./image/Path%20Map.png)

![image](./image/Branch%20tree(1).png)

### 基本算法：回溯法

### 算法分析：

1、核心运算在每个节点处计算路径长度对由n个城市形成的全排列树来说，所含的结点数目为：1+(n-1)+(n-1)(n-2)+ (n-1)(n-2) (n-3) +……+((n-1)(n-2)……2)+(n-1)!

2、运行时间函数T(n) =1 + (n-1)!×(1/(n−2)!+1/(n−3)!+⋯+1/2+1)                            ≤1 + (n-1)!×(1/2^n−3+1/2^n−4+⋯+1/2+1)                                ≤1+2(n-1)!

3、渐进运行时间函数取T*(n)=2(n-1)!=O((n-1)!)，阶为(n-1)!

### 实现思路：

### &emsp;&emsp;用递归的方式列出所有的分支，并通过建立一个` gnode`列表用来记录分支的结点路线并且在运行过程中用来记录已走结点保证不会出现重复；`order`主要用于统计当前分支已走结点个数并用作（递归结束）回溯条件的判定；

### 当前分支的路线总距离在递归结束阶段用`cvalue`存储通过for循环用`gnode`和`dnode`得到路线与路线之间距离并累加，并判断是否为最优值。

### 代码实现：

``` python
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
```

### 结束感悟：

&emsp;&emsp;这个算法的学习是从学校课程内容《算法分析与设计》中学到的，老师跟我们讲述了什么是回溯法，以及它的大体思路，课后需要用python自行实现。

&emsp;&emsp;当时为了编写这个代码参考了好多资料找取灵感，最后还是打算尝试用递归的方式去进行深度优先遍历把每一条分支给列出来，其中在计算分支路径总长度的时候出现了点问题，一开始考虑的是设一个变量记录每个分支、每次递归的同时累加它各结点的距离，但却出现了总距离计算错误的问题，随后发现原来是每次回溯完后当前结点累加的距离值没有被回溯，造成数值错误。随后，我采用了先计算完一个分支的路线，然后用记录路线的变量来单独重新过程，来累加结点距离，至此该问题就解决了。