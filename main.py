from graphics import *
import time

win=GraphWin('Urna',950,596)
urna=Image(Point(475,298),'lib/urna_eletronica.png').draw(win)
tela=Rectangle(Point(38,212),Point(587,533)).draw(win)
tela.setFill('white')

def numkey(click):
  if click.getX() in range(671,723) and click.getY() in range(272,312):
    num_down=Image(Point(695,292),'lib/button/n1_down.png').draw(win)
    # x=Rectangle(Point(671,272),Point(723,312)).draw(win)
    # print(x.getCenter())
    print('1')
    time.sleep(0.09)
    num_down.undraw()
  elif click.getX() in range(742,790) and click.getY() in range(273,312):
    print('2')
  elif click.getX() in range(811,859) and click.getY() in range(272,312):
    print('3')
  elif click.getX() in range(673,722) and click.getY() in range(332,371):
    print('4')
  elif click.getX() in range(743,791) and click.getY() in range(330,370):
    print('5')
  elif click.getX() in range(810,861) and click.getY() in range(330,370):
    print('6')
  elif click.getX() in range(674,722) and click.getY() in range(392,431):
    print('7')
  elif click.getX() in range(743,791) and click.getY() in range(392,427):
    print('8')
  elif click.getX() in range(810,858) and click.getY() in range(391,428):
    print('9')
  elif click.getX() in range(743,793) and click.getY() in range(444,488):
    print('0')
  elif click.getX() in range(642,712) and click.getY() in range(502,538):
    print('Branco')
  elif click.getX() in range(732,800) and click.getY() in range(502,539):
    print('Corrige')
  elif click.getX() in range(822,891) and click.getY() in range(491,538):
    print('Confirma')
    
# Image(Point(695,292),'lib/button/n1_down.png').draw(win)
# Image(Point(695,292),'lib/button/n2_down.png').draw(win)
# Image(Point(695,292),'lib/button/n3_down.png').draw(win)
# Image(Point(695,292),'lib/button/n4_down.png').draw(win)
# Image(Point(695,292),'lib/button/n5_down.png').draw(win)
# Image(Point(695,292),'lib/button/n6_down.png').draw(win)
# Image(Point(695,292),'lib/button/n7_down.png').draw(win)
# Image(Point(695,292),'lib/button/n8_down.png').draw(win)
# Image(Point(695,292),'lib/button/n9_down.png').draw(win)
# Image(Point(695,292),'lib/button/n0_down.png').draw(win)
# Image(Point(695,292),'lib/button/branco_down.png').draw(win)
# Image(Point(695,292),'lib/button/corrige_down.png').draw(win)
# Image(Point(695,292),'lib/button/confirma_down.png').draw(win)
while True:
  numkey(win.getMouse())
  print(win.getMouse())




'''
- colocar hora e data;
- msg de voto nulo;
- msg de voto em branco;
- msg de gravando;
- msg fim no final;
- pressionar dos botões;

- deputado(a) federal = 4 digitos
- deputado(a) estudal = 5 digitos
- senador(a) = 3 digitos
- govenador(a) = 2 digitos
- presidente = 2 digitos
'''