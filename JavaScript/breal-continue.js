/*
break : sirve para romper el bucle y salir de la ejecucion
continue : sirve para omitir algo y seguir iterando
*/

// Break - En este caso imprimira 0, 1 y 2, ya que el 3 contiene un break
for(let i=0 ; i<10 ; i++) {
    if( i == 3 ) {
        break;
    }
    console.log(i);
}

// Continue - En este caso imprimira del 0 al 9 y omitira el 5 porque el 5 contiene un continue
for(let i=0 ; i<10 ;i++) {
    if(i == 5) {
        continue;
    }
    console.log(i);
}