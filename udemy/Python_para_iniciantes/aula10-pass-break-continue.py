#break
numero=20
while True:
    numero=numero-1
    print(numero)
    if (numero == 2):
        break

#continue
numero2=10
while True:
    numero2=numero2-1
    if (numero2==4):
        continue
    print(numero2)
    if (numero2==2):
        break

#pass
for x in range(0,5):
    pass