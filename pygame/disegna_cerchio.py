import pygame

# Inizializza Pygame
pygame.init()

# Imposta le dimensioni della finestra
larghezza = 600
altezza = 600
schermo = pygame.display.set_mode((larghezza, altezza))

# Imposta il titolo della finestra
pygame.display.set_caption("Disegna un Cerchio")

# Definisci i colori
bianco = (255, 255, 255)
nero = (0, 0, 0)
rosso = (255, 0, 0)  # Puoi scegliere il colore del cerchio

# Definisci il raggio del cerchio
raggio = 100

# Calcola le coordinate del centro della finestra
centro_x = larghezza // 2
centro_y = altezza // 2

# Loop principale del gioco
running = True
while running:
    # Gestisci gli eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Pulisci lo schermo
    schermo.fill(bianco)

    # Disegna il cerchio
    # pygame.draw.circle(superficie, colore, (centro_x, centro_y), raggio, spessore=0)
    # - superficie: la superficie su cui disegnare (il nostro 'schermo')
    # - colore: il colore del cerchio (il nostro 'rosso')
    # - (centro_x, centro_y): le coordinate del centro del cerchio
    # - raggio: il raggio del cerchio
    # - spessore (opzionale): se omesso o 0, il cerchio è pieno. Un valore maggiore indica lo spessore del bordo.
    pygame.draw.circle(schermo, rosso, (centro_x, centro_y), raggio)

    # Aggiorna lo schermo per mostrare il disegno
    pygame.display.flip()

# Esce da Pygame
pygame.quit()
