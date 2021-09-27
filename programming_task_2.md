Strange Numbers: Given a number as a String N. Multiply all of its digits,
and repeat the same with the product obtained till the product consists of 
only one digit. Output the number of steps taken to do so. 

use while loop to determine if the result is <10
use string code in order to separate numbers
keep doing so until it is <10


N = input()
mut=1
t=0
s=0
while t=>10:
  for l in N:
  mut *= int(l)
  t+=1
print(t)
      
  
