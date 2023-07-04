
print("число начальное число")
a = int(input ())
print("число конечное число")
b = int(input ())
for i in range(a,b+1,1):
    if i%2==0:
        print(i, end=' ')