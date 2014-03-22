var b = require('bonescript');
b.pinMode('USR0', b.OUTPUT);
b.pinMode('USR1', b.OUTPUT);
b.pinMode('USR2', b.OUTPUT);
b.pinMode('USR3', b.OUTPUT);

function liga() {
  b.digitalWrite('USR0', b.HIGH);
  b.digitalWrite('USR1', b.HIGH);
  b.digitalWrite('USR2', b.HIGH);
  b.digitalWrite('USR3', b.HIGH);
}

function desliga() {
  b.digitalWrite('USR0', b.LOW);
  b.digitalWrite('USR1', b.LOW);
  b.digitalWrite('USR2', b.LOW);
  b.digitalWrite('USR3', b.LOW);
}
liga();
setTimeout(desliga, 1000);
setTimeout(liga, 2000);
setTimeout(desliga, 3000);
setTimeout(liga, 4000);
setTimeout(desliga, 5000);
console.log('FIM');



