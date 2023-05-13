tuplas = {"Gustavo", "Alline", "Ana Julia"}
print(tuplas)

my_tuple = tuple(tuplas) #foi necessário converter para imprimir a posição
print(my_tuple[0])
print(my_tuple[1])

print(my_tuple[0:2])

print(len(tuplas)) #quantidade de itens na tupla

print(my_tuple+my_tuple) #somar as tuplas pela conversão
print(my_tuple*7) #multiplicar tuplas pela conversão
print(4 in my_tuple) #verificar existencia de numero nas tuplas pela conversão = False
print("Alline" in my_tuple) #verificar existencia de nome nas tuplas pela conversão = true  
