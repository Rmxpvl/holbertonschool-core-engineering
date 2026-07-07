# File Handling (Python Advanced)

Ce dossier introduit la **manipulation de fichiers texte** en Python :
lecture, écriture et ajout de contenu, en respectant les bonnes pratiques
(`with`, encodage, valeurs de retour).

---

## Sommaire

1. [Ouvrir un fichier : la fonction `open`](#1-ouvrir-un-fichier--la-fonction-open)
2. [Le bloc `with` : pourquoi et comment](#2-le-bloc-with--pourquoi-et-comment)
3. [Lire un fichier](#3-lire-un-fichier)
4. [Écrire dans un fichier](#4-écrire-dans-un-fichier)
5. [Ajouter du contenu (append)](#5-ajouter-du-contenu-append)
6. [Exercices et notions travaillées](#6-exercices-et-notions-travaillées)
7. [Pièges fréquents](#7-pièges-fréquents)
8. [Pour aller plus loin](#8-pour-aller-plus-loin)

---

## 1. Ouvrir un fichier : la fonction `open`

```python
file = open(filename, mode, encoding="utf-8")
```

`open()` retourne un objet **fichier** sur lequel on peut appeler des
méthodes (`read`, `write`, `readlines`...). Le paramètre `mode` indique
**ce que l'on a le droit de faire** :

| Mode | Signification | Effet si le fichier existe déjà | Effet si le fichier n'existe pas |
|------|----------------|----------------------------------|-------------------------------------|
| `"r"` | Lecture (*read*) | Lit le contenu | `FileNotFoundError` |
| `"w"` | Écriture (*write*) | **Écrase tout le contenu** | Crée le fichier |
| `"a"` | Ajout (*append*) | Ajoute à la fin, sans rien effacer | Crée le fichier |
| `"rb"` / `"wb"` | Lecture/écriture **binaire** | (utilisé pour Pickle, images...) | – |

`encoding="utf-8"` garantit que les caractères accentués (`é`, `à`, `ç`...)
sont lus/écrits correctement, quel que soit le système d'exploitation.

---

## 2. Le bloc `with` : pourquoi et comment

```python
with open(filename, "r", encoding="utf-8") as file:
    contenu = file.read()
# ici, le fichier est déjà fermé automatiquement
```

- `with` est un **gestionnaire de contexte** : il garantit que
  `file.close()` est appelé **automatiquement**, même si une exception se
  produit dans le bloc.
- Sans `with`, il faudrait écrire :

  ```python
  file = open(filename, "r", encoding="utf-8")
  try:
      contenu = file.read()
  finally:
      file.close()
  ```

- **Règle pratique : toujours utiliser `with open(...) as file:` pour
  manipuler un fichier.** Un fichier non fermé peut provoquer des pertes de
  données (écriture non "flushée") ou épuiser les descripteurs de fichiers
  du système.

---

## 3. Lire un fichier

```python
def read_file(filename=""):
    """Read a UTF-8 text file and print its content to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end="")
```

- `file.read()` lit **tout le contenu** du fichier sous forme d'une seule
  chaîne de caractères.
- `print(..., end="")` : par défaut, `print` ajoute un retour à la ligne
  (`\n`) à la fin. Comme le contenu du fichier contient déjà ses propres
  retours à la ligne, on utilise `end=""` pour ne pas en rajouter un
  superflu.

### Autres façons de lire

| Méthode | Retourne |
|---------|----------|
| `file.read()` | Tout le fichier sous forme d'une seule chaîne |
| `file.readline()` | Une seule ligne (jusqu'au `\n`) |
| `file.readlines()` | Une liste de chaînes, une par ligne |
| `for line in file:` | Itère ligne par ligne (efficace pour les gros fichiers) |

---

## 4. Écrire dans un fichier

```python
def write_file(filename="", text=""):
    """write a UTF-8 string to a text file and return number of characters."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
```

- Le mode `"w"` **écrase** le contenu existant du fichier (ou le crée s'il
  n'existe pas). À utiliser quand on veut repartir d'un fichier vide.
- `file.write(text)` retourne le **nombre de caractères écrits** — c'est
  cette valeur que la fonction retourne directement (`return file.write(...)`),
  sans variable intermédiaire.

---

## 5. Ajouter du contenu (append)

```python
def append_write(filename="", text=""):
    """appends a string and return number of characters"""
    with open(filename, "a", encoding='utf-8') as file:
        return file.write(text)
```

- Le mode `"a"` (*append*) place le curseur d'écriture **à la fin** du
  fichier existant : le contenu déjà présent est conservé, et `text` est
  ajouté après.
- Si le fichier n'existe pas encore, `"a"` le crée (comme `"w"`).

### `"w"` vs `"a"` en un coup d'œil

```
Fichier existant : "Bonjour\n"

open(f, "w") puis write("Salut")  -> contenu final : "Salut"        (écrasé)
open(f, "a") puis write("Salut")  -> contenu final : "Bonjour\nSalut" (ajouté)
```

---

## 6. Exercices et notions travaillées

| Fichier | Fonction | Notion clé |
|---------|----------|------------|
| `read_file.py` | `read_file(filename="")` | Lire et afficher tout le contenu d'un fichier avec `with` + `read()` |
| `write_file.py` | `write_file(filename="", text="")` | Écraser/créer un fichier et retourner le nombre de caractères écrits |
| `append_write.py` | `append_write(filename="", text="")` | Ajouter du texte à la fin d'un fichier sans perdre son contenu |

Ces trois fonctions forment un mini-cycle complet : créer un fichier
(`write_file`), y ajouter du contenu (`append_write`), puis vérifier son
contenu (`read_file`).

---

## 7. Pièges fréquents

| Erreur | Conséquence | Solution |
|--------|-------------|----------|
| Ouvrir en mode `"w"` un fichier qu'on voulait juste compléter | Le contenu précédent est **perdu** | Utiliser `"a"` pour ajouter, `"w"` uniquement pour repartir de zéro |
| Oublier `with` / `close()` | Données pas écrites sur disque, fichiers "verrouillés" | Toujours utiliser `with open(...) as file:` |
| Oublier `encoding="utf-8"` | `UnicodeDecodeError` ou caractères mal affichés selon l'OS | Toujours préciser l'encodage pour les fichiers texte |
| Appeler `read()` deux fois sur le même fichier | La deuxième fois retourne `""` (le curseur est à la fin) | Ré-ouvrir le fichier, ou utiliser `file.seek(0)` |
| Lire un fichier qui n'existe pas en mode `"r"` | `FileNotFoundError` | Vérifier l'existence du fichier ou capturer l'exception |

---

## 8. Pour aller plus loin

- **`pathlib`** : API orientée objet moderne pour manipuler des chemins de
  fichiers (`Path("dossier") / "fichier.txt"`).
- **`os.path`** : fonctions historiques pour vérifier l'existence
  (`os.path.exists`), joindre des chemins (`os.path.join`)...
- Ce projet est la base des projets **`python-serialization`** (JSON,
  Pickle, CSV, XML) et **`python-object_relational_mapping`**, qui
  manipulent eux aussi des fichiers, mais avec des formats structurés.
