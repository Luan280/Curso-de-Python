from time import sleep


def maior(*valores):
    print("Analisando os valores passados.......")
    total = 0
    for n in valores:
        if n > total:
            total = n
        print(f"{n}", end=" ")
        sleep(0.5)
    print(f"Foram informados {len(valores)} valores ao todo.")
    print(f"O maior valor informado foi {total}.")
    print("-=" * 30)


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
