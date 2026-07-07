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

## Cours : programmation orientee objet en Python

### Classe, instance et `__init__`

```python
class Square:
    def __init__(self, size):
        self.__size = size       # attribut "prive" (par convention)
```

- Une **classe** est un modele qui decrit la structure et le comportement
  d'objets. Une **instance** est un objet concret cree a partir de ce
  modele : `carre = Square(5)`.
- `__init__` est le **constructeur** : appele automatiquement a la creation
  d'une instance (`Square(5)`), il initialise les attributs.
- `self` represente **l'instance courante** : c'est toujours le premier
  parametre des methodes d'instance, et Python le passe automatiquement
  (on ne l'ecrit jamais lors de l'appel : `carre.area()`, pas
  `carre.area(carre)`).

### Encapsulation : attributs "prives"

```python
class Square:
    def __init__(self, size):
        self.__size = size   # le double underscore "cache" l'attribut
```

- Prefixer un attribut par `__` declenche le *name mangling* : l'attribut
  devient difficile d'acces depuis l'exterieur de la classe
  (`carre._Square__size`). Convention pour signaler "ne touchez pas
  directement a cet attribut".
- But : **forcer le passage par des methodes controlees** (validation,
  calculs...) plutot que de laisser n'importe qui modifier l'etat interne
  sans verification.

### Validation dans le constructeur

```python
def __init__(self, size=0):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    self.__size = size
```

- `isinstance(valeur, type)` verifie le **type** d'une valeur — plus robuste
  que `type(valeur) == int`, car il prend en compte l'heritage.
- On **valide a la creation** : un objet `Square` ne devrait jamais pouvoir
  exister dans un etat incoherent (taille negative, mauvais type...).

### `@property` et `@x.setter` : controler l'acces aux attributs

```python
class Square:
    def __init__(self, size=0):
        self.size = size           # passe par le setter ci-dessous !

    @property
    def size(self):
        """Getter : appele quand on lit carre.size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter : appele quand on ecrit carre.size = ..."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
```

- `@property` transforme une **methode** en quelque chose qui se lit comme
  un **attribut** : `carre.size` (sans parentheses) appelle la methode
  `size(self)`.
- `@size.setter` definit ce qui se passe quand on ecrit `carre.size = 10` :
  la validation s'execute **automatiquement**, meme depuis l'exterieur de la
  classe.
- Resultat : l'interface reste simple (`carre.size`), mais chaque lecture ou
  ecriture passe par du code controle — le meilleur des deux mondes entre
  simplicite et securite.

### Methodes d'instance et calculs derives

```python
def area(self):
    return self.__size ** 2

def perimeter(self):
    if self.__size == 0:
        return 0
    return self.__size * 4
```

Une **methode d'instance** calcule ou agit a partir de l'**etat** de
l'objet (`self.__size`). Elle peut retourner une valeur calculee (`area`),
modifier l'etat, ou produire un affichage (`my_print`).

### `__str__` : representation textuelle d'un objet

```python
def __str__(self):
    if self.__size == 0:
        return ""
    lignes = []
    for _ in range(self.__size):
        lignes.append(" " * self.__position_x + "#" * self.__size)
    return "\n".join(lignes)
```

- `__str__` est une **methode magique** (entre doubles underscores) appelee
  automatiquement par `print(objet)` ou `str(objet)`.
- Elle permet de definir **comment un objet s'affiche**, sans que l'appelant
  ait besoin de connaitre les details internes.

### De `Square` a `Rectangle` : reutiliser un schema

`Rectangle` applique exactement le meme schema getter/setter validé sur
**deux** attributs (`width`, `height`) au lieu d'un seul (`size`), puis
ajoute des methodes derivees (`area`, `perimeter`) qui combinent ces deux
attributs. Reconnaitre ce genre de **schema repetable** est une competence
cle : une fois qu'on maitrise la validation d'un attribut via
`@property`/`@setter`, l'appliquer a plusieurs attributs est mecanique.

### Vue d'ensemble

```
Square / Rectangle
├── __init__        : creation + validation initiale (via les setters)
├── @property xxx   : lecture controlee d'un attribut prive
├── @xxx.setter     : ecriture controlee (validations TypeError/ValueError)
├── area() / perimeter() : calculs derives de l'etat courant
├── my_print()      : affichage base sur l'etat
└── __str__()       : representation textuelle (print(objet))
```

---

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