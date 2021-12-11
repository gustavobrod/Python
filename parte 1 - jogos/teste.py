'''
idade1 = 10
idade2 = "20"
print(idade1 + idade2)
'''

'''
nome = "Nico"
sobrenome = "Steppat"
print(nome + sobrenome)
'''

idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if(idade > 18):
    print("Você é maior de idade.")
else:
    if(idade < 12):
        print("Você é uma criança.")
    elif(idade > 12):
        print("Você é um adolescente.")
