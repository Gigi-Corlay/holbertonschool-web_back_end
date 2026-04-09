# 📘 0-async_generator

## 📌 Description

Ce module implémente un **générateur asynchrone** en Python.  
Il permet de produire une séquence de valeurs de manière **asynchrone**, en utilisant les mots-clés `async` et `await`.

---

## 🎯 Objectif

L’objectif est de comprendre :

- Les **fonctions asynchrones** (`async def`)
- L’utilisation de `await`
- Le concept de **générateur asynchrone** (`yield` dans une fonction async)
- La gestion du temps avec `asyncio`

---

## ⚙️ Fonctionnalité

Le fichier contient une fonction :

```python
async def async_generator():
```
**Cette fonction :**
- Attend 1 seconde à chaque itération (`await asyncio.sleep(1)`)
- Génère un nombre aléatoire
- Répète cela 10 fois
- Utilise `yield` pour retourner chaque valeur

## 🧠 Concepts clés
**🔹 Fonction asynchrone*
Une fonction définie avec async def permet d’exécuter du code de manière non bloquante.

```python
async def my_function():
    await asyncio.sleep(1)
```

### 🔹 await
Le mot-clé await permet d’attendre le résultat d’une opération asynchrone sans bloquer le programme.

### 🔹 Générateur asynchrone

Un générateur asynchrone est une fonction qui utilise :
```python
async def
yield
```
👉 Cela permet de produire des valeurs une par une dans un contexte asynchrone.

### 🔹 asyncio
Le module asyncio permet de gérer les tâches asynchrones en Python.

**Exemple :**

import asyncio
await asyncio.sleep(1)
▶️ Exemple d’utilisation
import asyncio
```python
async def main():
    async for value in async_generator():
        print(value)

asyncio.run(main())
```

---

## 📈 Comportement
Le programme affiche un nombre aléatoire toutes les secondes
Il s’exécute sans bloquer les autres tâches asynchrones

---

## 🧩 Cas d’usage
**Les générateurs asynchrones sont utiles pour :**
- Lire des données en streaming
- Traiter des API progressivement
- Gérer de gros volumes de données sans tout charger en mémoire

---

## 📚 Ressources
- Documentation officielle Python : asyncio
- PEP 525 – Asynchronous Generators