print("число вводимых чисел")
n = int(input ())
k=0
for i in range(0,n,1):
    m = int(input ())
    if m==0:
        k=k+1
print("0=",k)
