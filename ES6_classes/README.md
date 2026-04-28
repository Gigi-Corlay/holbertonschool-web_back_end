# ES6 Classes - Learning Objectives

## 📚 Project Overview
At the end of this project, you should be able to explain the following concepts clearly, without the help of Google.

This project introduces the fundamentals of **ES6 Classes**, inheritance, static methods, and metaprogramming concepts in JavaScript.

---

## 1. How to define a Class
A class in JavaScript is a blueprint for creating objects with shared properties and methods.

```js
class Person {
  constructor(name) {
    this.name = name;
  }
}
```

---

## 2. How to add methods to a class

Methods are functions defined inside a class that describe behaviors.

```js
class Person {
  constructor(name) {
    this.name = name;
  }

  sayHello() {
    return `Hello, my name is ${this.name}`;
  }
}
```

---

## 3. Why and how to add a static method to a class

Static methods belong to the class itself, not to instances of the class.

They are used for utility functions or operations that do not depend on instance data.

```js
class MathHelper {
  static add(a, b) {
    return a + b;
  }
}

MathHelper.add(2, 3); // 5
```

---

## 4. How to extend a class from another

Inheritance allows a class to reuse and extend the behavior of another class.

```js
class Animal {
  constructor(name) {
    this.name = name;
  }

  speak() {
    return `${this.name} makes a sound`;
  }
}

class Dog extends Animal {
  speak() {
    return `${this.name} barks`;
  }
}
```

---

## 5. Metaprogramming and Symbols

Metaprogramming allows you to modify or control the behavior of code dynamically.

Symbols are unique identifiers often used to avoid property name conflicts.

```js
const sym = Symbol('id');

const user = {
  name: 'John',
  [sym]: 123,
};
```

Symbols are not enumerable in loops, making them useful for hidden properties.

---


##  🚀 Summary

After completing this project, you should understand:
- How to create and structure ES6 classes
- How to add instance and static methods
- How inheritance works with extends
- How symbols enable safer property definitions
- Basic metaprogramming concepts in JavaScript
