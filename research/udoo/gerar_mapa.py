
pinos = {}

with open('pin_map.txt') as entrada:
    for linha in entrada:
        if linha.startswith('#'):
            continue
        arduino, gpio = linha.split()
        pinos[int(arduino)] = int(gpio)
        
#print pinos
if sorted(pinos) == range(0, 54):
    print 'pinos digitais do Arduino Due 0 a 53 completamente mapeados'
else:
    print 'falta algum pino do Arduino Due'
    
for arduino, udoo in sorted(pinos.items()):
    print '%s,' % udoo,
