a = input("enter list:").split()
print(sum(a.count(x) - 1 for x in a) // 2)
