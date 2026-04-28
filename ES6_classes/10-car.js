export default class Car {
    constructor(brand, motor, color) {
        this._brand = brand;
        this._motor = motor;
        this._color = color;

      // Symbol utilisé pour instancier dynamiquement la bonne classe
        const ctor = Symbol.for('ctor');

        this[ctor] = function () {
            return new this.constructor(this._brand, this._motor, this._color);
        };
    }

    cloneCar() {
        const ctor = Symbol.for('ctor');
        return this[ctor]();
    }
}
