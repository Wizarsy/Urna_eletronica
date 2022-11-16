#coding=UTF-8
from graphics import *
from pygame import mixer
import datetime
import time

'''//////////GLOBAL///////////////////////////////////////////////////////////////////////////////////////////////////////////'''
win = GraphWin('Urna Eletrônica', 950, 596)
urna = Image(Point(475, 298), 'Python/Urna_eletronica/lib/urna_eletronica.png').draw(win)
mixer.init()
now = datetime.datetime.now()
draws = []
tela = []
box = []

'''//////////FUNCTIONS////////////////////////////////////////////////////////////////////////////////////////////////////////'''  
def confirmaSound():
  sound = mixer.Sound('Python/Urna_eletronica/lib/inter.wav')
  return sound.play()

def fimSound():
  sound = mixer.Sound('Python/Urna_eletronica/lib/fim.wav')
  return sound.play()

def getCandidatos():
  candidatos = open('Python/Urna_eletronica/lib/candidatos.csv', mode = 'r', encoding = 'utf-8')
  cand_list = candidatos.read().split('\n')
  candidatos.close()
  for candidatos in range(len(cand_list)):
    cand_list[candidatos] = cand_list[candidatos].split(';')
  return cand_list
  
def getConfig():
  config = open('Python/Urna_eletronica/lib/config.csv', mode = 'r', encoding = 'utf-8')
  config_list = config.read().split('\n-\n')
  config.close()
  for x in range(len(config_list)):
    config_list[x] = config_list[x].split('\n')
    for x1 in range(len(config_list[x])):
      config_list[x][x1] = config_list[x][x1].split(';')
  return config_list
  
