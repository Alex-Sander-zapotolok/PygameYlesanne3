import pygame

# Initsialiseeri Pygame
pygame.init()

# Mänguakna seaded
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ülesanne 2")

# Laadi pildid
bg = pygame.image.load("bg_shop.jpg")
seller = pygame.image.load("seller.png")
chat = pygame.image.load("chat.png")
logo = pygame.image.load("VIKK logo.png")
sword = pygame.image.load("Mõõk.png")
tort = pygame.image.load("ai-generated-cute-birthday-cake-in-cartoon-style-png.webp")
tekst = pygame.image.load("inkpx-curved-text.png")

tekst_pos = (309, 10)

seller = pygame.transform.scale(seller, (248, 294))
chat = pygame.transform.scale(chat, (230, 183))
logo = pygame.transform.scale(logo, (265. , 45))
sword = pygame.transform.scale(sword, (173, 143))
tort = pygame.transform.scale(tort, (100, 93))
tekst = pygame.transform.scale(tekst, (500, 300))

# Fondi seaded
font = pygame.font.Font(None, 26)
text = font.render("Alex-Sander Zapotõlok", True, (255, 255, 255))
arc_font = pygame.font.Font(None, 30)


# Mängutsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Joonista ekraanile
    screen.blit(bg, (0, 0))
    screen.blit(logo, (10, 10))
    screen.blit(seller, (90, 150))
    screen.blit(chat, (216, 75))
    screen.blit(text, (236, 140))
    screen.blit(tort, (420, 200))
    screen.blit(sword, (515, 100))
    screen.blit(tekst, (120, 100))


    pygame.display.flip()

pygame.quit()