Pour un tout premier script, il est important de comprendre que l'ordinateur est comme un robot très obéissant : il fait **exactement** ce qu'on lui écrit, mais il ne devine rien.

Puisque c'est le début, voici les **3 concepts d'or**avant de lancer le code :

---

## 💡 Les 3 Piliers du Premier Script

### 1. L'indentation (Le "Décalage")
En Python, les espaces au début des lignes sont obligatoires. 
* Si une ligne est décalée vers la droite sous un `def`, cela signifie qu'elle fait partie de ce "bloc" d'instructions. 
* Si on oublie l'espace, l'ordinateur est perdu et affiche une `IndentationError`.

### 2. Les Variables (Les Boîtes)
Imagine que `score = 0` est une boîte étiquetée "score" dans laquelle on pose le chiffre 0. 
* Quand on écrit `score += 1`, on ouvre la boîte, on enlève le 0, on met un 1 à la place, et on referme.

### 3. Les Coordonnées (X et Y)
L'écran est une grille invisible :
* **X** : C'est la position horizontale (gauche à droite).
* **Y** : C'est la position verticale. **Attention :** En informatique, le `0` de Y est en **haut**. Plus Y augmente, plus l'objet descend.



---

## 🛠️ Guide d'installation rapide (pour le parent ou le prof)

Pour que ce premier script fonctionne sur l'ordinateur, voici la marche à suivre :

1.  **Installer Python :** Téléchargez-le sur [python.org](https://www.python.org/).
2.  **Installer l'outil de jeu :** Ouvrez une console (ou terminal) et tapez :
    `pip install pgzero`
3.  **L'Éditeur :** Vous pouvez utiliser **Notepad++**, **Mu Editor** (très simple pour les enfants), ou **VS Code**.
4.  **Le dossier "images" :** C'est l'erreur n°1 des débutants. Le fichier `jeu.py` **doit** être juste à côté d'un dossier nommé `images`. À l'intérieur de ce dossier, l'image doit s'appeler exactement `fantome.png` (tout en minuscules).

---

## 📝 Premier test : Le "Hello World" du jeu
Avant de copier tout le code du fantôme, essayez ce tout petit script pour vérifier que tout marche :
créer un fichier nommé `jeu.py` et copier le code suivant dedans :

```python
import pgzrun

def draw():
    screen.clear()
    screen.draw.text("Bravo ! Ton premier script fonctionne.", (100, 200), color="green")

pgzrun.go()
```

ensuite lancer le script avec la commande :
`python jeu.py`

**Une petite astuce :** Si tu fais une erreur de frappe, l'ordinateur affichera un message d'erreur en anglais. C'est là que Python donne l'indice pour réparer le bug !

