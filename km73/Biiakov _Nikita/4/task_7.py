x = int(input("Введіть х:"))
y = int(input("Введіть y:"))
a = int(input("Введіть a:"))
b = int(input("Введіть b:"))
if x<1 or x>8 or y<1 or y>8 or a<1 or a>8 or b<1 or b>8:
    print("Введіть ще раз:")
elif (x+y)%2==0 and (a+b)%2==0:
    print("YES")
elif (x+y)%2!=0 and (a+b)%2!=0:
    print("YES")
else:
    print("NO")
input()
