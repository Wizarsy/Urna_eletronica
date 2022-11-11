'''
CODIGO ICOMPLETO
'''









#coding=UTF-8
from graphics import *
from pygame import mixer
import datetime
import time

'''//////////GLOBAL///////////////////////////////////////////////////////////////////////////////////////////////////////////'''
win = GraphWin('Urna Eletrônica', 950, 596)
urna = Image(Point(475, 298), 'Python/Urna_eletronica/lib/urna_eletronica.png').draw(win)
default = [[4, 'Deputado Federal'],[5, 'Deputado Estadual'], [3, 'Senador'], [2, 'Governador'], [2, 'Presidente']]
mixer.init()
draws = []
tela = []
box = []
voto = ''

'''//////////FUNCTIONS////////////////////////////////////////////////////////////////////////////////////////////////////////'''
def confirmaSound():
  sound = mixer.Sound('Python/Urna_eletronica/lib/inter.wav')
  return sound.play()

def fimSound():
  sound = mixer.Sound('Python/Urna_eletronica/lib/fim.wav')
  return sound.play()

def getCandidatos():
  candidatos = open('Python/Urna_eletronica/lib/candidatos.csv', 'r')
  raw_list = candidatos.read().split('\n')
  candidatos.close()
  cand_list = []
  for candidatos in raw_list:
    cand_list.append(candidatos.split(';'))
  return cand_list
  
