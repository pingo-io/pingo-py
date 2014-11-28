import mraa

pot = mraa.Aio(0)
while 1:
	print pot.read()

