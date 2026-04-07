import pgzrun
import random

# 1. CONFIGURATION DE LA FENÊTRE
WIDTH = 1024
HEIGHT = 768
TITLE = "Chasse au Fantôme"

# 2. CRÉATION DU FANTÔME (Actor)
# 'fantome' fait référence au fichier 'images/fantome.png'
fantome = Actor('fantome')
fantome.pos = (300, 200)

score = 0
message = "Clique sur le fantôme !"

# 3. DESSINER SUR L'ÉCRAN
def draw():
    screen.clear()
    screen.fill((30, 30, 60)) # Fond bleu foncé
    fantome.draw()
    
    # Affichage du score et du message
    screen.draw.text(f"Score: {score}", (20, 20), fontsize=30, color="white")
    screen.draw.text(message, (20, 50), fontsize=30, color="orange")

# 4. DÉPLACER LE FANTÔME AU HASARD
def deplacer_fantome():
    # On choisit des coordonnées X et Y aléatoires
    fantome.x = random.randint(50, WIDTH - 50)
    fantome.y = random.randint(50, HEIGHT - 50)

# 5. RÉAGIR AU CLIC DE SOURIS
def on_mouse_down(pos):
    global score, message
    
    # Si la souris touche le fantôme au moment du clic
    if fantome.collidepoint(pos):
        score += 1
        message = "Touché !"
        deplacer_fantome()
    else:
        message = "Raté !"
        score -= 1

# 6. PROGRAMMER LE DÉPLACEMENT (Toutes les 1.5 secondes)
clock.schedule_interval(deplacer_fantome, 1.5)

# LANCER LE JEU
pgzrun.go()