import pygame

health = 100

damage = .05

def apply_dmg(dmg,orig_health):
    new_health = orig_health - (orig_health * dmg)
    return new_health

res = (800,600)

# need to complete
def draw_healthbar(scr, color, pos_x, pos_y, leng, wid):
    color = (0,255,0)
    obj = (pos_x, pos_y, leng, wid)
    pygame.draw.rect(scr,color, obj)

pygame.init()

screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()

p_x = 400
p_y = 300
speed = 5

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_SPACE:
                print("Loss health")

        # Handle continuous key holding
    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] or keys[pygame.K_UP]:
        p_y -= speed
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        p_y += speed
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        p_x -= speed
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        p_x += speed

    screen.fill((30, 30, 30))

    pygame.draw.rect(screen, (0, 200, 255), (p_x, p_y, 50, 50))
    pygame.draw.rect(screen, (0,255,0),(10,10,100,20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()            