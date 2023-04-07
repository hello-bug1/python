import heapq
# 物品信息
weight=[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
value=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
print("物品信息如下：")
print("重量：")
print(weight)
print("价值：")
print(value)
# 背包容量
maxcap=35
print("最大背包容量为：%d\n"%maxcap)
n=len(weight)
# 当前重量与当前价值
cweight=0
cvalue=0
# 最优价值
bestv=0
bests=[]
num=0
heap=[]
heapq.heapify
# 上界函数：计算当前结点下的价值上界
def maxbound(i):
	global cweight
	global cvalue
	global n
	global weight
	global value
	global maxcap
	left = maxcap-cweight
	b=cvalue
	while i<n and weight[i]<=left:
		left-=weight[i]
		b+=value[i]
		i+=1
	if i<n:
		b+=(value[i]/weight[i])*left
	return b
# 分支限界算法求解01背包
i=0
upper=maxbound(i)
str=''
while(1):
	wt=cweight+weight[i]
	#print("wt:")
	#print(wt)
	if wt<=maxcap:
		if cvalue+value[i]>bestv:
			#print("i=%d"%i)
			bestv=cvalue+value[i]
			#print("bestv=%d"%bestv)
			# 存储当前最优值的最优路径
			bests=str+'1'
			bests=bests+'0'*(n-len(bests))
		# 入堆： 由于python只有小根堆，因此通过对上界值取倒，实现上界值大，优先级高                         
		if i+1<n:
			heapq.heappush(heap,[1/upper,cweight+weight[i],cvalue+value[i],i+1,str+'1'])
	upper=maxbound(i+1)
	if upper>=bestv:
		if i+1<n:
			heapq.heappush(heap,[1/upper,cweight,cvalue,i+1,str+'0'])
	if len(heap)==0:
		print("%d个物品的状态（1为被装入背包，0为未被装入背包）：%s"%(n,bests))
		print("最优价值为： %d"%bestv)
		break
	#print("heap:")
	#print(heap)
	node=heapq.heappop(heap)
	upper=1/node[0]
	cweight=node[1]
	cvalue=node[2]
	i=node[3]
	str=node[4]
	#print('node:')
	#print(node)

