# Core Data Structures (Python Fundamentals)

Ce dossier couvre les structures de donnees de base en Python et leur
manipulation dans des fonctions simples.

## Sujets abordes

- Listes: parcours, acces par index, mise a jour
- Matrices (listes de listes): affichage ligne par ligne
- Tuples: acces partiel et somme positionnelle
- Dictionnaires: ajout, mise a jour, recherche d'une meilleure valeur
- Ensembles (`set`): intersection

## Cours : les structures de donnees de base

### Listes (`list`)

```python
nombres = [10, 20, 30]
print(nombres[0])     # 10
nombres[1] = 99       # modification en place : [10, 99, 30]
```

- Une **liste** est une collection **ordonnee** et **modifiable**
  (*mutable*) d'elements.
- L'**index** commence a `0`. `nombres[-1]` acceae au dernier element.
- Acceder a un index inexistant leve une `IndexError` : il faut donc
  **verifier les bornes** (`0 <= index < len(liste)`) avant d'indexer si
  l'index vient d'une entree externe.

### Matrices (listes de listes)

```python
matrice = [[1, 2, 3], [4, 5, 6]]

for ligne in matrice:
    for valeur in ligne:
        print(valeur, end=" ")
    print()
```

Une matrice est simplement une **liste dont chaque element est lui-meme une
liste**. On la parcourt avec deux boucles `for` imbriquees : la boucle
externe parcourt les lignes, la boucle interne parcourt les valeurs d'une
ligne.

### Tuples (`tuple`)

```python
position = (3, 4)
x, y = position        # "depaquetage" (unpacking)
```

- Un **tuple** ressemble a une liste mais est **immuable** : une fois cree,
  on ne peut pas modifier ses elements (`position[0] = 5` leve une
  `TypeError`).
- Utilise pour des donnees qui forment un **tout coherent** (coordonnees,
  paires cle/valeur...).
- Pour additionner deux tuples element par element, on combine acces par
  index et gestion des tailles differentes :

  ```python
  def add_tuple(t1=(), t2=()):
      a = t1[0] if len(t1) > 0 else 0
      b = t1[1] if len(t1) > 1 else 0
      c = t2[0] if len(t2) > 0 else 0
      d = t2[1] if len(t2) > 1 else 0
      return (a + c, b + d)
  ```

### Dictionnaires (`dict`)

```python
eleve = {"nom": "Alice", "note": 18}

eleve["age"] = 20            # ajout d'une cle
eleve["note"] = 19           # mise a jour d'une cle existante

for cle, valeur in eleve.items():
    print(cle, "->", valeur)
```

- Un **dictionnaire** associe des **cles uniques** a des **valeurs** :
  acces en `O(1)` par cle, contrairement a une recherche dans une liste.
- `dico[cle] = valeur` **ajoute** la cle si elle n'existe pas, ou **met a
  jour** sa valeur si elle existe deja — meme syntaxe pour les deux cas.
- `.items()`, `.keys()`, `.values()` permettent de parcourir respectivement
  les paires, les cles seules, ou les valeurs seules.
- Trouver la cle associee a la plus grande valeur :

  ```python
  def best_score(scores):
      if not scores:
          return None
      return max(scores, key=scores.get)
  ```

  `max(iterable, key=fonction)` applique `fonction` a chaque element pour
  decider lequel est "le plus grand" — ici, `scores.get` donne la valeur
  associee a chaque cle.

### Ensembles (`set`)

```python
a = {1, 2, 3}
b = {2, 3, 4}

print(a & b)    # intersection : {2, 3}
print(a | b)    # union : {1, 2, 3, 4}
print(a - b)    # difference : {1}
```

- Un **ensemble** est une collection **non ordonnee** d'elements
  **uniques** (pas de doublons).
- Tres efficace pour tester l'appartenance (`x in mon_set`) et pour les
  operations ensemblistes (`&`, `|`, `-`).

### Recapitulatif : quelle structure choisir ?

| Besoin | Structure |
|--------|-----------|
| Une sequence ordonnee, modifiable | `list` |
| Une sequence ordonnee, fixe (coordonnees, enregistrement) | `tuple` |
| Associer une cle a une valeur, recherche rapide | `dict` |
| Garantir l'unicite, operations d'ensembles (intersection, union) | `set` |
| Donnees en grille / tableau 2D | `list` de `list` |

---

## Exercices et notions travaillees

### `print_list_integer.py`

- Affiche chaque entier d'une liste sur une ligne.
- Notion cle: iteration directe sur les elements d'une liste.

### `element_at.py`

- Retourne l'element a un index donne, sinon `None` si index invalide.
- Notion cle: controle de bornes avant acces a une liste.

### `replace_in_list.py`

- Remplace l'element a l'index donne, ou laisse la liste intacte si index invalide.
- Notion cle: modification securisee d'une liste en place.

### `print_matrix_integer.py`

- Affiche une matrice d'entiers avec espaces entre colonnes.
- Notion cle: double iteration et formatage d'une structure 2D.

### `add_tuple.py`

- Additionne deux tuples element par element.
- Si un tuple a moins de 2 elements, les valeurs manquantes valent `0`.
- Notion cle: gestion defensive des tailles de tuples.

### `update_dictionary.py`

- Ajoute ou met a jour une cle dans un dictionnaire.
- Notion cle: mutation de dictionnaire avec affectation par cle.

### `best_score.py`

- Retourne la cle associee a la plus grande valeur d'un dictionnaire.
- Retourne `None` pour un dictionnaire vide ou `None`.
- Notion cle: parcours `key/value` et recherche d'un maximum.

### `common_elements.py`

- Retourne les elements communs entre deux ensembles.
- Notion cle: operation d'intersection avec `&`.

## Competences acquises

- Choisir la bonne structure selon le besoin.
- Ecrire des fonctions de manipulation de collections robustes.
- Gagner en precision sur les cas limites (index invalides, structures vides).