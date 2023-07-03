print("Введите слово: ") 
slovo = input() 
a = slovo.count('a') 
e = slovo.count('e') 
i = slovo.count('i') 
o = slovo.count('o') 
u = slovo.count('u') 
y = slovo.count('y') 
if a == 0: 
    print("a = False")
else:
    print("a =",a)
if e == 0: 
    print("e = False")
else:
    print("e =",e)
if i == 0: 
    print("i = False")
else:
    print("i =",i)    
if o == 0: 
    print("o = False")
else:
    print("o =",o)    
if u == 0: 
    print("u = False")
else:
    print("u =",u)    
   
print(f"Гласных: {a + e + i + o + u}") 
print(f"Согласных: {len(slovo) - (a + e + i + o + u)}")
