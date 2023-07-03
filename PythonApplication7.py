print("Введите  минимальную сумму инвестиции")
min = int(input ())
print("Введите  сумму доступную Майклу")
maikl = int(input ())
print("Введите  сумму доступную Ивану")
ivan = int(input ())
if (ivan>=min) and (maikl>=min):
    print(2)
elif (ivan>=min) or (maikl>=min):
    print(1)
else:
    print(0)
