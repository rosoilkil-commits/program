import pygame
import random
pygame.init() 
screen = pygame.display.set_mode((600, 300))
pygame.display.set_caption("snake")
icon = pygame.image.load('images/images.jpg')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
running = True
x = 150
y = 300
def spawn_figure():
    x = random.randint(0, 600-20)
    y = random.randint(0, 300-20)
    return x,y
x, y = spawn_figure()
figure_x, figure_y = spawn_figure()
paused = False
snake = 5
history = []
while running:  
   

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
    clock.tick(30)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 10
    if keys[pygame.K_s]:
        y += 10
    if keys[pygame.K_a]:
        x -= 10 
    if keys[pygame.K_d]:
        x += 10
    x = max(0, min(x, 600 - 20))
    y = max(0, min(y, 300 - 20))
    history.append((x, y))
    if len(history) > snake:
        history.pop(0)
    soil21 = pygame.Rect(x, y, 20, 20)
    soil32 = pygame.Rect(figure_x, figure_y, 20, 20)
    if soil21.colliderect(soil32):
        figure_x, figure_y = spawn_figure()
    screen.fill((0,0 ,0))
    for segment in history:
            pygame.draw.rect(screen, (255, 255, 255), (segment[0], segment[1], 20, 20))    
    pygame.draw.rect(screen, (255, 0, 0), (figure_x, figure_y, 20, 20))
    pygame.draw.rect(screen, (255, 255, 255), (x, y, 20, 20))
    pygame.display.update()
        

pygame.quit()