print("дите число")
x=int(input())
a=0
for b in range(1, x+1):
    if x%b==0:
        a=a+1
print ("число делителей=",a)
