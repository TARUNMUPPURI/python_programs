given = list(map(int,list(input().split())))
list_a=[]
ans=0
s=1
for i in range(len(given)-1):
  if given[i]<given[i+1]:
    if len(list_a) == 0:
      list_a.append(given[i])
      list_a.append(given[i+1])
    else:
      list_a.append(given[i+1])
    #print(list_a)
    s=sum(list_a) 
    if s>ans:
      ans=sum(list_a)
  else:
    list_a=[]

print(ans)
