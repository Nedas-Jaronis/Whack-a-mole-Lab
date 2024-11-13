import pygame
import random

def draw_grid(screen):
    black = (0,0,0) # Color to be used for the lines
    cell_size = 32 #declaring the cell size
    for i in range(0, 640, cell_size): #0 to 640 pixels in increments of 32 pixels
        pygame.draw.line(screen, black, (i, 0), (i, 512), 1)
    for i in range(0, 512, cell_size): #0 to 512 pixels in increments of 32 pixels
        pygame.draw.line(screen, black, (0, i), (640, i), 1)
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512)) #settings screen size
        clock = pygame.time.Clock()
        mole_x, mole_y = 0,0
        mole_rect = mole_image.get_rect(topleft=(mole_x, mole_y))  #setting mole to top left of the screen

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    if mole_rect.collidepoint(mouse_x, mouse_y): #if mouse click hits the box with the mole on it then mole randomizes
                        mole_x = random.randrange(0, 640, 32)
                        mole_y = random.randrange(0, 512, 32)
                        mole_rect.topleft = (mole_x, mole_y)
            screen.fill("light green") #background color of screen
            draw_grid(screen) #drawing the grid itself
            screen.blit(mole_image, mole_rect) 
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()



if __name__ == "__main__":
    main()
