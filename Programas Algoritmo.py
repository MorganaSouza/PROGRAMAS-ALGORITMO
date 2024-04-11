# Programa 1
num_int1 = int(input("Digite o primeiro número inteiro: "))
num_int2 = int(input("Digite o segundo número inteiro: "))
num_real = float(input("Digite um número real: "))

resultado_a = (2 * num_int1) * (num_int2 / 2)
resultado_b = (3 * num_int1) + num_real
cubo_num_real = num_real ** 3

print("a) O produto do dobro do primeiro com metade do segundo:", resultado_a)
print("b) A soma do triplo do primeiro com o terceiro:", resultado_b, "o terceiro elevado ao cubo:", cubo_num_real)

# Programa 2
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O maior número é:", num1)
elif num2 > num1:
    print("O maior número é:", num2)
else:
    print("Os números são iguais.")

# Programa 3
valor = float(input("Digite um valor: "))

if valor > 0:
    print("O valor é positivo.")
elif valor < 0:
    print("O valor é negativo.")
else:
    print("O valor é zero.")

# Programa 4
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 7.0:
    print("Aprovado")
else:
    print("Reprovado")

# Programa 5
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
    print("O maior número é:", num1)
elif num2 > num1 and num2 > num3:
    print("O maior número é:", num2)
elif num3 > num1 and num3 > num2:
    print("O maior número é:", num3)
else:
    print("Há números iguais.")
