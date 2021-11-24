N = int(input())
I = int(input())
X = int(input())
Y = int(input())
m=0
n=0
for m in range(I):
  for n in range(I):
    if m+n==I:
      if m*X + n*Y == N:
        print(m)
