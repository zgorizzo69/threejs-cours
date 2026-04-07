# 🐍 Lecon: Creer "Chasse au Fantome"

Pygame Zero est parfait pour apprendre la programmation, car le code est lisible et rapide a tester.

## Objectif

Un fantome apparait a des endroits aleatoires.  
Tu dois cliquer dessus avant qu'il ne se deplace pour gagner un point.

## 1) Preparation


1. **Structure du dossier**
   Dans ce dossier, cree:
   - un fichier `jeu.py`
   - verifie que le dossier `images/` existe et qu'il contient l'image `fantome.png`.


2. **Installation de Pygame Zero** (si ce n'est pas deja fait)
   Ouvre ton terminal et execute:
   ```bash
   pip install pgzero
   ```

3. **lance le script avec la commande :**
   ```bash
   python jeu.py
   ``` 

## 2) Concepts cles

- **Actors (acteurs)**: dans Pygame Zero, les personnages sont des `Actor`.
- **`draw()`**: indique a l'ordinateur quoi afficher (fond, score, personnage).
- **Evenements**: les fonctions comme `on_mouse_down()` reagissent aux actions du joueur.

**variables globales:** les variables qui sont declarees en dehors des fonctions sont accessibles partout dans le code. Elles sont déclarées avec le mot-clé `global`.
**variables locales:** les variables qui sont declarees dans les fonctions sont accessibles uniquement dans la fonction. Elles sont déclarées avec le mot-clé `local`.
Exemple de variable globale :
```python
global score = 0
```
Exemple de variable locale :
```python
def increment_score():
    local score = 0
    score += 1
    return score
```
si on oublie de mettre le mot-clé `local`, la variable sera globale.

## 3) Code complet (`jeu.py`)

Copie ce code dans ton fichier:

```python
import pgzrun
import random

# 1. CONFIGURATION DE LA FENETRE
# WIDTH, HEIGHT et TITLE sont lus automatiquement par Pygame Zero
# au demarrage pour creer la fenetre du jeu.
WIDTH = 1024
HEIGHT = 768
TITLE = "Chasse au Fantome"

# 2. CREATION DU FANTOME (Actor)
# 'fantome' fait reference au fichier 'images/fantome.png'
fantome = Actor("fantome")
# pos est la position du fantome sur l'ecran, (x, y).
fantome.pos = (300, 200)
# score est la variable qui contient le score du joueur.
score = 0
# message est la variable qui contient le message a afficher.
message = "Clique sur le fantome !"

# 3. DESSINER SUR L'ECRAN
# draw() est appelee automatiquement plusieurs fois par seconde.
# Elle doit redessiner toute la scene a chaque frame.
def draw():
    # clear() efface tout ce qui est affiche sur l'ecran.
    # screen est l'ecran du jeu.
    screen.clear()
    # fill() remplit l'ecran avec la couleur specifiee.
    screen.fill((30, 30, 60))  # Fond bleu fonce
    # fantome.draw() affiche le fantome sur l'ecran.
    # draw() affiche le fantome sur l'ecran.
    fantome.draw()

    # Affichage du score et du message
    screen.draw.text(f"Score: {score}", (20, 20), fontsize=30, color="white")
    # draw.text() affiche le texte sur l'ecran.
    # f"Score: {score}" est une chaine de caracteres qui contient le score du joueur.
    # (20, 50) est la position du texte sur l'ecran.
    # fontsize=30 est la taille du texte.
    # color="orange" est la couleur du texte.
    screen.draw.text(message, (20, 50), fontsize=30, color="orange")

# 4. DEPLACER LE FANTOME AU HASARD
# Cette fonction place le fantome a une nouvelle position aleatoire.
# On garde une marge de 50 px pour eviter qu'il sorte de l'ecran.
def deplacer_fantome():
    # On choisit des coordonnees X et Y aleatoires
    # random.randint() genere un nombre aleatoire entre deux valeurs.
    # WIDTH - 50 est la largeur de l'ecran - 50px pour eviter qu'il sorte de l'ecran.
    # HEIGHT - 50 est la hauteur de l'ecran - 50px pour eviter qu'il sorte de l'ecran.
    # fantome.x sera un nombre aleatoire entre 50 et WIDTH - 50.
    # fantome.y sera un nombre aleatoire entre 50 et HEIGHT - 50.
    fantome.x = random.randint(50, WIDTH - 50)
    fantome.y = random.randint(50, HEIGHT - 50)

# 5. REAGIR AU CLIC DE SOURIS
# on_mouse_down(pos) est appelee automatiquement a chaque clic.
# l'argument "pos" contient la position du clic (x, y).
def on_mouse_down(pos):
    # declarer les variables score et message en global
    global score, message

    # Si la souris touche le fantome au moment du clic
    if fantome.collidepoint(pos):
        # incrementer le score de 1
        score += 1
        # declarer la variable message avec la valeur "Touche !"
        message = "Touche !"
        # deplacer le fantome a une nouvelle position aleatoire
        deplacer_fantome()
    else:
        # declarer la variable message avec la valeur "Rate !"
        message = "Rate !"
        # decrementer le score de 1
        score -= 1

# 6. PROGRAMMER LE DEPLACEMENT (toutes les 1.5 secondes)
# schedule_interval() appelle deplacer_fantome() automatiquement
# toutes les 1.5 secondes pendant la partie.
clock.schedule_interval(deplacer_fantome, 1.5)

# LANCER LE JEU
# pgzrun.go() demarre la boucle principale:
# - ecoute les clics
# - appelle draw()
# - execute les fonctions planifiees par clock
pgzrun.go()
```

## 4) Defis (hacks)

Une fois le jeu fonctionnel, essaie ces ameliorations:

1. **Acceleration**  
   `clock` est un objet fourni par Pygame Zero pour gerer le temps dans le jeu.  
   Il permet de lancer une fonction apres un delai, ou de la repeter a intervalle regulier.

   Nous voulons augmenter la difficulté du jeu en augmentant la vitesse de deplacement du fantome.
   Pour ce faire nous allons utiliser la fonction `clock.schedule_interval()` pour planifier le deplacement du fantome a intervalle regulier.
   Nous allons utiliser la fonction `clock.unschedule()` pour retirer l'ancien timer.
     **Pourquoi devons nous retirer l'ancien timer ?**
     **Réponse:** Parce que si nous ne le faisons pas, nous aurons deux timers actifs en meme temps pour la meme action, ce qui causera des problèmes de performance.

   Puis nous allons utiliser la fonction `clock.schedule_interval()` pour planifier a nouveau le deplacement du fantome a intervalle regulier mais avec un intervalle plus court.
   Plus la valeur est petite, plus le fantome bouge vite, donc le jeu devient plus difficile.
 

   **Reflexion:**
   - A quel moment du jeu veux-tu augmenter la difficulte: a chaque clic reussi, tous les X points, ou avec le temps?
   - Dans quelle fonction existante ce changement doit-il etre declenche?
   - Comment eviter d'avoir plusieurs timers actifs en meme temps pour la meme action?
   - Quelle valeur dois-tu modifier pour que le fantome se deplace de plus en plus vite?
   - Quelle limite minimale fixes-tu pour que le jeu reste jouable?

   **Indice:** il faut chercher dans le code l'endroit ou le deplacement est planifie, puis imaginer une facon de replanifier ce deplacement avec un intervalle plus court quand la difficulte augmente.

   Pour retirer l'ancien timer : `clock.unschedule(deplacer_fantome)`.
   Pour planifier le nouveau timer : `clock.schedule_interval(deplacer_fantome, 1.0)`.  `1.0` est l'intervalle en secondes, ajuste cette valeur pour augmenter ou diminuer la vitesse de deplacement du fantome.


2. **Fantome qui retrecit**  
   A chaque clic reussi: 
   Exemple de code :
   ```python
   def clic_reussi():
       fantome.scale -= 0.1
   ```
    **Reflexion:**
    - A quel moment du jeu veux-tu que le fantome retrecisse?
    - Dans quelle fonction existante ce changement doit-il etre declenche?
    - Comment eviter d'avoir plusieurs timers actifs en meme temps pour la meme action?
    - Quelle valeur dois-tu modifier pour que le fantome retrecisse?
    - Quelle limite minimale fixes-tu pour que le jeu reste jouable?



3. **Game over**  
   Ajoute un chronometre.  
   Si le joueur n'atteint pas 10 points en 20 secondes, affiche **PARTIE TERMINEE** au centre de l'ecran.
   **Reflexion:**
   - A quel moment du jeu veux-tu afficher le message **PARTIE TERMINEE**?
   - Dans quelle fonction existante ce changement doit-il etre declenche?
   - Comment eviter d'avoir plusieurs timers actifs en meme temps pour la meme action?
   - Quelle valeur dois-tu modifier pour que le fantome se deplace de plus en plus vite?
   - Quelle limite minimale fixes-tu pour que le jeu reste jouable?

   **Indice:** il faut chercher dans le code l'endroit ou le chronometre est affiche, puis imaginer une facon de afficher le message **PARTIE TERMINEE** quand le chronometre arrive a 20 secondes.

   Pour afficher le message **PARTIE TERMINEE** : `screen.draw.text("PARTIE TERMINEE", (WIDTH/2, HEIGHT/2), fontsize=30, color="red")`.
   Exemple de code :
   ```python
   if score >= 10:
       # declarer la variable message avec la valeur **PARTIE TERMINEE**
       message = "PARTIE TERMINEE"
       # Afficher le message **PARTIE TERMINEE** au centre de l'ecran
       screen.draw.text(message, (WIDTH/2, HEIGHT/2), fontsize=30, color="red")
       # arreter le jeu
       pgzrun.quit()
   ```
   Exemple de fonction chronometre :
   ```python
   def chronometre():
       # declarer la variable chronometre avec la valeur 0
       global chronometre
       # incrementer la variable chronometre de 1
       chronometre += 1
       # afficher la variable chronometre
       print(chronometre)
   ```
   Pour arreter le jeu : `pgzrun.quit()`.
   Pour reinitialiser le chronometre : `clock.unschedule(chronometre)`.
   Pour planifier le nouveau chronometre : `clock.schedule_interval(chronometre, 1.0)`.  `1.0` est l'intervalle en secondes, ajuste cette valeur pour augmenter ou diminuer la vitesse de deplacement du fantome.

   4. **Fantome qui change de couleur**  
   A chaque clic reussi: le fantome change de couleur aléatoirement
   
   **Indice:** il faut chercher dans le code l'endroit ou le fantome change de couleur, puis imaginer une facon de changer la couleur du fantome.

   Pour choisir aleatoirement une couleur du fantome : `fantome.color = random.choice(["red", "green", "blue", "yellow", "purple", "orange", "pink", "brown", "gray", "black", "white"])`.

   Exemple de code :
   ```python
   def clic_reussi():
       fantome.color = random.choice(["red", "green", "blue", "yellow", "purple", "orange", "pink", "brown", "gray", "black", "white"])
   ```

   **Reflexion:**
   - A quel moment du jeu veux-tu que le fantome change de couleur?
   - Dans quelle fonction existante ce changement doit-il etre declenche?
   - Quelle valeur dois-tu modifier pour que le fantome change de couleur?
   - Quelle limite minimale fixes-tu pour que le jeu reste jouable?