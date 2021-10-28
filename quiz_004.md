```.p
def perfectN(N):
  sum = 0
  factors=[]
  for i in range(1,N-1):
    if i%N==0:
      factors.append(i)
      sum += i
  return factors,sum==N
  ```
