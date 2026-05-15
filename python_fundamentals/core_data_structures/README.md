# Core Data Structures (Python Fundamentals)

Ce dossier couvre les structures de donnees de base en Python et leur
manipulation dans des fonctions simples.

## Sujets abordes

- Listes: parcours, acces par index, mise a jour
- Matrices (listes de listes): affichage ligne par ligne
- Tuples: acces partiel et somme positionnelle
- Dictionnaires: ajout, mise a jour, recherche d'une meilleure valeur
- Ensembles (`set`): intersection

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