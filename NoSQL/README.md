# 📚 NoSQL - MongoDB

## 📌 Description

Ce projet introduit les bases des bases de données **NoSQL**, en particulier **MongoDB**.  
Contrairement aux bases relationnelles (SQL), MongoDB stocke les données sous forme de **documents JSON-like** dans des **collections**.

L'objectif est de comprendre :

- comment interagir avec MongoDB  
- comment écrire des scripts dans le shell MongoDB  
- les opérations CRUD (Create, Read, Update, Delete)  

---

## 🧠 Concepts clés

- **NoSQL** : bases de données non relationnelles  
- **MongoDB** : base de données orientée documents  
- **Collection** : équivalent d’une table en SQL  
- **Document** : équivalent d’une ligne (format JSON)  
- **Shell MongoDB** : interface en ligne de commande  

### CRUD operations

- Create  
- Read  
- Update  
- Delete  

---

## ⚙️ Installation

### Installer MongoDB (Ubuntu)

```bash
sudo apt update
sudo apt install -y mongodb
```
### Lancer MongoDB :
```bash
sudo service mongodb start
```

---

## 🚀 Utilisation

### Lancer le shell MongoDB :
```bash
mongo
```

---

###  Exécuter un script :
```bash
cat fichier.js | mongo
```

---

## 📂 Structure du projet
NoSQL/
├── 0-list_databases
├── 1-use_or_create_database
├── 2-insert
├── 3-all
├── 4-match
├── 5-count
├── 6-update
├── 7-delete
└── README.md

---

## 📝 Exemples

### 🔹 Lister toutes les bases de données
```JavaScript
db.adminCommand('listDatabases').databases.forEach(d => print(d.name));
```
### 🔹 Utiliser une base de données
```JavaScript
use my_db
```
### 🔹 Insérer un document
```JavaScript
db.collection.insert({ name: "John", age: 30 });
```
### 🔹 Lire les documents
```JavaScript
db.collection.find();
```
### 🔹 Mettre à jour
```JavaScript
db.collection.update({ name: "John" }, { $set: { age: 31 } });
```
### 🔹 Supprimer
```JavaScript
db.collection.remove({ name: "John" });
```

---

## ⚠️ Bonnes pratiques
- Toujours tester les scripts dans le shell avant
- Ne pas utiliser les commandes interactives (show dbs) dans les scripts
- Utiliser print() pour afficher les résultats
- Respecter les contraintes du projet

---

## 📊 Différences SQL vs NoSQL

| SQL          | NoSQL (MongoDB) |
|--------------|-----------------|
| Tables       | Collections     |
| Rows         | Documents       |
| Schema fixe  | Schema flexible |
| JOIN         | Pas de JOIN natif |