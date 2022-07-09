from cgi import print_directory
import math
import re
import datetime
import webbrowser
import time 
from time import strftime
import os
from playsound import playsound

# # padrao = r"^\d*\s+"
# # padrao2 = r"\s+\d*$"
# # texto = '25 gas+gdsa 43'
# # regex = re.findall(padrao, texto)
# # regex2 = re.findall(padrao2, texto)
# # convert = list(map(int, regex))
# # convert2 = list(map(int, regex2))
# # # sum = list(map(sum, convert, convert2))
# # print(convert, convert2)
# # soma = convert + convert2
# # print(math.prod(soma))
# # sinal = r"\+"
# # regex3 = re.findall(sinal, texto)
# # print(regex3)

# # def padrao_sinal(texto):
# #     padrao_sinal = r"[\+|\-|\*|\/]"
# #     regex_sinal = re.findall(padrao_sinal, texto)
# #     string = "".join(regex_sinal)
# #     return string

# # print(padrao_sinal('/'))


# # padrao0 = r"\s*\d+$"
# # padrao1 = r"^\d+\s*"
# # regex0 = re.findall(padrao1, '6531 *8')
# # print(list(map(int, regex0)))

# lista = [36]
# lista2 = [54]
# s = [str(integer) for integer in lista]
# a_string = "".join(s)
# res = int(a_string)

# print(type(res))


# def alarmYT():
#     # # return print(strftime("%I:%M"))
#     horario = strftime('%I:%M')
#     while True:
#         horario = strftime('%I:%M')
#         time.sleep(5)
#         print(horario)
#         if horario == "04:":
#             webbrowser.open('https://www.youtube.com/watch?v=60ItHLz5WEA')
#             return False



# if __name__ == '__main__':
#     alarmYT()

def temporizador():
    segundos = 10
    while True:
        tempo = datetime.timedelta(seconds = segundos)
        segundos -= 1
        time.sleep(1)
        print(tempo)
        if segundos == 0:
            print('acabou o tempo!! tocarei uma musica \O/')
            playsound(os.getcwd() +'\projetosIniciantes\musica.mp3')
            return False

if __name__ == '__main__':
    temporizador()

# directory = os.getcwd()
# print_directory()

# playsound(os.getcwd() + '\projetosIniciantes\musica.mp3')
# C:\Users\vicas\projetosInteressantes\projetosIniciantes