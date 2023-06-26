/*
Las funciones se ocupan para realizar procesos repetitivos.
Por lo general las funciones siempre deben retornar algo.
*/

//! Funciones llamadas en el mismo archivo
// Ejemplo funcion sin return
function welcome(nom){
    console.log(`Welcome, ${nom}`);
}

let nombre = 'Sugo'
welcome(nombre);


// Ejemplo funcion con retorno
function mult (a, b){
    return a * b;
}
console.log(`funcion suma: ${mult(2, 3)}`);

function div (a, b){
    return a / b;
}
console.log(div(30, 3));

//! Funciones llamadas desde otro archivo
exports.suma_para_call = function(a, b) {
    return a + b;
};
    
    exports.resta_para_call = function(a, b) {
    return a - b;
};