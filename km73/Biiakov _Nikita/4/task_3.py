x = int(input("Введіть x:"))
y = int(input("Введіть y:"))
z = int(input("Введіть z:"))
if x>=y > z:
    answer=z
elif y>x > z:
    answer=z
elif x>=z > y:
    answer=y
elif z>x > y:
    answer=y
else:
    answer=x
print("Найменше число:",answer)
input()
