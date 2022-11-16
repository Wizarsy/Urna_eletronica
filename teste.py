#coding=UTF-8
from graphics import *
from pygame import mixer
import datetime
import time

'''//////////GLOBAL///////////////////////////////////////////////////////////////////////////////////////////////////////////'''
win = GraphWin('Urna Eletrônica', 950, 596, autoflush = False)
urna = Image(Point(475, 298), 'Python/Urna_eletronica/lib/urna_eletronica.png').draw(win)
default = [[4, 'Deputado Federal'],[5, 'Deputado Estadual'], [3, 'Senador'], [2, 'Governador'], [2, 'Presidente']]
mixer.init()
draws = []
tela = []
box = []
voto = ''

load = 0
while load <= 460:
  load_bar = Rectangle(Point(80, 375), Point(80 + load, 390)).draw(win)
  load_bar.setFill('green')       
  msg_gravando = Text(Point(320, 410), 'Gravando').draw(win)
  msg_gravando.setStyle('bold')
  msg_gravando.setSize(15)
  update()
  time.sleep(0.05)
  load_bar.undraw()
  msg_gravando.undraw()
  load += 10
win.getMouse()
    
# def cargoNum(leng, initX, initY):
#   X1 = initX + 27
#   Y1 = initY + 33
#   pontos = []
#   pontos.append(initY + Y1 / 2)
#   for i in range(leng):
#     cargo_num = Rectangle(Point(initX, initY), Point(X1, Y1)).draw(win)
#     pontos.append((initX + X1) / 2)
#     initX = X1 + 2
#     X1 += 29
#     box.append(cargo_num)
#   return pontos

# cargoNum(3, 122, 273)

# win.getMouse()


# config = open('Python/Urna_eletronica/lib/config.csv', mode = 'r', encoding = 'utf-8')
# raw_list = config.read().split('\n-\n')
# config.close()
# for x in range(len(raw_list)):
#   raw_list[x] = raw_list[x].split('\n')
#   for x1 in range(len(raw_list[x])):
#     raw_list[x][x1] = raw_list[x][x1].split(';')
#   print(raw_list,'\n')

# print(raw_list[0][1][0])



# candidatos = open('Python/Urna_eletronica/lib/candidatos.csv', mode = 'r', encoding = 'utf-8')
# cand_list = candidatos.read().split('\n')
# candidatos.close()
# for candidatos in range(len(cand_list)):
#   cand_list[candidatos] = cand_list[candidatos].split(';')



# cand_matrix = getCandidatos()[1:]
    # x = 320
    # y = 250
    # for c in range(len(cand_matrix)):
    #   v = Text(Point(x, y), f'{candidatos_matrix[c][3]} \t {candidatos_matrix[c][4]} Votos').draw(win)
    #   v.setSize(8)
    #   y += 15
    # win.getMouse()
    
# while res == 1:
#   while cargo < 5:
#     if len(draws) == 0:
#       if cargo == 0:
#         label_cargo = cargoLabel(224, 282, 'Deputado Federal')
#         slots = cargoNum(4, 114, 333)
#         tam = 4
#       elif cargo == 1:
#         label_cargo = cargoLabel(224, 282, 'Deputado Estadual')
#         slots = cargoNum(5, 114, 333)
#         tam = 5
#       elif cargo == 2:
#         label_cargo = cargoLabel(238, 254, 'Senador')
#         slots = cargoNum(3, 122, 273)
#         tam = 3
#       elif cargo == 3:
#         label_cargo = cargoLabel(239, 266,'Governador')
#         slots = cargoNum(2, 129, 301)
#         tam =  2
#       elif cargo == 4:
#         label_cargo = cargoLabel(239, 266, 'Presidente')
#         slots = cargoNum(2, 129, 301)
#         tam = 2
#     click = getKey(win.getMouse())
#     if len(voto) < tam:
#       if click in range(10):
#         voto += str(click)
#         writeNum(slots, str(click), len(voto))
#       if len(voto) >= (tam // 2):
#         cand, label = searchCandidato(candidatos_matrix, voto, tam, draws[0].getText())
#         if cand == False and voto != 'nulo':
#           eraseDraws(a = tela)
#           nuloMsg()
#           voto = 'nulo'
#           cand = -1
#         else:
#           if draws[0].getText() != label:
#             draws[0].setText(label)
#           eraseDraws(a = tela)
#           legendaMsg()
#         if len(voto) == tam and voto != 'nulo':
#           if cargo == 0:
#             deputadoFederal(candidatos_matrix, cand)
#           elif cargo == 1:
#             deputadoEstadual(candidatos_matrix, cand)
#           elif cargo == 2:
#             senador(candidatos_matrix, cand)
#           elif cargo == 3:
#             governador(candidatos_matrix, cand)
#           elif cargo == 4:
#             presidente(candidatos_matrix, cand)
#       if 'Corrige' in str(click):
#         voto = ''
#         eraseDraws(a = draws, b = tela)
#       elif 'Branco' in str(click) and voto == '':
#         cand = -2
#         voto = 'Branco'
#         eraseDraws(a = tela, b = box)
#         brancoMsg()
#     if len(voto) >= tam:
#       if 'Corrige' in str(click):
#         voto = ''
#         eraseDraws(a = draws, b = tela)
#       elif 'Confirma' in str(click):
#         confirmaVoto(candidatos_matrix, cand)
#         confirmaSound()
#         eraseDraws(a = draws, b = tela, c = box)
#         cargo += 1
#         voto = ''
#   eraseDraws(a = draws, b = tela, c = box)
#   fimSound()
#   Fim = Text(Point(320, 360), 'FIM').draw(win)
#   Fim.setSize(35)
#   time.sleep(1)
#   Fim.undraw()
#   secao += 1
#   fimTela = Text(Point(320, 360), 'Pressione CONFIRMA para rodar novamente ou CORRIGE para contabilizar os votos').draw(win)
#   fimTela.setSize(10)
#   click = getKey(win.getMouse())
#   fimTela.undraw()
#   if 'Confirma' in str(click):
#     res = 1
#     cargo = 0
#   else:
#     res = 0
#     candidatos_matrix = getCandidatos()[1:]
#     x = 320
#     y = 250
#     for c in range(len(candidatos_matrix)):
#       v = Text(Point(x, y), f'{candidatos_matrix[c][3]} \t {candidatos_matrix[c][4]} Votos').draw(win)
#       v.setSize(8)
#       y += 15
#     win.getMouse()