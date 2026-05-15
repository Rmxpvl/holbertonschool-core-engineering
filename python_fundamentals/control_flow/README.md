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