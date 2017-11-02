x = int(input("Введіть рік:"))
if x%4==0 and x%100!=0:    
    print("LEAP")
elif x%400==0:
    print("LEAP")
else:
    print("COMMON")
input()
