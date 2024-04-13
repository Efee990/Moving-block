import pygame, sys
from pygame.locals import QUIT

clock = pygame.time.Clock()

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
while True:
  clock.tick(60)
  screen.fill((255,70,231))
  screen.blit(t_car,Dino)
  screen.blit(fire_image,water)
  keys = pygame.key.get_pressed()
  if keys[pygame.K_a] and Dino.x > 0:
    Dino.x-=2
    t_car = pygame.transform.rotate(car_image,270)
  if keys[pygame.K_w] and Dino.y < 260:
    Dino.y+=3
    t_car = pygame.transform.rotate(car_image,0)
  if keys[pygame.K_d] and Dino.x < 370: 
    Dino.x+=2
    t_car = pygame.transform.rotate(car_image,90)
  if keys[pygame.K_s] and Dino.y > 0:
    Dino.y-=2
    t_car = pygame.transform.rotate(car_image,180)
    #pygame.transform.rotate("30,car_image")
  for event in pygame.event.get():
  
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  if Dino.colliderect(water):
    pygame.quit()    
  water.x += 9/10
  if water.x>400:
    water.x=-50
  pygame.display.update()
