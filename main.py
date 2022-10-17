#coding=UTF-8
from graphics import *
import datetime
import time
from pygame import mixer

'''//////////GLOBAL///////////////////////////////////////////////////////////////////////////////////////////////////////////'''
win=GraphWin('Urna', 950, 596)
urna=Image(Point(475, 298),'Python/Urna_eletronica/lib/urna_eletronica.png').draw(win)
mixer.init()

# cargo_label = Text(Point(224, 282), 'Deputado Federal').draw(win).setSize(19)
# cargo_num = Rectangle(Point(114, 333), Point(141, 365)).draw(win)

'''//////////FUNCTIONS////////////////////////////////////////////////////////////////////////////////////////////////////////'''
def getCandidatos():
  candidatos = open('Python/Urna_eletronica/lib/candidatos.csv','r')
  raw_list = candidatos.read().split('\n')
  candidatos.close()
  cand_list = []
  for candidatos in raw_list[1:]:
    cand_list.append(candidatos.split(';'))
  return cand_list
  
def searchCandidato(candidato, numero):
  for linha in range(len(candidato)):
    for coluna in range(len(candidato[linha])):
      if numero in candidato[linha][coluna]:
        print(candidato[linha][coluna + 3])
      else:
        print('invalido')

def getKey(click):
  if click.getX() in range(670,722) and click.getY() in range(272,312):
    num_down=Image(Point(695,292),'Python/Urna_eletronica/lib/button/n1_down.png').draw(win)
    print('1')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(742,790) and click.getY() in range(272,312):
    num_down=Image(Point(766,292),'Python/Urna_eletronica/lib/button/n2_down.png').draw(win)
    print('2')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(810,860) and click.getY() in range(272,312):
    num_down=Image(Point(835,292),'Python/Urna_eletronica/lib/button/n3_down.png').draw(win)
    print('3')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(670,722) and click.getY() in range(330,370):
    num_down=Image(Point(695,352),'Python/Urna_eletronica/lib/button/n4_down.png').draw(win)
    print('4')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(742,790) and click.getY() in range(330,370):
    num_down=Image(Point(766,352),'Python/Urna_eletronica/lib/button/n5_down.png').draw(win)
    print('5')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(810,860) and click.getY() in range(330,370):
    num_down=Image(Point(835,352),'Python/Urna_eletronica/lib/button/n6_down.png').draw(win)
    print('6')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(670,722) and click.getY() in range(390,430):
    num_down=Image(Point(696,411),'Python/Urna_eletronica/lib/button/n7_down.png').draw(win)
    print('7')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(742,790) and click.getY() in range(390,430):
    num_down=Image(Point(765.5,411),'Python/Urna_eletronica/lib/button/n8_down.png').draw(win)
    print('8')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(810,860) and click.getY() in range(390,430):
    num_down=Image(Point(834,411),'Python/Urna_eletronica/lib/button/n9_down.png').draw(win)
    print('9')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(742,790) and click.getY() in range(444,488):
    num_down=Image(Point(773,466),'Python/Urna_eletronica/lib/button/n0_down.png').draw(win)
    print('0')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(642,712) and click.getY() in range(502,540):
    num_down=Image(Point(677,521),'Python/Urna_eletronica/lib/button/branco_down.png').draw(win)
    print('Branco')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(732,800) and click.getY() in range(502,540):
    num_down=Image(Point(766,521),'Python/Urna_eletronica/lib/button/corrige_down.png').draw(win)
    print('Corrige')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(822,890) and click.getY() in range(490,540):
    num_down=Image(Point(859,519),'Python/Urna_eletronica/lib/button/confirma_down.png').draw(win)
    print('Confirma')
    time.sleep(0.09)
    num_down.undraw()

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
  return cargo_label

'''//////////MAIN/////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
while True:
  getKey(win.getMouse())
  candidatos_matrix = getCandidatos()
  print(candidatos_matrix)
  cargoLabel(candidatos_matrix)
  searchCandidato(candidatos_matrix, '9104')
  
  
  
  
  
  
  
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