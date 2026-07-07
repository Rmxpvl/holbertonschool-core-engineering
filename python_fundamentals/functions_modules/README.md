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

## Cours : fonctions et organisation en modules

### Definir et appeler une fonction

```python
def add(a, b):
    return a + b

resultat = add(1, 2)   # resultat = 3
```

- `def nom(parametres):` definit une fonction. Le mot-cle `return` renvoie
  une valeur a l'appelant et **termine** immediatement la fonction.
- Une fonction sans `return` retourne implicitement `None`.
- Donner des **noms explicites** aux parametres et a la fonction rend le
  code auto-documente : `add(a, b)` est plus clair que `f(x, y)`.

### `if __name__ == "__main__":`

```python
def add(a, b):
    return a + b

if __name__ == "__main__":
    print("1 + 2 = {}".format(add(1, 2)))
```

- `__name__` est une variable **automatiquement definie** par Python :
  - elle vaut `"__main__"` quand le fichier est **execute directement**
    (`python3 fichier.py`) ;
  - elle vaut le **nom du module** quand le fichier est **importe**
    (`import fichier`).
- Ce garde-fou permet d'avoir un fichier qui est a la fois :
  - une **bibliotheque** de fonctions reutilisables (quand on l'importe), et
  - un **script executable** (quand on le lance directement) —
    sans que le code de demonstration s'execute lors de l'import.

### Importer depuis un autre fichier

```python
# add_0.py
def add(a, b):
    return a + b
```

```python
# add.py
from add_0 import add

print("1 + 2 = {}".format(add(1, 2)))
```

- `from module import nom` importe **un element precis** (une fonction,
  une classe, une variable) depuis un module — ici, le fichier `add_0.py`
  (sans l'extension `.py`) est vu comme le module `add_0`.
- `import module` importe le **module entier** ; on accede alors a ses
  elements via `module.nom` (ex : `import simple_add` puis
  `simple_add.add(1, 2)`).

### Regrouper plusieurs fonctions dans un module

```python
# calculator_1.py
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b
```

```python
# calculation.py
from calculator_1 import add, sub, mul, div

a, b = 10, 5
print("{} + {} = {}".format(a, b, add(a, b)))
print("{} / {} = {}".format(a, b, div(a, b)))
```

Regrouper des fonctions liees dans un meme fichier (ici, des operations
arithmetiques) permet de les **importer ensemble** et de garder le code
**organise par theme**.

### Importer une variable

```python
# variable_load_5.py
a = 98
```

```python
# variable_load.py
from variable_load_5 import a

print("a = {}".format(a))
```

L'import ne se limite pas aux fonctions : on peut importer **n'importe quel
nom defini au niveau du module** — variable, constante, classe...

### Algorithmes simples sans operateurs "magiques"

```python
def pow(a, b):
    if b < 0:
        return 1 / pow(a, -b)
    resultat = 1
    for _ in range(b):
        resultat *= a
    return resultat
```

Reimplementer `a ** b` avec une boucle est un exercice classique pour
s'entrainer a **traduire une definition mathematique en algorithme** :
"`a` puissance `b`" = "multiplier `a` par lui-meme `b` fois".

### Recapitulatif : organiser son code

```
module_a.py  (def f1, def f2, variable X)
      │
      │  import module_a
      │  from module_a import f1, X
      ▼
script.py    (if __name__ == "__main__": orchestre les appels)
```

- **Module** = un fichier `.py` que l'on peut importer.
- **Script** = un fichier `.py` que l'on execute directement, generalement
  protege par `if __name__ == "__main__":`.
- Un meme fichier peut jouer les deux roles.

---

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