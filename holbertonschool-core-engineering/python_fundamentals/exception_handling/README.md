# Exception Handling (Python Fundamentals)

Ce dossier introduit la gestion d'erreurs en Python pour rendre les scripts
plus robustes face aux entrees invalides ou aux operations risquant d'echouer.

## Sujets abordes

- Lever explicitement des exceptions (`raise`)
- Blocs `try/except`
- Bloc `finally`
- Capture d'exceptions specifiques (`TypeError`, `ValueError`, `IndexError`,
  `ZeroDivisionError`, `NameError`)
- Retour de valeurs de statut apres tentative d'operation

## Cours : comprendre les exceptions

### Qu'est-ce qu'une exception ?

Quand Python rencontre une erreur pendant l'execution (et non a la
compilation, puisque Python n'en a pas), il **leve une exception** : le
programme s'interrompt immediatement et "remonte" la pile d'appels jusqu'a
trouver un endroit qui gere cette erreur, ou jusqu'a planter completement en
affichant un *traceback*.

```python
>>> int("abc")
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: 'abc'
```

### `try` / `except` : intercepter une erreur

```python
try:
    valeur = int(entree_utilisateur)
except ValueError:
    print("Ce n'est pas un nombre valide")
```

- Le code "a risque" est place dans le bloc `try`.
- Si une exception du type indique se produit, l'execution **saute
  directement** dans le bloc `except` correspondant : le reste du `try`
  n'est pas execute.
- Si aucune exception ne se produit, le(s) bloc(s) `except` sont ignores.

### Capturer plusieurs types d'exceptions

```python
try:
    resultat = a / b
except (TypeError, ZeroDivisionError):
    resultat = None
```

On peut grouper plusieurs types dans un tuple, ou ecrire plusieurs blocs
`except` successifs si on veut un traitement different par type.

### `raise` : lever une exception soi-meme

```python
def diviser(a, b):
    if b == 0:
        raise ValueError("b ne peut pas etre zero")
    return a / b
```

`raise` permet de **signaler explicitement** qu'une situation est anormale,
plutot que de laisser la fonction retourner une valeur incoherente (comme
`None` ou `-1`) que l'appelant pourrait oublier de verifier.

### `finally` : le bloc qui s'execute toujours

```python
try:
    resultat = a / b
except ZeroDivisionError:
    resultat = None
finally:
    print("Resultat :", resultat)
```

Le bloc `finally` s'execute **dans tous les cas** : que le `try` reussisse,
qu'une exception soit attrapee, ou meme si une exception non capturee
remonte plus haut. Il est ideal pour des actions de nettoyage (fermer un
fichier, afficher un etat final...).

### Quelques exceptions courantes

| Exception | Quand elle survient |
|-----------|----------------------|
| `TypeError` | Operation appliquee a un type incompatible (ex: `"a" + 1`) |
| `ValueError` | Valeur du bon type mais invalide (ex: `int("abc")`) |
| `IndexError` | Acces a un index de liste hors limites |
| `ZeroDivisionError` | Division ou modulo par zero |
| `NameError` | Utilisation d'une variable/nom non defini |

### Schema general

```
try:
    bloc a risque
except TypeErreur1:
    traitement specifique 1
except (TypeErreur2, TypeErreur3):
    traitement specifique 2
finally:
    toujours execute
```

---

## Exercices et notions travaillees

### `raise_exception.py`

- Leve volontairement une `TypeError`.
- Notion cle: signaler explicitement une erreur plutot que la masquer.

### `raise_exception_msg.py`

- Leve une `NameError` avec un message personnalise.
- Notion cle: fournir un message utile avec l'exception.

### `safe_print_integer.py`

- Tente d'afficher une valeur comme entier via `{:d}`.
- Retourne `True` si succes, `False` en cas de `TypeError` ou `ValueError`.
- Notion cle: encapsuler un comportement potentiellement fragile.

### `safe_print_list.py`

- Tente d'afficher `x` elements d'une liste.
- Interrompt proprement l'affichage en cas de depassement d'index.
- Retourne le nombre d'elements effectivement affiches.
- Notion cle: gerer les limites de liste sans crash.

### `safe_print_list_integers.py`

- Affiche jusqu'a `x` elements en ne gardant que ceux convertibles en entier.
- Ignore les elements non conformes et retourne le nombre imprimes.
- Notion cle: filtrage tolerant aux erreurs pendant une boucle.

### `safe_print_division.py`

- Tente une division `a / b`.
- Attrape `TypeError` et `ZeroDivisionError`.
- Affiche toujours le resultat (ou `None`) dans un bloc `finally`.
- Notion cle: garantir une action de fin, que l'operation reussisse ou non.

## Competences acquises

- Anticiper les erreurs les plus frequentes.
- Ecrire des fonctions qui echouent proprement.
- Distinguer ce qui doit etre capture, ignore, signale ou retourne.
