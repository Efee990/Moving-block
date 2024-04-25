import pygame, sys
from pygame.locals import QUIT
pygame.font.init()

clock = pygame.time.Clock()
level = 0
speed = 9/10
lives = 3
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('WORLD DESTROYED')
screen.fill((255,70,231))
fire_image = pygame.image.load("./fire.png")
fire_image = pygame.transform.scale(fire_image,(100,50))
car_image = pygame.image.load("car.png")
car_image = pygame.transform.scale(car_image,(30,45))
Dino = car_image.get_rect(center=(200,30))
water = fire_image.get_rect(center=(0,200))
t_car = car_image.copy()
def level_up():
  global level, speed
  Dino.y = 30
  Dino.x = 200
  level = level+1
  speed = speed+6/10
  



while True:
  my_font = pygame.font.SysFont('Comic Sans MS', 30)
  text_surface = my_font.render(str(lives), False, (0, 0, 0))
  clock.tick(60)
  screen.fill((255,70,231))
  screen.blit(t_car,Dino)
  screen.blit(fire_image,water)
  screen.blit(text_surface, (0,0))
  text_surface = my_font.render(str(level), False, (0,0,0))
  screen.blit(text_surface, (380,0))
  keys = pygame.key.get_pressed()
  if keys[pygame.K_a] and Dino.x > 0:
    Dino.x-=3
    t_car = pygame.transform.rotate(car_image,270)
  if keys[pygame.K_s]:
    Dino.y+=4
    t_car = pygame.transform.rotate(car_image,0)
  if keys[pygame.K_d] and Dino.x < 370: 
    Dino.x+=3
    t_car = pygame.transform.rotate(car_image,90)
  if keys[pygame.K_w] and Dino.y > 0:
    Dino.y-=4
    t_car = pygame.transform.rotate(car_image,180)
    #pygame.transform.rotate("30,car_image")
  for event in pygame.event.get():
  
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  if Dino.colliderect(water):
    lives = lives-1
    if lives == 0:
      pygame.quit()
    level_up()
  water.x += speed
  if water.x>400:
    water.x=-50
  if Dino.y > 260:
    level_up()
  pygame.display.update()
