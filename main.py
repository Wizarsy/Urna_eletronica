from graphics import *
import time
from pygame import mixer

# mixer.init()
# mixer.music.load("Python/Urna_eletronica/lib/inter.mp3")
# mixer.music.play()
win=GraphWin('Urna',950,596)
urna=Image(Point(475,298),'lib/urna_eletronica.png').draw(win)
# tela=Rectangle(Point(38,212),Point(587,533)).draw(win)
# tela.setFill('white')

def numkey(click):
  if click.getX() in range(670,722) and click.getY() in range(272,312):
    num_down=Image(Point(695,292),'lib/button/n1_down.png').draw(win)
    print('1')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(742,790) and click.getY() in range(272,312):
    num_down=Image(Point(766,292),'lib/button/n2_down.png').draw(win)
    print('2')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(810,860) and click.getY() in range(272,312):
    num_down=Image(Point(835,292),'lib/button/n3_down.png').draw(win)
    print('3')
    time.sleep(0.09)
    num_down.undraw()

  elif click.getX() in range(670,722) and click.getY() in range(330,370):
    num_down=Image(Point(695,352),'lib/button/n4_down.png').draw(win)
    print('4')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(742,790) and click.getY() in range(330,370):
    num_down=Image(Point(766,352),'lib/button/n5_down.png').draw(win)
    print('5')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(810,860) and click.getY() in range(330,370):
    num_down=Image(Point(835,352),'ib/button/n6_down.png').draw(win)
    print('6')
    time.sleep(0.09)
    num_down.undraw()

  elif click.getX() in range(670,722) and click.getY() in range(390,430):
    num_down=Image(Point(696,411),'lib/button/n7_down.png').draw(win)
    print('7')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(742,790) and click.getY() in range(390,430):
    num_down=Image(Point(765.5,411),'lib/button/n8_down.png').draw(win)
    print('8')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(810,860) and click.getY() in range(390,430):
    num_down=Image(Point(834,411),'lib/button/n9_down.png').draw(win)
    print('9')
    time.sleep(0.09)
    num_down.undraw()

  elif click.getX() in range(742,790) and click.getY() in range(444,488):
    num_down=Image(Point(773,466),'lib/button/n0_down.png').draw(win)
    print('0')
    time.sleep(0.09)
    num_down.undraw()

  elif click.getX() in range(642,712) and click.getY() in range(502,540):
    num_down=Image(Point(677,521),'lib/button/branco_down.png').draw(win)
    print('Branco')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(732,800) and click.getY() in range(502,540):
    num_down=Image(Point(766,521),'lib/button/corrige_down.png').draw(win)
    print('Corrige')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(822,890) and click.getY() in range(490,540):
    num_down=Image(Point(859,519),'lib/button/confirma_down.png').draw(win)
    print('Confirma')
    time.sleep(0.09)
    num_down.undraw()

while True:
  numkey(win.getMouse())



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