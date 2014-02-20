var b = require('bonescript');
var exibir = function exibir(p) {
  console.log(p.value);
};
var ler = function ler() {
  b.analogRead('P9_39', exibir);
};
var timer = setInterval(ler, 50);
var parar = function parar() {
  clearInterval(timer);
};

setTimeout(parar, 10000);

