# /bin/env python
# -*- encode: utf-8 -*-
__author__ = '@MauriSudario'

def ex01():
    """Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também
    se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.
Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes. """

string_1 = input("Digite a primeira string: ")
string_2 = input("Digite a segunda string: ")
tamanho_str_1 =(string_1)
tamanho_str_2 =(string_2)
print(string_1 + " " + str(tamanho_str_1))
print(string_2 + " " + str(tamanho_str_2))


def ex02():
    """Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário
     de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário
     pode digitar letras maiúsculas ou minúsculas."""

nome = input('Digite seu nome: ')
print (nome.upper () [::-1])

def ex03():
    """Faça um programa que solicite o nome do usuário e imprima-o na vertical."""

nome = input('Digite seu nome: ')
for i in nome:
    print(str.upper(i))

def ex04():
    """Modifique o programa anterior de forma a mostrar o nome em formato de escada."""

nome = str(input('Digite o seu nome: ')).upper()
for i in range(0, len(nome)+1):
    print(nome[:i])


def ex05():
    """Altere o programa anterior de modo que a escada seja invertida."""

nome = input('Digite o seu nome: ')
for i in range(0, len(nome)-1)
while(contador > 0):
    print(nome[0:contador])
    contador = contador – 1

def ex06():
    """Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o
    nome do mês por extenso."""

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
'Outubro', 'Novembro', 'Dezembro']

dia, mes, ano = input('Escreva a data de nascimento no formato DD/MM/AAAA: ').split('/')

print('Você nasceu no dia {} de {} de {}'.format(dia, meses[int(mes)-1], ano))

def ex07():
    """Dado uma string com uma frase informada pelo usuário (incluindo espaços em branco), conte:
quantos espaços em branco existem na frase.
quantas vezes aparecem as vogais a, e, i, o, u."""

frase = input('Digite uma frase: ')

letraA = frase.count('a')
letraE = frase.count('e')
letraI = frase.count('i')
letraO = frase.count('o')
letraU = frase.count('u')
espaco = frase.count(' ')

print('Letra A: {}'.format(letraA))
print('Letra E: {}'.format(letraE))
print('Letra I: {}'.format(letraI))
print('Letra O: {}'.format(letraO))
print('Letra U: {}'.format(letraU))
print('Espaços: {}'.format(espaco))


def ex08():
    """Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da direita para esquerda
     ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. Em textos mais complexos os espaços e pontuação são
     ignorados. A frase SUBI NO ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados.
     Faça um programa que leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não."""

expressao = input('Escreva uma expressão: ').upper().replace(' ', '')
expInv = expressao[::-1]
if expressao == expInv:
    print('É palíndromo, pois, {} --> {}.'.format(expressao, expInv))
else:
    print('Não é palíndromo.')

def ex09():
    """Desenvolva um programa que solicite a digitação de um número de CPF no formato xxx.xxx.xxx-xx
 e indique se é um número válido ou inválido através da validação dos dígitos verificadores e dos caracteres
 de formatação."""

cpf = input('Digite o seu cpf no formato xxx.xxx.xxx-xx: ')
tamCPF = len(cpf)
if tamCPF == 14 and '.' in cpf[3] and '.' in cpf[7] and '-' in cpf[11]:
    print('{} é um CPF válido'.format(cpf))
else:
    print('{} é um CPF inválido.'.format(cpf))

def ex10():
    """Escreva um programa que solicite ao usuário a digitação de um número até 99 e imprima-o na tela
    por extenso."""

converter_em_texto(numeral):
    dicionario_numerico = {
        0: 'zero', 1: 'um', 2: 'dois', 3: 'três', 4: 'quatro', 5: 'cinco',
        6: 'seis', 7: 'sete', 8: 'oito', 9: 'nove', 10: 'dez',
        11: 'onze', 12: 'doze', 13: 'treze', 14: 'quatorze', 15: 'quinze',
        16: 'dezesseis', 17: 'dezessete', 18: 'dezoito', 19: 'dezenove', 20: 'vinte',
        30: 'trinta', 40: 'quarenta', 50: 'cinquenta', 60: 'sessenta', 70: 'setenta',
        80: 'oitenta', 90: 'noventa',
    }

    if numeral > 99 or numeral < 0:
        raise ValueError('O número deve estar entre 0 e 99 (inclusive)')

    if numeral < 20 or numeral % 10 == 0:
        return dicionario_numerico.get(numeral)

    decimal = numeral // 10 * 10
    unidade = numeral % 10
    extenso = f'{dicionario_numerico.get(decimal)} e {dicionario_numerico.get(unidade)}'
    return extenso


if __name__ == '__main__':
    print('Insira um número:')
    numeral = int(input())
    numero_por_extenso = converter_em_texto(numeral)
    print(numero_por_extenso)


def ex11():
    """  Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e
    escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.
Digite uma letra: A
-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O
A palavra é: _ _ _ _ O

Digite uma letra: E
A palavra é: _ E _ _ O

Digite uma letra: S

-> Você errou pela 2ª vez. Tente de novo!"""

import random


def print_forca(forca):
    print(' '.join(forca).upper())
    print('')


palavras = ['programa', 'arquivo', 'texto', 'aleatoriamente', 'jogador', 'enforcado']
palavra = random.choice(palavras)
forca = ['_' for i in range(len(palavra))]
erros = 0
ganhou = False

while erros < 6 and not ganhou:
    print_forca(forca)
    print('Digite uma letra:')
    chute = str(input()).lower()

    if chute not in palavra:
        erros += 1
        print(f'Você errou pela {erros}a vez. Tente de novo!')
        continue

    for index, letra in enumerate(palavra):
        if letra == chute:
            forca[index] = chute

    if '_' not in forca:
        ganhou = True

if ganhou:
    print('You win!')
else:
    print('Game over!')
print_forca(forca)

def ex12():
    """ Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos,
     acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador."""

def corrigir_telefone(telefone, formatar=True):
    telefone_sem_hifen = telefone.replace('-', '')
    qtd_caracteres = len(telefone_sem_hifen)
    telefone_corrigido = telefone_sem_hifen

    if qtd_caracteres < 8:
        print(f'Telefone possui {qtd_caracteres} dígitos. Vou acrescentar o digito três na frente.')
        caracteres_faltantes = 8 - qtd_caracteres
        telefone_corrigido = caracteres_faltantes * '3' + telefone_sem_hifen

    if formatar:
        telefone_corrigido = telefone_corrigido[0:4] + '-' + telefone_corrigido[4:8]

    return telefone_corrigido


if __name__ == '__main__':
    print('Valida e corrige número de telefone:')
    print('Telefone:')
    telefone = str(input())

    print('Telefone corrigido sem formatação:', corrigir_telefone(telefone, formatar=False))
    print('Telefone corrigido com formatação:', corrigir_telefone(telefone))
