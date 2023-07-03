print("Введите целое число ")
b = int(input ())
c=b%2
if c==0:
    print("число является четным")
else:
    print("число не является четным")
if b==0:
    print("нулевое число")
elif b>0 and c==0:
    print("положительное четное")
elif b>0 and c!=0:
    print("положительное нечетное")
elif b<0 and c==0:
    print("отрицательное четное")
elif b>0 and c!=0:
    print("отрицательное нечетное")


