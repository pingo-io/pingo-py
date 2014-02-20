var b = require('bonescript');
var pinos = [11, 12, 13, 14, 15, 16, 21, 22];
for (var i=0; i<pinos.length; i++ ) {
  var p = pinos[i];
  console.log(p);
  var pin = "P9_" + p;
  b.pinMode(pin, b.OUTPUT);
  b.digitalWrite(pin, 1);
}
