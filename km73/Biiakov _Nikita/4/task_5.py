x = int(input("Введіть х:"))
y = int(input("Введіть у:"))
z = int(input("Введіть z:"))
if x == y == z:
    print(3)
elif y==x and x!=z:
    print(2)
elif y!=x and x==z:
    print(2)
elif x!=y and y==z:
    print(2)
elif x!=y!=z:
    print(0)
input()
