print("inserte un numero:")
a = int(input())
b = True

for x in range(2, a-1):
    if a % x == 0:
        b = False
        break
    else:
        continue
if b == True:
    print("Es primo")
else:
    print("No es primo")

