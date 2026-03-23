# Cours Three.js (démo)

Petit projet pédagogique : scène 3D avec **Three.js** dans le navigateur.

## Contenu

| Fichier | Description |
|--------|-------------|
| `index.html` | Cube, lumières, texture (fichier local), contrôles souris et clavier |
| `space.html` | Système solaire simplifié : Soleil, Terre, Lune, étoiles, particules, curseur de vitesse |

## Lancer en local

Pour éviter les soucis CORS avec les textures, préférez un petit serveur HTTP :

```bash
cd theejs
python3 -m http.server 8000
```

Puis ouvrez [http://localhost:8000](http://localhost:8000) et choisissez `index.html` ou `space.html`.

## Dépendances

Les scripts chargent **Three.js** via CDN (`esm.sh`) — connexion internet requise au chargement de la page.

## Licence

Contenu pédagogique — adaptez librement pour vos cours.
