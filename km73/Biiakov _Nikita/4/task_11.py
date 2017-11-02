x = int(input("Введіть x:"))
y = int(input("Введіть y:"))
a = int(input("Введіть a:"))
b = int(input("Введіть b:"))
import math
del1 = abs(x - a)
del2 = abs(y - b)
if x<1 or x>8 or y<1 or y>8 or a<1 or a>8 or b<1 or b>8:
    print("Введіть ще раз")
elif((del1 == 2) & (del2 == 1)) or ((del1 == 1) & (del2 == 2)) :
    print("Yes")
else:
    print("No")
input()
