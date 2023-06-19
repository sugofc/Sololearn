/*
Cosas basicas de JS
*/

//^ Prints
console.log('test');
console.log(2);
console.log("salto \nde \nlinea"); // \n saltar linea
console.log("\ttabulacion"); // \t tabulacion

//^ variables let
/*tienen un ámbito de bloque, lo que significa que solo están disponibles dentro del bloque en el que se declaran*/
//~ en 2 lineas
let name;
name = "Felipe";
//~ en 1 linea
let last = "Castillo";
let apodo = "Sugo"
console.log("Mi nombre es ",{name}," y me apellido es ",{last}); //impresion de variable
// Comillas lietrales, imprime variables con ${} y permite salto de linea
console.log(`Me llamo ${name} ${last}
mi apodo es '${apodo}'`); 

//^ variables var
/* tienen un ámbito de función o global, lo que significa que están disponibles en todo el ámbito de la función en la que se declaran o en el ámbito global del archivo */
var nombre; nombre = "Felipe"; var apellido = "Castillo";
console.log("Mi nombre es ",{nombre},{apellido},"!");

//^ Variables Const
/* Las const no pueden cambiar su valor despues de que se declaran */
const nickname = "Sugo";
// nickname = "Sugin"

//^ Booleanos
v = true;
f = false;
console.log({v},{f});

x = "5"; y = 5;
console.log(x == y) // operador logico
console.log(x === y) // operador logico estricto

//^ Operaciones Aritmeticas
let = a = 6
let = b = 2
console.log(a+5); // suma
console.log(a+=2) // suma con reasignacion inmediata
console.log(a/b) // 8 / 2 = 4
console.log(a/=b) // 8 / 2 = 4 division con reasignacion inmediata
console.log(4%3); // modulo
console.log(a+b); // suma 2 variables
console.log(b++); // el sufijo ++ (+1) imprime el resultado en la siguiente linea
console.log(b); // le suma +1 en la linea anterior y lo imprime en esta
console.log(++b); // el prefijo ++ (+1) imprime el resultado en la misma linea
console.log(--b); // el prefijo -- (-1) imprime el resultado en la misma linea