def searchCandidato(matrix, voto, tam, cargo):
  for linha in range(len(matrix)):
    if voto in matrix[linha][0] and cargo[:2] in matrix[linha][1]:
      if len(matrix[linha][0]) == tam:
        return linha, matrix[linha][1]
      elif len(matrix[linha][0]) != tam:
        continue
      elif len(voto) == (tam // 2):
        return True, ''
  return False, ''

def getKey(click):
  if click.getX() in range(670, 722) and click.getY() in range(272, 312):
    num_down = Image(Point(695, 292),'Python/Urna_eletronica/lib/button/n1_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return 1
  elif click.getX() in range(742, 790) and click.getY() in range(272, 312):
    num_down = Image(Point(766, 292),'Python/Urna_eletronica/lib/button/n2_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return 2
  elif click.getX() in range(810, 860) and click.getY() in range(272, 312):
    num_down = Image(Point(835, 292),'Python/Urna_eletronica/lib/button/n3_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return 3
  elif click.getX() in range(670, 722) and click.getY() in range(330, 370):
    num_down = Image(Point(695, 352),'Python/Urna_eletronica/lib/button/n4_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return 4
  elif click.getX() in range(742, 790) and click.getY() in range(330, 370):
    num_down = Image(Point(766, 352),'Python/Urna_eletronica/lib/button/n5_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return 5
  elif click.getX() in range(810, 860) and click.getY() in range(330, 370):
    num_down = Image(Point(835, 352),'Python/Urna_eletronica/lib/button/n6_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return 6
  elif click.getX() in range(670, 722) and click.getY() in range(390, 430):
    num_down = Image(Point(696, 411),'Python/Urna_eletronica/lib/button/n7_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return 7
  elif click.getX() in range(742, 790) and click.getY() in range(390, 430):
    num_down = Image(Point(765.5, 411),'Python/Urna_eletronica/lib/button/n8_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return 8
  elif click.getX() in range(810, 860) and click.getY() in range(390, 430):
    num_down = Image(Point(834, 411),'Python/Urna_eletronica/lib/button/n9_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return 9
  elif click.getX() in range(742, 790) and click.getY() in range(444, 488):
    num_down = Image(Point(773,466),'Python/Urna_eletronica/lib/button/n0_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return 0
  elif click.getX() in range(642, 712) and click.getY() in range(502, 540):
    num_down = Image(Point(677, 521),'Python/Urna_eletronica/lib/button/branco_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return 'Branco'
  elif click.getX() in range(732, 800) and click.getY() in range(502, 540):
    num_down = Image(Point(766, 521),'Python/Urna_eletronica/lib/button/corrige_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return 'Corrige'
  elif click.getX() in range(822, 890) and click.getY() in range(490, 540):
    num_down = Image(Point(859, 519),'Python/Urna_eletronica/lib/button/confirma_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return 'Confirma'

def cargoLabel(x, y, cargo):
  cargo_label = Text(Point(x, y), f'{cargo}').draw(win)
  cargo_label.setSize(19)
  draws.append(cargo_label)
  
def cargoNum(leng, initX, initX1, initY, initY1):
  pontos = []
  pontos.append((initY + initY1) / 2)
  for i in range(leng):
    cargo_num = Rectangle(Point(initX, initY), Point(initX1, initY1)).draw(win)
    pontos.append((initX + initX1) / 2)
    initX = initX1 + 2
    initX1 += 29
    box.append(cargo_num)
  return pontos

def deputadoFederal(matrix, x):
  msgNum = Text(Point(71, 349), 'Número: ').draw(win)
  msgNome = Text(Point(140, 380),f'Nome: \t{matrix[x][1]}').draw(win)
  msgPartido = Text(Point(140, 405),f'Partido: \t{matrix[x][2]}').draw(win)
  msgImage = Image(Point(500, 220), 'Python/Urna_eletronica/lib/13.png').draw(win)
  tela.append(msgNum), tela.append(msgNome), tela.append(msgPartido), tela.append(msgImage)
  
def deputadoEstadual(matrix, x):
  msgNum = Text(Point(40, 349), 'Número').draw(win)
  msgNome = Text(Point(40, 380), matrix[x][1]).draw(win)
  msgPartido = Text(Point(40, 405), matrix[x][2]).draw(win)
  msgImage = Image(Point(587, 220), 'Python/Urna_eletronica/lib/13.png').draw(win)
  tela.append(msgNum), tela.append(msgNome), tela.append(msgPartido), tela.append(msgImage)
  
def senador(matrix, x):
  msgNum = Text(Point(40, 349), 'Número').draw(win)
  msgNome = Text(Point(40, 380), matrix[x][1]).draw(win)
  msgPartido = Text(Point(40, 405), matrix[x][2]).draw(win)
  msgImage = Image(Point(587, 220), f'Python/Urna_eletronica/lib/{matrix[x][0]}.png').draw(win)
  tela.append(msgNum), tela.append(msgNome), tela.append(msgPartido), tela.append(msgImage)
    
def governador(matrix, x):
  msgNum = Text(Point(71, 349), 'Número').draw(win)
  msgNome = Text(Point(40, 380), matrix[x][1]).draw(win)
  msgPartido = Text(Point(40, 405), matrix[x][2]).draw(win)
  msgImage = Image(Point(587, 220), 'Python/Urna_eletronica/lib/13.png').draw(win)
  tela.append(msgNum), tela.append(msgNome), tela.append(msgPartido), tela.append(msgImage)
  
def presidente(matrix, x):
  msgNum = Text(Point(40, 349), 'Número').draw(win)
  msgNome = Text(Point(40, 380), matrix[x][1]).draw(win)
  msgPartido = Text(Point(40, 405), matrix[x][2]).draw(win)
  msgImage = Image(Point(587, 220), 'Python/Urna_eletronica/lib/13.png').draw(win)
  tela.append(msgNum), tela.append(msgNome), tela.append(msgPartido), tela.append(msgImage)

def telaInfo():
  line = Line(Point(38, 479), Point(587, 479)).draw(win)
  msg = Text(Point(102, 229),'SEU VOTO PARA').draw(win)
  msg1 = Text(Point(88, 490),'Aperte a tecla:').draw(win)
  msg2 = Text(Point(183, 520),'CORRIGE para REINICIAR este voto').draw(win)
  line.setWidth(2)
  msg.setSize(11)
  msg1.setSize(10)
  msg2.setSize(10)
  tela.append(line), tela.append(msg), tela.append(msg1), tela.append(msg2)

def nuloMsg():
  telaInfo()
  msg = Text(Point(179, 505),'CONFIRMA para CONFIRMAR este voto').draw(win)
  msg1 = Text(Point(334, 443),'VOTO NULO').draw(win)
  msg.setSize(10)
  msg1.setSize(28)
  tela.append(msg), tela.append(msg1)
  
def brancoMsg():
  telaInfo()
  msg = Text(Point(179, 505),'CONFIRMA para CONFIRMAR este voto').draw(win)
  msg1 = Text(Point(322, 360),'VOTO EM BRANCO').draw(win)
  msg.setSize(10)
  msg1.setSize(27)
  tela.append(msg), tela.append(msg1)

def legendaMsg():
  telaInfo()
  msg = Text(Point(179, 505),'CONFIRMA para PROSSEGUIR').draw(win)
  msg1 = Text(Point(525, 508),'(voto de legenda)').draw(win)
  msg.setSize(10)
  msg1.setSize(10)
  tela.append(msg), tela.append(msg1)

def writeNum(point, num, l):
  text = Text(Point(point[l], point[0]), num).draw(win)
  draws.append(text)
  
def eraseDraws(draws):
  for i in draws:
    i.undraw()
  draws.clear()

def confirmaVoto(matrix, cand):
  candidatos = open('Python/Urna_eletronica/lib/candidatos.csv', 'w')
  votoM = int(matrix[cand][4]) + 1
  matrix[cand][4] = str(votoM)
  for linha in range(len(matrix)):
    for coluna in range(len(matrix[linha])):
      candidatos.write(matrix[linha][coluna])
      if coluna<len(matrix[linha]) - 1:
        candidatos.write(';')
    if linha<len(matrix) - 1:
      candidatos.write('\n')
  candidatos.close()
  
'''//////////MAIN/////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
candidatos_matrix = getCandidatos()
cargo = 3
secao = 0
res = 1
while res == 1:
  while cargo < 5:
    if len(draws) == 0:
      if cargo == 0:
        label_cargo = cargoLabel(224, 282, 'Deputado Federal')
        slots = cargoNum(4, 114, 141, 333, 365)
        tam = 4
      elif cargo == 1:
        label_cargo = cargoLabel(224, 282, 'Deputado Estadual')
        slots = cargoNum(5, 114, 141, 333, 365)
        tam = 5
      elif cargo == 2:
        label_cargo = cargoLabel(238, 254, 'Senador')
        slots = cargoNum(3, 122, 149, 273, 305)
        tam = 3
      elif cargo == 3:
        label_cargo = cargoLabel(239, 266,'Governador')
        slots = cargoNum(2, 129, 156, 301, 333)
        tam =  2
      elif cargo == 4:
        label_cargo = cargoLabel(239, 266, 'Presidente')
        slots = cargoNum(2, 129, 156, 301, 333)
        tam = 2
    click = getKey(win.getMouse())
    if len(voto) < tam:
      if click in range(10):
        voto += str(click)
        writeNum(slots, str(click), len(voto))
      if len(voto) >= (tam // 2):
        cand, label = searchCandidato(candidatos_matrix, voto, tam, draws[0].getText())
        if cand == False and voto != 'nulo':
          eraseDraws(tela)
          nuloMsg()
          voto = 'nulo'
          cand = -1
        else:
          if draws[0].getText() != label:
            draws[0].setText(label)
          eraseDraws(tela)
          legendaMsg()
        if len(voto) == tam and voto != 'nulo':
          if cargo == 0:
            deputadoFederal(candidatos_matrix, cand)
          elif cargo == 1:
            deputadoEstadual(candidatos_matrix, cand)
          elif cargo == 2:
            senador(candidatos_matrix, cand)
          elif cargo == 3:
            governador(candidatos_matrix, cand)
          elif cargo == 4:
            presidente(candidatos_matrix, cand)
      if 'Corrige' in str(click):
        voto = ''
        eraseDraws(draws)
        eraseDraws(tela)
      elif 'Branco' in str(click) and voto == '':
        cand = -2
        voto = 'Branco'
        eraseDraws(tela)
        eraseDraws(box)
        brancoMsg()
    if len(voto) >= tam:
      if 'Corrige' in str(click):
        voto = ''
        eraseDraws(draws)
        eraseDraws(tela)
      elif 'Confirma' in str(click):
        confirmaVoto(candidatos_matrix, cand)
        confirmaSound()
        eraseDraws(draws)
        eraseDraws(tela)
        eraseDraws(box)
        cargo += 1
        voto = ''
  eraseDraws(draws)
  eraseDraws(tela)
  eraseDraws(box)
  fimSound()
  Fim = Text(Point(320, 360), 'FIM').draw(win)
  Fim.setSize(35)
  time.sleep(1)
  Fim.undraw()
  secao += 1
  fimTela = Text(Point(320, 360), 'Pressione CONFIRMA para rodar novamente ou CORRIGE para contabilizar os votos').draw(win)
  fimTela.setSize(10)
  click = getKey(win.getMouse())
  fimTela.undraw()
  if 'Confirma' in str(click):
    res = 1
    cargo = 0
  else:
    res = 0
    candidatos_matrix = getCandidatos()[1:]
    x = 320
    y = 250
    for c in range(len(candidatos_matrix)):
      v = Text(Point(x, y), f'{candidatos_matrix[c][3]} \t {candidatos_matrix[c][4]} Votos').draw(win)
      v.setSize(8)
      y += 15
    win.getMouse()