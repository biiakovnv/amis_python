n = int(input("Введіть довжину: "))
m = int(input("Введіть ширину: "))
k = int(input("Введіть кількість шматків,яку ви хочете відрізати: "))
if (((k % n) == 0) or ((k % m) == 0)) & ((m * n) >= k):
    print("YES")
else:
    print("NO")
input()
