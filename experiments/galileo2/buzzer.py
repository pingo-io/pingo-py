import pyupm_buzzer as buzzer

notes = [buzzer.DO, buzzer.RE, buzzer.MI, buzzer.FA,
         buzzer.SOL, buzzer.LA, buzzer.SI]

buz = buzzer.Buzzer(5)

for x in range(0, 7):
   buz.playSound(notes[x], 1000000)
