# Troubleshooting

## Board Auto Discovery Failed!, Shutting Down
If anyone is facing some error like this:
```
Please wait while Arduino is being detected. This can take up to 30 seconds ...
Board Auto Discovery Failed!, Shutting Down
```

Please, upload the StandardFirmata.ino sketch.
It can be found on Arduino >> Examples >> Firmata >> StandardFirmata
* https://github.com/firmata/arduino/blob/master/examples/StandardFirmata/StandardFirmata.ino
* https://www.arduino.cc/en/Reference/Firmata


## Arduino IDE errors
If anyone is facing some error like this:
```
$ arduino
java.lang.UnsatisfiedLinkError: no rxtxSerial in java.library.path thrown while loading gnu.io.RXTXCommDriver
Exception in thread "main" java.lang.UnsatisfiedLinkError: no rxtxSerial in java.library.path
	at java.lang.ClassLoader.loadLibrary(ClassLoader.java:1681)
	at java.lang.Runtime.loadLibrary0(Runtime.java:840)
	at java.lang.System.loadLibrary(System.java:1047)
	at gnu.io.CommPortIdentifier.<clinit>(CommPortIdentifier.java:123)
	at processing.app.Editor.populateSerialMenu(Editor.java:962)
	at processing.app.Editor.buildToolsMenu(Editor.java:691)
	at processing.app.Editor.buildMenuBar(Editor.java:476)
	at processing.app.Editor.<init>(Editor.java:205)
	at processing.app.Base.handleOpen(Base.java:704)
	at processing.app.Base.handleOpen(Base.java:669)
	at processing.app.Base.handleNew(Base.java:565)
	at processing.app.Base.<init>(Base.java:305)
	at processing.app.Base.main(Base.java:194)
```
The fix is this:
```
$ sudo ln -s /usr/lib/jni/librxtxSerial-2.2pre1.so /usr/lib/jni/librxtxSerial.so
```
PS: I'm running here a CrunchBang 11. But Debian/Ubuntu/Mint user may have this problem too.
