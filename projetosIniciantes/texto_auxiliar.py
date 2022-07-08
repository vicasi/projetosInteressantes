import math
import re

# padrao = r"^\d*\s+"
# padrao2 = r"\s+\d*$"
# texto = '25 gas+gdsa 43'
# regex = re.findall(padrao, texto)
# regex2 = re.findall(padrao2, texto)
# convert = list(map(int, regex))
# convert2 = list(map(int, regex2))
# # sum = list(map(sum, convert, convert2))
# print(convert, convert2)
# soma = convert + convert2
# print(math.prod(soma))
# sinal = r"\+"
# regex3 = re.findall(sinal, texto)
# print(regex3)

# def padrao_sinal(texto):
#     padrao_sinal = r"[\+|\-|\*|\/]"
#     regex_sinal = re.findall(padrao_sinal, texto)
#     string = "".join(regex_sinal)
#     return string

# print(padrao_sinal('/'))


# padrao0 = r"\s*\d+$"
# padrao1 = r"^\d+\s*"
# regex0 = re.findall(padrao1, '6531 *8')
# print(list(map(int, regex0)))

lista = [36]
lista2 = [54]
s = [str(integer) for integer in lista]
a_string = "".join(s)
res = int(a_string)

print(type(res))