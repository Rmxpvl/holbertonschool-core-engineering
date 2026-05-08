# Fonctions et modules en Python

Ce dossier introduit les bases des fonctions, des modules et de l import en Python.
L idee generale est simple : une fonction permet de factoriser un calcul ou un traitement,
et un module permet de regrouper du code reutilisable dans un fichier separé.

## Objectifs du module

Dans cette partie, on apprend a :

- ecrire une fonction simple
- importer une fonction depuis un autre fichier
- utiliser `if __name__ == "__main__":` pour separer l execution directe de l import
- manipuler des valeurs entieres, des chaines et des conversions de base
- comprendre la difference entre definir une fonction et executer un script

## Notions importantes

### 1. Une fonction

Une fonction est un bloc de code reutilisable qui recoit des arguments et peut renvoyer un resultat.
Exemple : une fonction d addition recoit deux nombres et retourne leur somme.

### 2. Un module

Un module est un fichier Python que l on peut importer depuis un autre fichier.
Cela permet de reutiliser du code sans le recopier.

### 3. `if __name__ == "__main__":`

Ce test sert a executer une partie du code seulement quand le fichier est lance directement.
Quand le fichier est importe, cette partie ne doit pas s executer.

### 4. Importer sans `*`

Le caractere `*` permettrait d importer tout un module, mais ce module demande d importer de maniere explicite.
On doit donc ecrire le nom exact de la fonction ou de la variable utilisee.

## Exercices du dossier

### `add_0.py`

Ce premier exercice definit une fonction `add(a, b)` qui renvoie la somme de `a` et `b`.
Le bloc principal affiche ensuite le resultat de `1 + 2` sous la forme `1 + 2 = 3`.

But pedagogique : comprendre la definition d une fonction simple et l affichage d un resultat.

### `simple_add.py`

Ce programme contient aussi une fonction `add(a, b)`.
Quand le fichier est execute directement, il affiche `8` en appelant `add(3, 5)`.

But pedagogique : separer la logique d une fonction et son execution dans un script.

### `add.py`

Ce fichier importe la fonction `add` depuis `add_0.py`.
Il montre comment utiliser une fonction definie dans un autre module.

But pedagogique : apprendre a importer une fonction precise depuis un autre fichier.

### `calculator_1.py`

Ce module contient quatre fonctions : `add`, `sub`, `mul` et `div`.
Chaque fonction effectue une operation arithmetique de base.

Details :

- `add(a, b)` retourne `a + b`
- `sub(a, b)` retourne `a - b`
- `mul(a, b)` retourne `a * b`
- `div(a, b)` retourne `int(a / b)`

But pedagogique : regrouper plusieurs fonctions dans un meme module reutilisable.

### `calculation.py`

Ce script importe les quatre fonctions de `calculator_1.py`.
Il fixe `a = 10` et `b = 5`, puis affiche les resultats au format :

- `10 + 5 = 15`
- `10 - 5 = 5`
- `10 * 5 = 50`
- `10 / 5 = 2`

But pedagogique : combiner import, calculs et affichage formatte.

### `print_last_digit.py`

Cette fonction recoit un nombre entier et affiche son dernier chiffre.
Elle renvoie aussi ce dernier chiffre.

Principe utilise :

- `abs(number)` pour travailler avec la valeur absolue
- `% 10` pour recuperer le dernier chiffre
- `print(..., end="")` pour afficher sans retour a la ligne

But pedagogique : utiliser une fonction qui affiche et retourne une valeur.

### `islower.py`

Cette fonction verifie si un caractere est une minuscule entre `a` et `z`.
Elle utilise `ord()` pour comparer la valeur ASCII du caractere.

Retour :

- `True` si le caractere est une lettre minuscule
- `False` sinon

But pedagogique : manipuler les codes ASCII et les tests conditionnels.

### `uppercase.py`

Cette fonction prend une chaine de caracteres et affiche la version en majuscules.
Elle parcourt chaque caractere et convertit les lettres minuscules avec `chr(ord(i) - 32)`.

But pedagogique : parcourir une chaine et transformer les caracteres un par un.

### `pow.py`

Cette fonction calcule une puissance sans utiliser directement l operateur `**`.
Elle gere aussi les exposants negatifs en renvoyant l inverse du resultat.

But pedagogique : comprendre les boucles, la multiplication repetee et le traitement des cas speciaux.

### `variable_load_5.py`

Ce fichier definit simplement la variable `a`.
Il sert de source de donnees pour un autre module.

But pedagogique : montrer qu un module peut contenir une simple variable importable.

### `variable_load.py`

Ce script importe `a` depuis `variable_load_5.py` et affiche sa valeur.
Il doit rester silencieux quand il est importe comme module.

But pedagogique : importer une variable depuis un autre fichier sans utiliser `*`.

### `test.py`

Ce fichier affiche les indices d une chaine `abcd` avec une boucle `for`.
L affichage attendu est `0`, `1`, `2`, `3`.

But pedagogique : comprendre `range(len(...))` et le parcours d une chaine par indice.

### `test_import.py`

Ce script montre un import de module simple : `import simple_add`.
Il sert a illustrer la difference entre importer un module entier et importer une fonction precise.

But pedagogique : comprendre la forme la plus basique d import Python.

## Methode pour resoudre ce type d exercice

1. Identifier ce que le programme doit afficher ou retourner.
2. Choisir si le code doit definir une fonction, un module ou un script executable.
3. Proteger le code executable avec `if __name__ == "__main__":` si necessaire.
4. Tester le fichier directement pour verifier le comportement attendu.
5. Verifier ensuite que l import du fichier ne lance pas le programme principal.

## Resume

Ce module apprend les bases du code reutilisable en Python.
La progression va de la fonction simple vers l import de fonctions, de modules et de variables,
avec une attention particuliere au comportement d un fichier lorsqu il est importe ou execute.