lista=[1, 4, 7, "Gustavo", 23, 14]
print(lista)

lista.append("python") #adiciona item a lista
print(lista)

lista.append(100) #adiciona item a lista
print(lista)

print(lista.index("Gustavo")) #saber posição do item na lista

print(lista.count(4)) #contar quantos item 4 tem na lista

lista.remove("Gustavo") #remove item da lista
print(lista)

lista.reverse() #inverter posição da lista
print(lista)

lista2 = [5, 9, 6, 1, 10, 7, 2]
lista2.sort() #sort
print(lista2)