def searchCandidato(voto, tam, cargo):
  for linha in range(len(cand_matrix)):
    if voto[:2] in cand_matrix[linha][0][:2] and cargo[:2] in cand_matrix[linha][1]:
      if len(cand_matrix[linha][0]) == tam:
        return linha, cand_matrix[linha][1]
      elif len(cand_matrix[linha][0]) != tam:
        continue
      elif len(voto) == (tam // 2):
        return True, ''
  return False, ''

def getKeys(click):
  if click == None:
    return
  elif click.getX() in range(670, 722) and click.getY() in range(272, 312):
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

def cargoLabel(index):
  cargo_label = Text(Point(config[index][0][1], config[index][0][2]), f'{config[index][0][0]}').draw(win)
  cargo_label.setSize(19)
  draws.append(cargo_label)
  
def numSlots(index):
  tam, initX, initY = int(config[index][1][0]), int(config[index][1][1]), int(config[index][1][2])
  X1 = initX + 27
  Y1 = initY + 33
  pontos = []
  pontos.append((initY + Y1) / 2)
  for i in range(tam):
    cargo_num = Rectangle(Point(initX, initY), Point(X1, Y1)).draw(win)
    pontos.append((initX + X1) / 2)
    initX = X1 + 2
    X1 += 29
    box.append(cargo_num)
  return pontos

def telaInfo():
  msg_voto = Text(Point(102, 229),'SEU VOTO PARA').draw(win)
  msg_tecla = Text(Point(88, 490),'Aperte a tecla:').draw(win)
  msg_corrige = Text(Point(183, 520),'CORRIGE para REINICIAR este voto').draw(win)
  msg_voto.setSize(11)
  msg_tecla.setSize(10)
  msg_corrige.setSize(10)
  tela.append(msg_voto), tela.append(msg_tecla), tela.append(msg_corrige)

def nuloMsg():
  telaInfo()
  line = Line(Point(38, 479), Point(587, 479)).draw(win)
  line.setWidth(2)
  msg_confirma = Text(Point(179, 505),'CONFIRMA para CONFIRMAR este voto').draw(win)
  msg_nulo = Text(Point(334, 443),'VOTO NULO').draw(win)
  msg_nome = Text(Point(int(config[cargo][4][1]) + 68 , config[cargo][4][2]), 'NÚMERO ERRADO').draw(win)
  msg_nome.setSize(16)
  msg_confirma.setSize(10)
  msg_nulo.setSize(28)
  tela.append(line), tela.append(msg_confirma), tela.append(msg_nome), tela.append(msg_nulo)
  
def brancoMsg():
  telaInfo()
  line = Line(Point(38, 479), Point(587, 479)).draw(win)
  line.setWidth(2)
  msg_confirma = Text(Point(179, 505),'CONFIRMA para CONFIRMAR este voto').draw(win)
  msg_branco = Text(Point(322, 360),'VOTO EM BRANCO').draw(win)
  msg_confirma.setSize(10)
  msg_branco.setSize(27)
  tela.append(line), tela.append(msg_confirma), tela.append(msg_branco)

def legendaMsg():
  telaInfo()
  line = Line(Point(38, 479), Point(587, 479)).draw(win)
  line.setWidth(2)
  msg_confirma = Text(Point(179, 505),'CONFIRMA para PROSSEGUIR').draw(win)
  msg_legenda = Text(Point(525, 508),'(voto de legenda)').draw(win)
  msg_partido = Text(Point(config[cargo][2][1], config[cargo][2][2]), config[cargo][2][0]).draw(win)
  msg_partido_nome = Text(Point(int(config[cargo][2][1]) + (3.5 * len(cand_matrix[cand][2]) + 50), config[cargo][2][2]), cand_matrix[cand][2]).draw(win)
  msg_confirma.setSize(10)
  msg_legenda.setSize(10)
  tela.append(line), tela.append(msg_confirma), tela.append(msg_legenda), tela.append(msg_partido), tela.append(msg_partido_nome)

def writeNum(point, num, tam):
  Num = Text(Point(point[tam], point[0]), num).draw(win)
  Num.setSize(20)
  draws.append(Num)
  
def eraseDraws(**draws):
  for dic in draws.values():
    for x in dic:
      x.undraw()
    dic.clear()

def confirmaVoto(cand):
  candidatos = open('Python/Urna_eletronica/lib/candidatos.csv', mode = 'w', encoding = 'utf-8')
  votoM = int(cand_matrix[cand][4]) + 1
  cand_matrix[cand][4] = str(votoM)
  for linha in range(len(cand_matrix)):
    for coluna in range(len(cand_matrix[linha])):
      candidatos.write(cand_matrix[linha][coluna])
      if coluna<len(cand_matrix[linha]) - 1:
        candidatos.write(';')
    if linha<len(cand_matrix) - 1:
      candidatos.write('\n')
  candidatos.close()
  
def candInfo(index, cand, voto):
  last, n = None, 0
  for x in range(len(config[index])):
    for x1 in range(len(config[index][x])):
      if '_' in config[index][x][x1] and last == None:
        last = x
        break
  temp = config[index][2:last]
  for i in range(len(temp)):
    info = Text(Point(temp[i][1], temp[i][2]), temp[i][0])
    info.draw(win)
    draws.append(info)   
  msg_partido_nome = Text(Point(int(config[cargo][2][1]) + (3.5 * len(cand_matrix[cand][2]) + 50), config[cargo][2][2]), cand_matrix[cand][2]).draw(win)
  draws.append(msg_partido_nome)
  while cand_matrix[cand][0] == cand_matrix[cand + n][0]:
    msg_nome = Text(Point(int(config[cargo][4 + n][1]) + (3.5 * len(cand_matrix[cand + n][3]) + 85), config[cargo][4 + n][2]),cand_matrix[cand + n][3]).draw(win)
    n += 1
    draws.append(msg_nome)
  temp = config[index][last:]
  for i in range(len(temp)):
    img = Image(Point(temp[i][1], temp[i][2]), f'Python/Urna_eletronica/lib/cand_imagens/{voto + temp[i][0]}').draw(win)
    draws.append(img)
  return n 

def getdayweek():
  return datetime.datetime.now().strftime('%a')

def getday():
  return datetime.datetime.now().strftime('%d')

def getmonth():
  return datetime.datetime.now().strftime('%m')

def getyear():
  return datetime.datetime.now().strftime('%Y')

def gethour():
  return datetime.datetime.now().strftime('%H')

def getminute():
  return datetime.datetime.now().strftime('%M')

def getsecond():
  return datetime.datetime.now().strftime('%S')

def getdate():
  return f'{getdayweek()}  {getday()}/{getmonth()}/{getyear()}  {gethour()}:{getminute()}:{getsecond()}'

'''//////////MAIN/////////////////////////////////////////////////////////////////////////////////////////////////////////////'''
config = getConfig()
cand_matrix = getCandidatos()
status = ['legenda', 'branco', 'nulo']
click = ''
voto = ''
st = ''
cargo = 0
seções = 0
res = 1

while res == 1:
  msg_inicio = Text(Point(310, 390 ), 'INÍCIO DA VOTAÇÃO\n\nIDENTIFIQUE O ELEITOR').draw(win)
  msg_inicio.setSize(18)
  while not 'Confirma' in str(click):
    msg_hora = Text(Point(138, 226), f'{getdate()}').draw(win)
    time.sleep(0.5)
    msg_hora.undraw()
    click = getKeys(win.checkMouse())
  msg_inicio.undraw()
  while cargo < 5:
    if len(draws) == 0:
      cargoLabel(cargo)
      slots = numSlots(cargo)
      tam = int(config[cargo][1][0])
    click = getKeys(win.getMouse())
    if len(voto) < tam and st != 'branco':
      if click in range(10):
        voto += str(click)
        writeNum(slots, str(click), len(voto))
        if len(voto) >= (tam // 2):
          cand, label = searchCandidato(voto, tam, draws[0].getText())
          if cand == False:
            eraseDraws(a = tela)
            nuloMsg()
            cand = -2
            st = 'nulo'
          else:
            if draws[0].getText() != label:
              draws[0].setText(label)
            if cargo < 2 and len(tela) <= 1:
              eraseDraws(a = tela)
              legendaMsg()
              st = 'legenda'
              cand = -1       
        if len(voto) == tam and st != 'nulo':
          if voto == cand_matrix[cand][0]:
            eraseDraws(a = tela)
            n_images = candInfo(cargo, cand, voto)
            if n_images == 1:
              line = Line(Point(38, 479), Point(587, 479)).draw(win)
            if n_images == 2:
              line = Line(Point(38, 479), Point(508, 479)).draw(win)
            elif n_images >= 3:
              line = Line(Point(38, 479), Point(428, 479)).draw(win)
            line.setWidth(2)
            msg_voto = Text(Point(102, 229),'SEU VOTO PARA').draw(win)
            msg_voto.setSize(11)
            msg_confira = Text(Point(300, 505),'CONFIRA O SEU VOTO').draw(win)
            msg_confira.setSize(20)
            time.sleep(1)
            msg_confira.undraw()
            msg_tecla = Text(Point(88, 490),'Aperte a tecla:').draw(win)
            msg_tecla.setSize(10)
            msg_corrige = Text(Point(183, 520),'CORRIGE para REINICIAR este voto').draw(win)
            msg_corrige.setSize(10)
            msg_confirma = Text(Point(179, 505),'CONFIRMA para CONFIRMAR este voto').draw(win)
            msg_confirma.setSize(10)
            tela.append(line), tela.append(msg_confirma), tela.append(msg_voto), tela.append(msg_tecla), tela.append(msg_corrige)
          else:
            cand = -1
            line = Line(Point(38, 479), Point(587, 479)).draw(win)
            line.setWidth(2)
            msg_num = Text(Point(config[cargo][3][1], config[cargo][3][2]), config[cargo][3][0]).draw(win)
            msg_nome = Text(Point(int(config[cargo][4][1]) + 104, config[cargo][4][2]), 'CANDIDATO INEXISTENTE').draw(win)
            msg_nome.setSize(16)
            msg_legenda = Text(Point(300, 462),'VOTO DE LEGENDA').draw(win)
            msg_legenda.setSize(25)
            tela.append(line), draws.append(msg_num), draws.append(msg_nome), draws.append(msg_legenda)
      if 'Corrige' in str(click):
        eraseDraws(a = draws, b = tela)
        voto = ''
        st = ''
      elif 'Branco' in str(click) and voto == '':
        eraseDraws(a = tela, b = box)
        brancoMsg()
        cand = -3
        st = 'branco'       
    if len(voto) >= tam or st in status:
      if 'Corrige' in str(click):
        eraseDraws(a = draws, b = tela)
        voto = ''
        st = '' 
      elif 'Confirma' in str(click):
        confirmaVoto(cand)
        confirmaSound()
        eraseDraws(a = draws, b = tela, c = box)
        cargo += 1
        voto = ''
        st = ''
  eraseDraws(a = draws, b = tela, c = box)
  load = 0
  msg_gravando = Text(Point(320, 410), 'Gravando').draw(win)
  msg_gravando.setStyle('bold')
  msg_gravando.setSize(15)
  while load <= 460:
    load_bar = Rectangle(Point(80, 375), Point(80 + load, 390)).draw(win)
    load_bar.setFill('green')       
    time.sleep(0.030)
    load_bar.undraw()
    load += 10
  msg_gravando.undraw()
  seções += 1
  msg_Fim = Text(Point(320, 360), 'FIM').draw(win)
  msg_Fim.setSize(35)
  msg_bateria = Image(Point(559, 231), 'Python/Urna_eletronica/lib/bateria.png').draw(win)
  fimSound()
  time.sleep(1)
  msg_Fim.undraw()
  msg_bateria.undraw()
  click = ''
  fimTela = Text(Point(320, 360), 'Pressione CONFIRMA para rodar novamente\n\nou CORRIGE para contabilizar os votos').draw(win)
  fimTela.setSize(18)
  while not 'Confirma' in str(click) and not 'Corrige' in str(click):
    msg_hora = Text(Point(134, 226), f'{getdate()}').draw(win)
    time.sleep(0.5)
    msg_hora.undraw()
    click = getKeys(win.checkMouse())
  fimTela.undraw()
  if 'Confirma' in str(click):
    cargo = 0
    res = 1
  if 'Corrige' in str(click):
    res = 0
    break

cand_cor ={
  'REPUBLICANOS' : 'blue3',
  'NOVO' : 'orange',
  'PT' : 'red',
  'PL' : 'blue1',
  'PSD' : 'blue2',
  'PSOL' : 'yellow1',
  'PSDB' : 'blue',
  'MDB' : 'green',
  '' : 'black'
}

graph_cand = 0
click = ''
config_linha = 0
cand_matrix = cand_matrix[1:]
linex = Line(Point(79, 480), Point(541, 480)).draw(win)
liney = Line(Point(79, 480), Point(79, 260)).draw(win)
graphX_label = Text(Point(linex.getP2().getX() + 20, 480), 'Votos').draw(win)
graphX_label.setSize(8)
graphY_label = Text(Point(79, liney.getP2().getY() - 20), 'Seções').draw(win)
graphY_label.setSize(8)
tela.append(linex), tela.append(liney), tela.append(graphX_label), tela.append(graphY_label)
liney_points = (liney.getP1().getY() - liney.getP2().getY()) / seções
graphY = liney_points
linex_points = (linex.getP1().getX() + linex.getP2().getX()) / 3
graphX = 0

for seção in range(1, (seções + 1)):
  graph_seções = Text(Point(60, 480 - graphY), seção).draw(win)
  tela.append(graph_seções)
  graphY += liney_points

for linha in range(len(cand_matrix)):
  if cand_matrix[linha][2]== '-':
    continue
  if graph_cand == 0:
    try:
      graph_label = Text(Point(320, 231), config[config_linha][0][0]).draw(win)
      draws.append(graph_label)
    except:
      pass
  graph_result = Text(Point(110 + graphX, 500), f'{cand_matrix[linha][3]}').draw(win)
  graph_result.setSize(8)
  graph_votos = Text(Point(110 + graphX, 520), f'{cand_matrix[linha][4]} votos').draw(win)
  graph_votos.setSize(8)
  graph_bar = Rectangle(Point(105 + graphX, 480), Point(120 + graphX, 480 - (liney_points * int(cand_matrix[linha][4])))).draw(win)
  graph_bar.setFill(cand_cor[cand_matrix[linha][2]])
  if graph_bar.getP2().getY() < liney.getP2().getY():
    graph_bar.undraw()
    graph_bar = Rectangle(Point(105 + graphX, 480), Point(120 + graphX, liney.getP2().getY())).draw(win)
    graph_bar.setFill(cand_cor[cand_matrix[linha][2]])
  percent = (int(cand_matrix[linha][4]) * 100) / seções
  graph_percent = Text(Point(110 + graphX, graph_bar.getP2().getY() - 10), f'{percent}%').draw(win)
  graph_percent.setSize(8)
  draws.append(graph_result), draws.append(graph_bar), draws.append(graph_votos), draws.append(graph_percent)
  graphX += linex_points
  graph_cand += 1
  if graph_cand == 3:
    while not 'Confirma' in str(click):
      click = getKeys(win.getMouse())
    eraseDraws(a = draws)
    config_linha += 1
    graph_cand = 0
    graphX = 0
    click = ''
eraseDraws(a = draws, b = tela)
click = ''
while not 'Confirma' in str(click):
  msg_final = Text(Point(320, 360), 'Pressione CONFIRMA para encerrar o programa').draw(win)
  msg_final.setSize(16)
  msg_hora = Text(Point(134, 226), f'{getdate()}').draw(win)
  time.sleep(1)
  msg_final.undraw()
  msg_hora.undraw()
  click = getKeys(win.checkMouse())
urna.undraw()
win.close()