# Write your code here :-)
import pygame
import random
import time
pygame.init()


# define colors
black=(0,0,0)
white=(255, 255, 255)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)   # Blue
yellow=(255, 255, 0)  # Yellow
magenta=(255, 0, 255)  # Magenta
cyan=(0, 255, 255)  # Cyan
purple=(128, 0, 128)  # Purple
orange=(255, 165, 0)  # Orange

# width and height of window
width=900
height=600

ball_size = 10
pygame.display.set_caption("My Snake")
gameWindow=pygame.display.set_mode((width,height))
surface = pygame.Surface((width, height))
exit_game=False
game_over=False
food_x=random.randint(20,width/2)
food_y=random.randint(20,height/2)
snake_x=40
snake_y=40
snake_size=10
food_size=10
velocity_x=0
velocity_y=0
s=0
#ball_x=360
#ball_y=200

#control speed
clock = pygame.time.Clock()
fps =12

while exit_game is not True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_LEFT:

                velocity_x=-10
                velocity_y=0
            if event.key==pygame.K_RIGHT:
                velocity_x=10
                velocity_y=0
            if event.key==pygame.K_UP:
                velocity_y=-10
                velocity_x=0
            if event.key==pygame.K_DOWN:
                velocity_y=10
                velocity_x=0
#
    snake_x+=velocity_x
    snake_y+=velocity_y
    if abs(snake_x-food_x) and abs(snake_y - food_y)<6:
        s+=10
        snake_size+=2
        food_x=random.randint(20,width/2)
        food_y=random.randint(20,height/2)
    if snake_x < 0 or snake_x >width or snake_y < 0 or snake_y >height  :
        exit_game=True
    #if abs(snake_x - ball_x) < 12 and abs(snake_y - ball_y) < 12:
      # s-=1

    gameWindow.fill(purple)
    #pygame.draw.circle(gameWindow, white, (ball_x, ball_y), ball_size)
    #pygame.draw.circle(gameWindow, white, (bal_x, bal_y), ball_size)
    #pygame.draw.circle(gameWindow, white, (ba_x, ba_y), ball_size)
    pygame.draw.rect(gameWindow,red,[food_x,food_y,food_size,food_size])
    pygame.draw.rect(gameWindow,yellow,[snake_x,snake_y,snake_size,snake_size])
# display score board
    font = pygame.font.Font(None, 25)
    text = font.render("Score: " + str(s), True, (255, 255, 255))
    gameWindow.blit(text, (10, 10))
    clock.tick(fps)
    pygame.display.update()
font = pygame.font.Font(None, 36)
text = font.render("Game Over!", True, (255, 255, 255))
gameWindow.blit(text, (width/2 - text.get_width()/2, height/2 - text.get_height()/2))
pygame.display.update()
time.sleep(2)
pygame.quit()
