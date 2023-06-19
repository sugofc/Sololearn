/*
Operador Ternario sirve como una alternativa al tipico if, else
*/

// if - else
let balance = 250000;
let retirar = 300000;

balance = (retirar > balance) ? 'No hay suficiente dinero' : balance-retirar;
console.log(balance);


// if - else - if
let a = 1; b = 3; c = 2 

result = (a > b) ? 'SI' : (a < c) ? 'SI!' : 'NO2'
console.log(result)