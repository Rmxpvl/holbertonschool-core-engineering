# Control Flow (Python Fundamentals)

Ce dossier regroupe des exercices d'introduction au controle de flux en Python.
L'objectif est d'apprendre a piloter l'execution d'un programme avec des
conditions, des boucles et du formatage de sortie.

## Sujets abordes

- Conditions: `if`, `elif`, `else`
- Comparaisons numeriques et logiques
- Boucles `for` avec `range`
- Utilisation de `continue`
- Manipulation basique des caracteres (`chr`, codes ASCII)
- Conversion et affichage formate (`{:02d}`, `hex`)

## Cours : piloter l'execution d'un programme

### Les conditions : `if` / `elif` / `else`

```python
if nombre > 0:
    print("positif")
elif nombre < 0:
    print("negatif")
else:
    print("zero")
```

- Chaque condition est testee **dans l'ordre**. Des qu'une condition est
  vraie, son bloc s'execute et les suivants sont ignores.
- `elif` ("else if") permet d'enchainer plusieurs cas sans imbriquer des
  `if` les uns dans les autres.
- `else` est optionnel : il capture **tous les cas restants**.
- En Python, l'**indentation** (4 espaces par convention) delimite les blocs
  — il n'y a pas d'accolades `{}`.

### La boucle `for` et `range`

```python
for i in range(10):
    print(i)        # affiche 0, 1, 2, ..., 9
```

- `range(n)` genere les entiers de `0` a `n - 1` (n valeurs au total).
- `range(debut, fin)` genere de `debut` a `fin - 1`.
- `for variable in iterable:` execute le bloc une fois pour chaque element,
  en affectant successivement chaque valeur a `variable`.

### `continue` : passer a l'iteration suivante

```python
for i in range(ord('a'), ord('z') + 1):
    lettre = chr(i)
    if lettre in ('e', 'q'):
        continue          # on ignore 'e' et 'q', et on passe a i+1
    print(lettre, end="")
```

`continue` arrete immediatement l'iteration courante de la boucle et passe
directement a la suivante, sans executer le reste du bloc pour cette
iteration.

### Caracteres et codes ASCII : `ord` et `chr`

| Fonction | Role | Exemple |
|----------|------|---------|
| `ord(c)` | Caractere -> code numerique (ASCII/Unicode) | `ord('a')` -> `97` |
| `chr(n)` | Code numerique -> caractere | `chr(97)` -> `'a'` |

Ces deux fonctions sont inverses l'une de l'autre et permettent de
**parcourir un intervalle de lettres** comme s'il s'agissait de nombres :
`for i in range(ord('a'), ord('z') + 1): print(chr(i))`.

### Boucles imbriquees

```python
for i in range(10):
    for j in range(10):
        print(i, j)
```

Une boucle `for` peut en contenir une autre : pour **chaque** valeur de la
boucle externe, la boucle interne s'execute **entierement**. C'est la base
de l'exploration de toutes les **paires** ou **combinaisons** possibles
entre deux ensembles de valeurs.

### Formatage de l'affichage

```python
print("{:02d}".format(5))   # "05" : entier sur 2 chiffres, complete par des 0
print(hex(255))             # "0xff" : representation hexadecimale
```

- `"{:02d}"` est une **specification de format** : `02d` signifie "entier
  (`d`), largeur minimale 2, complete avec des `0`".
- `hex(n)` retourne une chaine commencant par `0x` representant `n` en base
  16.

### Gerer la virgule finale dans un affichage en serie

```python
for i in range(100):
    print("{:02d}".format(i), end="" if i == 99 else ", ")
```

L'expression conditionnelle `valeur_si_vrai if condition else valeur_si_faux`
permet de choisir le separateur a afficher selon qu'on est au **dernier**
element ou non — un motif tres courant pour produire une sortie "propre"
(`00, 01, ..., 99` sans virgule finale).

---

## Exercices et notions travaillees

### `positive_or_negative.py`

- Genere un entier aleatoire entre `-10` et `10`.
- Utilise une structure conditionnelle pour afficher si le nombre est
	positif, negatif ou zero.
- Notion cle: prise de decision simple avec `if/elif/else`.

### `last_digit.py`

- Genere un entier aleatoire et extrait son dernier chiffre.
- Gere le cas des nombres negatifs avec `abs(number) % 10` puis re-signe.
- Notion cle: conditions composees et logique de traitement par cas.

### `print_alphabt.py`

- Parcourt les lettres minuscules de `a` a `z` via leurs codes ASCII.
- Ignore les lettres `e` et `q` avec `continue`.
- Notion cle: boucle + filtrage conditionnel.

### `print_comb2.py`

- Affiche tous les nombres de `00` a `99` avec deux chiffres.
- Gere le separateur de fin pour eviter une virgule finale.
- Notion cle: formatage numerique et gestion de sortie.

### `print_comb3.py`

- Affiche toutes les combinaisons croissantes de deux chiffres differents.
- Utilise des boucles imbriquees pour parcourir toutes les paires valides.
- Notion cle: exploration combinatoire avec boucles imbriquees.

### `print_hexa.py`

- Affiche les nombres de `0` a `98` avec leur representation hexadecimale.
- Utilise la fonction standard `hex(i)`.
- Notion cle: conversion de base et affichage multi-format.

## Competences acquises

- Ecrire des scripts simples et lisibles.
- Decouper un probleme en conditions et parcours iteratifs.
- Produire une sortie conforme a un format strict.