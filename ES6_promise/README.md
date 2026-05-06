# 📘 JavaScript Asynchrone : Promises, async/await et gestion des erreurs

## 🎯 Objectifs du projet

À la fin de ce projet, vous devez être capable d’expliquer et d’utiliser sans aide externe :

- Les Promises (ce que c’est, pourquoi et comment les utiliser)
- Les méthodes `then`, `catch`, `finally`
- Les méthodes principales de l’objet Promise
- La gestion des erreurs avec `throw` et `try/catch`
- L’opérateur `await`
- Les fonctions `async`

---

# 1. 🔵 Les Promises

## 📌 Définition
Une **Promise** est un objet JavaScript qui représente une opération asynchrone (qui se termine dans le futur).

Elle peut être dans 3 états :
- `pending` : en attente
- `fulfilled` : réussite
- `rejected` : échec

## 📌 Pourquoi utiliser les Promises ?
- Éviter le "callback hell"
- Rendre le code plus lisible
- Gérer les erreurs proprement

## 📌 Exemple
```js
const promise = new Promise((resolve, reject) => {
  let success = true;

  if (success) {
    resolve("Succès !");
  } else {
    reject("Erreur !");
  }
});
```
---

## 2. 🔗 then, catch et finally
📌 then()

Permet de gérer le succès d’une Promise.

```js
promise.then(result => {
  console.log(result);
});
```

### 📌 catch()

Permet de gérer les erreurs.
```js
promise.catch(error => {
  console.log(error);
});
```
### 📌 finally()

S’exécute dans tous les cas.
```js
promise.finally(() => {
  console.log("Terminé");
});
```
---

## 3. ⚙️ Méthodes de l’objet Promise
### 📌 Promise.all()

Attend que toutes les Promises réussissent.
```js
Promise.all([p1, p2]).then(results => {
  console.log(results);
});
```

### 📌 Promise.race()

Retourne la première Promise terminée.

Promise.race([p1, p2]);

### 📌 Promise.allSettled()

Retourne le résultat de toutes les Promises (réussies ou non).

Promise.allSettled([p1, p2]);

### 📌 Promise.any()

Retourne la première Promise réussie.

Promise.any([p1, p2]);

---

## 4. 🚨 try / catch / throw

### 📌 try/catch

Permet de gérer les erreurs.
```js
try {
  console.log("OK");
} catch (error) {
  console.log("Erreur :", error);
}
```

### 📌 throw

Permet de créer une erreur volontairement.

throw new Error("Une erreur s'est produite");

---

## 5. ⏳ async / await

### 📌 async

Une fonction async retourne automatiquement une Promise.
```js
async function hello() {
  return "Bonjour";
}
```

## 📌 await

Permet d’attendre une Promise.
```js
async function test() {
  const result = await promise;
  console.log(result);
}
```

### 📌 Exemple complet
```js
function wait() {
  return new Promise(resolve => {
    setTimeout(() => resolve("Terminé"), 2000);
  });
}

async function run() {
  try {
    console.log("Début");
    const result = await wait();
    console.log(result);
  } catch (error) {
    console.log("Erreur :", error);
  }
}

run();
```

---

## 🧠 Résumé
- Promise → valeur future
- then → succès
- catch → erreur
- finally → toujours exécuté
- Promise.all / race / any / allSettled → gestion multiple
- try/catch → gestion des erreurs
- async/await → syntaxe simplifiée des Promises

---

## 🚀 Conclusion

Les Promises et async/await sont essentiels pour gérer le code asynchrone en JavaScript de manière propre, lisible et efficace.