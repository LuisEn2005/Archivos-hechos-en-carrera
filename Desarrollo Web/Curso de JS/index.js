let saludo = "Hello World";


console.log(saludo);
//tipos de datos / el dato var puede ser mutable
var numero = 5;

console.log(numero);

numero = "webada";

console.log(numero);

saludo = "mamadas";

let objeto = {
    numero,
    saludo,
    nombre: "Luis",
}

console.log(objeto);

function administrador(objeto){
    objeto.numero = "mmgvo";
    objeto.nombre = "Juan";
    console.log(objeto)
}
// null significa ausencia de valor;
let y = null;
console.log(y);

administrador(objeto);

let array = ["mamaguevo","pendejo","idiota"];

console.log(array[2]);

let valor1, valor2;

function suma(valor1,valor2){
    let respuesta = valor1 + valor2;
    if(valor1 != valor2){
        console.log("huebadas")
    }
    return respuesta;
}

console.log(suma(4,8));
