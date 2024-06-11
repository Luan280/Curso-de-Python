count = 3
termos = int(input("Quantos termos você mostrar?: "))

t1 = 0
t2 = 1

print(f"{t1} - {t2}", end=" ")
while count <= termos:
    count += 1
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    print("-", t3, end=' ')
print("-FIM!")
