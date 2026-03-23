# Cours Three.js (11 ans) - "Mon premier monde 3D"

## Mini-cours facile : les coordonnees en 3D (avant de commencer)

### Point de depart : ce que les enfants connaissent deja

Dans Scratch (et en maths), ils connaissent le repere 2D :

- `x` = abscisse (gauche/droite)
- `y` = ordonnee (haut/bas)

En Three.js, on ajoute une 3e direction :

- `z` = profondeur (avant/arriere)

### Image simple a raconter

"Imagine une salle de classe :"

- Se deplacer a gauche/droite -> axe `x`
- Monter/descendre -> axe `y`
- Avancer/reculer dans la salle -> axe `z`

### Regle tres simple

- `x` positif -> vers la droite
- `x` negatif -> vers la gauche
- `y` positif -> vers le haut
- `y` negatif -> vers le bas
- `z` positif -> vers toi (camera)
- `z` negatif -> vers le fond de la scene

### Mini-exemples (comme Scratch, mais en 3D)

```js
cube.position.x = 2;   // va a droite
cube.position.y = 1;   // monte un peu
cube.position.z = -3;  // va vers le fond
```

ajoute la  ligne suivante avant ```renderer.render(scene, camera);```  dans la fonction animate() du fichier index.html pour que le cube se déplace :

```js
cube.position.set(2, 1, -3); // x, y, z d'un coup
```



### Activite flash (5 min)

Demander aux enfants :

1. "Comment envoyer le cube a gauche ?" -> `x` negatif
2. "Comment le faire monter ?" -> augmenter `y`
3. "Comment l'eloigner de la camera ?" -> mettre `z` plus negatif

Objectif de cette intro :
"En 3D, c'est comme le 2D... avec une dimension bonus : la profondeur `z`."

---

## Objectif du cours

A la fin de la séance, les enfants sauront :

- Comprendre les 4 éléments de base de Three.js : `scene`, `camera`, `renderer`, `objet`
- Créer un objet 3D et le faire tourner
- Ajouter de la lumière pour rendre la scène plus jolie
- Modifier la position, la taille et la rotation d'un objet
- Contrôler un objet avec le clavier (flèches) 

--- 

## Idee simple pour les enfants

On peut expliquer Three.js comme un petit theatre 3D :

