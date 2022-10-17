#coding=UTF-8
from graphics import *
from pygame import mixer
import datetime
import time

'''//////////GLOBAL///////////////////////////////////////////////////////////////////////////////////////////////////////////'''
win=GraphWin('Urna Eletrônica', 950, 596)
urna=Image(Point(475, 298),'Python/Urna_eletronica/lib/urna_eletronica.png').draw(win)
mixer.init()
draws = []
voto = ''

'''//////////FUNCTIONS////////////////////////////////////////////////////////////////////////////////////////////////////////'''
def getCandidatos():
  candidatos = open('Python/Urna_eletronica/lib/candidatos.csv','r')
  raw_list = candidatos.read().split('\n')
  candidatos.close()
  cand_list = []
  for candidatos in raw_list[1:]:
    cand_list.append(candidatos.split(';'))
  return cand_list
  
def searchCandidato(matrix, numero):
  for linha in range(len(matrix)):
    for coluna in range(len(matrix[linha])):
      if numero in matrix[linha][coluna]:
        if numero <= 2:
          print(matrix[linha][coluna + 3])
          return True
      else:
        return False

def getKey(click):
  if click.getX() in range(670, 722) and click.getY() in range(272, 312):
    num_down = Image(Point(695, 292),'Python/Urna_eletronica/lib/button/n1_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return '1'
  elif click.getX() in range(742, 790) and click.getY() in range(272, 312):
    num_down = Image(Point(766, 292),'Python/Urna_eletronica/lib/button/n2_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return '2'
  elif click.getX() in range(810, 860) and click.getY() in range(272, 312):
    num_down = Image(Point(835, 292),'Python/Urna_eletronica/lib/button/n3_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return '3'
  elif click.getX() in range(670, 722) and click.getY() in range(330, 370):
    num_down = Image(Point(695, 352),'Python/Urna_eletronica/lib/button/n4_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return '4'
  elif click.getX() in range(742, 790) and click.getY() in range(330, 370):
    num_down = Image(Point(766, 352),'Python/Urna_eletronica/lib/button/n5_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return '5'
  elif click.getX() in range(810, 860) and click.getY() in range(330, 370):
    num_down = Image(Point(835, 352),'Python/Urna_eletronica/lib/button/n6_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return '6'
  elif click.getX() in range(670, 722) and click.getY() in range(390, 430):
    num_down = Image(Point(696, 411),'Python/Urna_eletronica/lib/button/n7_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return '7'
  elif click.getX() in range(742, 790) and click.getY() in range(390, 430):
    num_down = Image(Point(765.5, 411),'Python/Urna_eletronica/lib/button/n8_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return '8'
  elif click.getX() in range(810, 860) and click.getY() in range(390, 430):
    num_down = Image(Point(834, 411),'Python/Urna_eletronica/lib/button/n9_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return '9'
  elif click.getX() in range(742, 790) and click.getY() in range(444, 488):
    num_down = Image(Point(773,466),'Python/Urna_eletronica/lib/button/n0_down.png').draw(win)
    time.sleep(0.10)
    num_down.undraw()
    return '0'
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

def confirmaSound():
  sound = mixer.Sound('Python/Urna_eletronica/lib/inter.wav')
  return sound.play()

def fimSound():
  sound = mixer.Sound('Python/Urna_eletronica/lib/fim.wav')
  return sound.play()

def cargoNum(leng):
  initX = 114
  initX1 = 141
  for i in range(leng):
    cargo_num = Rectangle(Point(initX, 333), Point(initX1, 365)).draw(win)
    initX = initX1 + 2
    initX1 += 29
    
def cargoLabel(candidatos):
  cargo_label = Text(Point(224, 282), f'{candidatos[0][1]}').draw(win).setSize(19)

def nuloMsg():
    return 0

def legendaMsg():
    return 0

'''//////////MAIN/////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
candidatos_matrix = getCandidatos()
while True:
  voto += str(getKey(win.getMouse()))
  if len(voto) >= 2:
    if searchCandidato(candidatos_matrix, voto) == False:
      nuloMsg()
  if 'Corrige' in voto:
    voto = ''
  
  
  
  
  
  
  
'''
- colocar hora e data ();
- msg de voto nulo ();
- msg de voto em branco ();
- msg de gravando ();
- msg fim no final ();
- pressionar dos botões (feito);

- deputado(a) federal = 4 digitos
- deputado(a) estudal = 5 digitos
- senador(a) = 3 digitos
- govenador(a) = 2 digitos
- presidente = 2 digitos
'''