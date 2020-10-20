def fibonacci(num):
    if num <= 1:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)
x = int(input("Digite um número para calcular o Fibonacci:"))
res = fibonacci (x-1)
print("O Fibonacci de %d e %d" % (x, res))