- **La scene** = la scene de theatre (ou se passe l'action)
- **La camera** = les yeux du spectateur
- **Le renderer** = la tele qui affiche l'image
- **L'objet 3D** = l'acteur principal (ici : le cube )

---

## Deroulement du cours (1h environ)

## 0-5 min - Allumer la tele 3D

### But
Comprendre les 4 briques de base.

### chercher les 4 briques de base dans `index.html`

- `const scene = new THREE.Scene();`
- `const camera = new THREE.PerspectiveCamera(...);`
- `const renderer = new THREE.WebGLRenderer(...);`
- `document.body.appendChild(renderer.domElement);`

### A noter
"Sans ces 4 briques, rien ne peut s'afficher."

### Mini-defi (2 min)
Demander : "Que se passe-t-il si on ne met pas `renderer` ?"

Votre Réponse ici : 

---

## 5-15 min - Ajouter le cube heros

### But
Creer le premier objet 3D visible.

### chercher le code pour créer le cube dans `index.html`
une de ces lignes est commentée enleve le commentaire pour que le cube soit créé.
- `new THREE.BoxGeometry(...)` -> la forme
- `new THREE.MeshStandardMaterial(...)` -> l'apparence
- `new THREE.Mesh(geometry, material)` -> l'objet final
- `scene.add(cube)` -> on l'ajoute dans le monde

### Image mentale
Geometry = squelette, Material = peau, Mesh = personnage complet.

### Mini-defi
Changer la taille du cube :

- Petit : `new THREE.BoxGeometry(1, 1, 1)`
- Geant : `new THREE.BoxGeometry(3, 3, 3)`

lien vers la documentation de la taille du cube : https://threejs.org/docs/#api/en/geometries/BoxGeometry

---

## 15-25 min - La boucle magique (animation)

### But
Comprendre pourquoi le cube bouge.

### chercher le code pour faire tourner le cube
certaines lignes sont commentées enleve le commentaire pour que le cube tourne.

- `requestAnimationFrame(animate);`
- `cube.rotation.x += 0.01;`
- `cube.rotation.y += 0.015;`
- `renderer.render(scene, camera);`

###  A noter
"La fonction `animate()` se rappelle elle-meme tres vite, comme un dessin anime."

### Mini-defi

- Doubler la vitesse (`0.02`, `0.03`)
- Inverser la rotation (`-0.01`)


lien vers la documentation de la rotation : https://threejs.org/docs/#api/en/objects/Mesh/rotation

---

## Lumiere

### But
Voir l'effet de la lumiere sur un objet 3D.

### Chercher le code pour ajouter la lumiere dans `index.html`

- `DirectionalLight` (le soleil)
- `AmbientLight` (la lumiere generale)
- `MeshStandardMaterial` avec `metalness` et `roughness`

### chercher le code à décommenter pour ajouter la lumiere d'une lampe de poche dans `index.html`
que remarquez vous ?
 
### Mini-defi
Mettre une lumiere trop faible puis forte :
- faible : `new THREE.DirectionalLight(0xffffff, 0.2)`
- forte : `new THREE.DirectionalLight(0xffffff, 2)`
commenter les autres lumieres pour ne voir que la lumiere ambiante.
decommente ensuite la lampe de poche.

### A noter :
 un objet sans lumiere parait plat 

lien vers la documentation de la lumiere : https://threejs.org/docs/#api/en/lights/DirectionalLight

## Materiaux (texture)

### But
Comprendre les differents materiaux disponibles.

### Chercher le code pour ajouter le materiau dans `index.html`

- `MeshStandardMaterial`
- `MeshBasicMaterial`
- `MeshPhongMaterial`

lien vers la documentation de la texture : https://threejs.org/docs/#api/en/loaders/TextureLoader

### Mini-defi
Mettre un materiau different pour le cube :
- standard : `new THREE.MeshStandardMaterial({ color: 0x00ffcc })`
- basic : `new THREE.MeshBasicMaterial({ color: 0x00ffcc })`
- phong : `new THREE.MeshPhongMaterial({ color: 0x00ffcc })`

### A noter :
un materiau (texture) est une image qui est appliquée sur un objet.
on peut appliquer une texture sur un objet en ajoutant un materiau avec une texture. 

essayez de changer la texture ! sélectionnez une image via le bouton "texture" .

lien vers la documentation de la texture : https://threejs.org/docs/#api/en/materials/MeshStandardMaterial



## Personnalisation libre + clavier

### Partie A  - "Mon mini univers"

Personnalisez votre monde :

- Changer la couleur du cube (`color: 0x00ffcc`, etc.)
- Changer la forme (sphere, cone, torus)
  - sphere : `new THREE.SphereGeometry(0.8, 32, 32)`
  - cone : `new THREE.ConeGeometry(0.7, 1.8, 32)`
  - torus : `new THREE.TorusGeometry(0.7, 0.2, 32, 32)`
- Ajouter 2 ou 3 objets
- Changer la position (`position.x`, `position.y`, `position.z`)
- Changer la taille (`scale.set(...)`)

### Exemples d'objets bonus

```js
const sphere = new THREE.Mesh(
  new THREE.SphereGeometry(0.8, 32, 32),
  new THREE.MeshStandardMaterial({ color: 0x33aaff })
);
sphere.position.x = -2.5;
scene.add(sphere);
```

```js
const cone = new THREE.Mesh(
  new THREE.ConeGeometry(0.7, 1.8, 32),
  new THREE.MeshStandardMaterial({ color: 0xffaa00 })
);
cone.position.x = 2.5;
scene.add(cone);
```

### Partie B - Controle clavier + conclusion

Dans le fichier, garder la logique :

- Fleche droite/gauche -> rotation du cube
- Fleche haut/bas -> deplacement vertical

Puis demander un mini challenge :
"Fais bouger le cube aussi avec `A`, `D`, `W`, `S`."

Exemple :

```js
window.addEventListener("keydown", (event) => {
  if (event.key === "d") cube.position.x += 0.3;
  if (event.key === "a") cube.position.x -= 0.3;
  if (event.key === "w") cube.position.z -= 0.3;
  if (event.key === "s") cube.position.z += 0.3;
});
```


---

## Bonus  

- Ajouter un "sol" avec `PlaneGeometry`
- Faire changer la couleur du cube dans le temps
- Ajouter un deuxieme cube qui tourne en sens inverse

Exemple couleur animee :

```js
const t = Date.now() * 0.002;
cube.material.color.setHSL((Math.sin(t) + 1) / 2, 0.8, 0.5);
```

 
