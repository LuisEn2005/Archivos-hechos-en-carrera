console.log("bola comes");

var primeravariable = 5;
console.log("usando mi primera variable llamada " + primeravariable);
var primeravariable = 10;
console.log("usando mi primera variable llamada " + primeravariable);

var booleano = false;
console.log(booleano);

let mivariable;

const miconstante = 3;
console.log(miconstante)
/* cambiar de valor a un numero constante, es ilegal y ocasiona un error
miconstante = 25; 
console.log(miconstante)
*/

var operador1 = 5;
var operador2 = 7;

var resultado = operador1 + operador2;

console.log("el resultado de los operadores es " + resultado)

//Condicionales

let miNumero1 = 9;

/* let resultadopregunta = numero1 == 6

console.log(resultadopregunta)
*/
/* las (===) hacen una igualdad estricta la cual, 9 == "9" es verdadero, pero 9 === "9" falso,
porque son tipos de datos diferentes */
/* <=, >=, <, >, &&(and), ||(or), +=, -=, etc.*/

/* if (miNumero1 === "9") {
    console.log("es 9")
}
else {
    console.log("no es 9")
} */

let miNumero2 = 5;

if (miNumero2 > 0){
    console.log('Mi numero es positivo');
}
else if (miNumero2 === 0){
    console.log('Mi numero es cero');
}
else{
    console.log("Mi numero es negativo");
}

/* 
let contador = 0;

while(contador < 5){
    console.log(contador);
    contador = contador + 1;
} */

for(let contador = 0;contador < 10;contador++){
    console.log(contador);
}

function saludar(name){
    console.log("Hola "+ name);
}

//saludar("Pepe");

function multiplicar2nums(num1,num2){
    let multiplicacion = num1 * num2;
    return multiplicacion;
}
//console.log(multiplicar2nums(5,5));

let miArreglo = ["David","Fernando","Kevin"];

function lector(miArreglo){
    for(let i = 0;i < 3;i++){
        console.log(miArreglo[i]);
    }
}

lector(miArreglo);

let persona = {
    nombre: "Carlitos",
    edad: 24,
    masculino: true,
};
console.log(persona);

persona.nombre = "Cabeza de huevo";
console.log(persona);

/*¨
let persona2 = {
    nombre: "Celia",
    edad: 17,
    masculino: false,
};
*/
