x = int(input("x="))
a = 2
s = []
for i in range(1 , x+1):
    if x > a and x % a == 0:
        s.append(a)
    a = a + 1
print("answer is",s)