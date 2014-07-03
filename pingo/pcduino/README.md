# Troubleshooting

## pcDuino V1:

### Boot
If the board does not show any image on the monitor, right after the power
cable is plugged, you should wait about 2:30 minutes. If it's taking
longer then 3 minutes, your board has a tilt.

### Power Supply
pcDuino V1 draw many mA (I don't know the exact figure). Try to use a higher
power PSU. If a low current power supply is used, pcDuino might not boot or
freeze after some time. A 2000mA PSU is recommended.

Other solution is a USB Hub with with its own power source, and plug the
keyboard and mouse there.

### Wire Network
The correct /etc/network/interfaces configuration:
```
auto lo
iface lo inet loopback
```
Notice that NO eth0 interface is used.

On /etc/NetworkManager/NetworkManager.conf set:
```
[ifupdown]
managed=true
```

Then restart the service:
```
sudo service network-manager restart
```
