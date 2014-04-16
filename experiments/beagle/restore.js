var b = require('bonescript');
var p = '/sys/class/leds/beaglebone:green:usr';
b.digitalWrite('USR0', b.LOW);
b.digitalWrite('USR1', b.LOW);
b.digitalWrite('USR2', b.LOW);
b.digitalWrite('USR3', b.LOW);
resetUSR0();
function resetUSR0() {
    b.writeTextFile(p+'0/trigger', 'heartbeat', resetUSR1);
}
function resetUSR1() {
    b.writeTextFile(p+'1/trigger', 'mmc0', resetUSR2);
}
function resetUSR2() {
    b.writeTextFile(p+'2/trigger', 'cpu0', resetUSR3);
}
function resetUSR3() {
    b.writeTextFile(p+'3/trigger', 'mmc1', complete);
}
function complete() {
}
