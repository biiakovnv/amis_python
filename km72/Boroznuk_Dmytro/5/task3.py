a = [int(s) for s in input("Введіть список чисел: ").split()]
for i in range(len(a)):
    for j in range(len(a)):
        if i != j and a[i] == a[j]:
            break
    else:
        print(a[i])
