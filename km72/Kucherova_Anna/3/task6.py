a = int(input("Кількість учнів першої групи a = "))
b = int(input("Кількість учнів другої групи b = "))
c = int(input("Кількість учнів третьої групи c = "))

print("Необхідна кількість столів N =", a//2+a%2+b//2+b%2+c//2+c%2)
