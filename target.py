
'''
#Ex 1

Após as iterações, o valor da variável SOMA é de 91.
'''




# Ex 2
def verifica_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    if b == numero:
        return True
    else:
        return False


numero = int(input("Digite umn número para verificar se pertence à sequencia de Fibonacci: \n"))
if verifica_fibonacci(numero):
    print(f'O número {numero} pertence à sequência de Fibonacci.\n')
else:
    print(f'O numero {numero} não pertence à sequência de Fibonacci.\n')


#Ex 3
'''
A) 1,3,5,7, 9 (numeros ímpares)

B)2,4,8,16,32,64, 128 (potencias de 2)

C) 0, 1, 4, 9, 16, 25, 36, 49 (quadrados perfeitos)

D) 4, 16, 36, 64 , 256 (4 elevado a potencias cujo o numero é o indice, 256 é 4^5)

E) 1,1,2,3,5,8, 13 (Fibonacci)

F) 2,10,12,16,17,18,19, 200(todos os numeros começam com a letra D)

'''



# EX 4
''' 
ligaria o primeiro interruptor, esperaria 30s
então desligaria o primeiro e ligaria o segundo, iria ate onde esta a lampada desligada.
se estiver fria, então é do terceiro interruptor.
se estiver quente, então é do primeiro.
e a luz acesa é do segundo.

'''


#Ex 5
palavra = input("Digite uma palavra para ser invertida: ")
palavra_invetida = palavra[::-1]
print(f'\nEsta é a palavra original: {palavra}, e aqui está ela com os caracteres invertidos: {palavra_invetida}')