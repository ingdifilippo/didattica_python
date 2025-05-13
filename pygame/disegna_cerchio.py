import pygame

# Initialize game engine modules
pygame.init()

# Set window dimensions
larghezza = 600
altezza = 600

surface = pygame.display.set_mode((larghezza, altezza))

# Set window title
pygame.display.set_caption("Disegna un Cerchio sulla superficie creata")

# set colors
nero = (0, 0, 0)

rosso = (255, 0, 0)  # Puoi scegliere il colore del cerchio

# Definisci il raggio del cerchio in pixel
raggio = 100

# Calcola le coordinate del centro della finestra
centro_x = larghezza // 2
centro_y = altezza // 2

# Main loop
running = True
while running:
    # Manage window close call event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clear screen
    surface.fill(nero)

    # Disegna il cerchio
    # pygame.draw.circle(superficie, colore, (centro_x, centro_y), raggio, spessore=0)
    # - superficie: la superficie su cui disegnare (il nostro 'schermo')
    # - colore: il colore del cerchio (il nostro 'rosso')
    # - (centro_x, centro_y): le coordinate del centro del cerchio
    # - raggio: il raggio del cerchio
    # - spessore (opzionale): se omesso o 0, il cerchio è pieno. Un valore maggiore indica lo spessore del bordo.
    pygame.draw.circle(surface, rosso, (centro_x, centro_y), raggio, 4)

    # Aggiorna lo schermo per mostrare il disegno
    pygame.display.flip()

# Esce da Pygame
pygame.quit()
