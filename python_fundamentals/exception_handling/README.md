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
