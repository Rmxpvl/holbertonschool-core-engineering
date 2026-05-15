# Fonctions et Modules (Python Fundamentals)

Ce dossier introduit la creation de fonctions reutilisables et l'organisation
du code en modules Python importables.

## Sujets abordes

- Definition de fonctions et retour de valeurs
- Imports explicites depuis d'autres fichiers
- Bloc `if __name__ == "__main__":` pour separer import et execution
- Fonctions arithmetiques simples
- Manipulation de caracteres avec `ord` et `chr`
- Import d'une variable depuis un module

## Exercices et notions travaillees

### `add_0.py`

- Definit `add(a, b)` qui retourne la somme de deux entiers.
- Notion cle: ecriture d'une fonction minimale.

### `simple_add.py`

- Reprend la fonction `add` et l'execute dans un bloc principal.
- Notion cle: proteger le code executable avec `if __name__ == "__main__":`.

### `add.py`

- Importe `add` depuis `add_0.py` puis affiche `1 + 2 = 3`.
- Notion cle: import de fonction ciblee.

### `calculator_1.py`

- Regroupe 4 fonctions: `add`, `sub`, `mul`, `div`.
- Notion cle: centraliser des operations dans un module reutilisable.

### `calculation.py`

- Importe les fonctions de `calculator_1.py` et affiche les resultats pour `a=10`, `b=5`.
- Notion cle: orchestrer plusieurs fonctions importees dans un script.

### `print_last_digit.py`

- Affiche et retourne le dernier chiffre d'un entier (y compris negatif).
- Notion cle: combiner calcul, affichage et valeur de retour.

### `islower.py`

- Verifie si un caractere est une lettre minuscule (`a` a `z`) via ASCII.
- Notion cle: test de plage avec `ord`.

### `uppercase.py`

- Convertit et affiche une chaine en majuscules, caractere par caractere.
- Notion cle: transformation conditionnelle de caracteres.

### `pow.py`

- Calcule `a` puissance `b` avec une boucle (inclut le cas `b < 0`).
- Notion cle: repetition algorithmique sans appeler `**` directement.

### `variable_load_5.py`

- Defini une variable globale `a = 98`.
- Notion cle: exposer une valeur importable.

### `variable_load.py`

- Importe `a` depuis `variable_load_5.py` puis l'affiche.
- Notion cle: import explicite de variable.

### `test.py`

- Affiche les index d'une chaine avec `range(len(x))`.
- Notion cle: iteration par indice.

### `test_import.py`

- Fait un import de module simple (`import simple_add`).
- Notion cle: forme basique d'import Python.

## Competences acquises

- Structurer du code pour qu'il soit reutilisable.
- Comprendre la difference entre un module importe et un script execute.
- Maitriser les imports de fonctions et de variables.