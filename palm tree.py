def dfs(g,i,h,maxv):
    h+=1
    maxv=h if h>maxv else maxv
    if len(g[i])>0:
        for j in g[i]:
            maxvar=dfs(g,j,h,maxv)
            maxv = maxvar if maxvar > maxv else maxv
    else:
        return maxv
    return maxv

g=dict()
# g={0:[1,2,3],1:[4,5],2:[6],3:[],4:[],5:[],6:[]}
n=1000
for i in range(n):
    g[i]=[i+1]
g[n]=[]
print(g)
# maxv=dfs(g,0,0,0)
# print(maxv)
stack = []
stack.append([0,1])
maxv=0
while stack:
    v=stack.pop()
    maxv=v[1] if v[1]>maxv else maxv
    for i in g[v[0]]:
        stack.append([i,v[1]+1])
print(maxv)