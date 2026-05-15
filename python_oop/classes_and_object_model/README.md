# Classes and Object Model (Python OOP)

Ce dossier introduit la programmation orientee objet en Python a travers une
progression de classes `Square` et `Rectangle`.

## Sujets abordes

- Definition de classes et creation d'instances
- Constructeur `__init__`
- Attributs prives (encapsulation)
- Propriete `@property` et setters
- Validation de type et de valeur
- Methodes d'instance (`area`, `perimeter`, `my_print`, `__str__`)

## Exercices et notions travaillees

### `0-square.py`

- Cree une classe `Square` vide.
- Notion cle: syntaxe minimale d'une classe.

### `1-square.py`

- Ajoute un constructeur avec attribut prive `__size`.
- Notion cle: initialisation d'etat interne.

### `2-square.py`

- Valide `size` dans `__init__`:
	- `TypeError` si ce n'est pas un entier
	- `ValueError` si negatif
- Notion cle: defensive programming des la construction d'objet.

### `3-square.py`

- Ajoute la methode `area()` pour calculer la surface.
- Notion cle: encapsuler un calcul dans une methode d'instance.

### `4-square.py`

- Introduit `@property size` et `@size.setter` avec validations.
- Conserve `area()`.
- Notion cle: controle d'acces a un attribut prive via proprietes.

### `5-square.py`

- Ajoute `my_print()` pour afficher le carre en `#`.
- Gere le cas `size == 0`.
- Notion cle: comportement d'affichage lie a l'etat d'un objet.

### `6-square.py`

- Ajoute un attribut `position` (tuple de 2 entiers positifs) avec validation.
- Met a jour `my_print()` pour tenir compte du decalage.
- Redefinit `__str__()` pour une representation textuelle du carre.
- Notion cle: modelisation plus riche d'un objet (taille + position + rendu).

### `1-rectangle.py`

- Cree une classe `Rectangle` avec `width` et `height` en proprietes validees.
- Notion cle: reutiliser le schema getter/setter sur plusieurs attributs.

### `2-rectangle.py`

- Complete `Rectangle` avec `area()` et `perimeter()`.
- Retourne `0` pour le perimetre si largeur ou hauteur vaut `0`.
- Notion cle: ajouter des comportements derives de l'etat.

## Competences acquises

- Construire des classes robustes avec validations coherentes.
- Encapsuler les donnees et exposer des interfaces claires.
- Faire evoluer une classe par increments fonctionnels.