n=int(input())
list_a=[]
list_ans=[]
for i in range(n):
 list_a.append(list(map(int,list(input().split()))))
#print(list_a)

for i in range(len(list_a)):
  sum = 0
  for  j in range(len(list_a)):
    sum += list_a[j][i]
  list_ans.append(sum)
print(list_ans)
