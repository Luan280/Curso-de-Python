n = int(input('Digite um número: '))
total = 0
for c in range(1, n + 1):
    if n % c == 0:
        print("\033[33m", end=" ")
        total += 1
    else:
        print("\033[m", end=" ")
    print("{}".format(c), end=" ")

if total == 2:
    print("\nEle é primo!")
else:
    print("\nEle NÃO é PRIMO!!")