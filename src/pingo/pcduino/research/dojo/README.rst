============
Notas
============

---------------------
Sistema pre-instalado
---------------------

PCduino veio com algo parecido com o Lubuntu 12.07. Veja o resultado de 
``lsb_release -a`` ::

	$ lsb_release -a
	No LSB modules are available.
	Distributor ID:	Linaro
	Description:	Linaro 12.07
	Release:	12.07
	Codename:	precise

Este comando e' o mais recomendado para identificar a versao das
distribuicoes GNU/Linux derivadas de Debian, como Ubuntu, Lubuntu etc.

Linaro e' uma organizacao que porta pacotes Linux para CPUs ARM.

--------------------
Python pre-instalado
--------------------

Python 2.7.3 de 32 bits veio instalado. Instalei o pacote ``python-tk`` 
e conferi que o Tkinter funciona rodando o script ``garoa/relogio.py``.

----------------------------------------------
Instalacao de pacotes do GNU/Linux
----------------------------------------------

Para instalar pacotes, use o comando ``sudo apt-get install X`` onde X 
e' o nome do pacote.

Por exemplo, para instalar o tree::

	$ sudo apt-get install tree

No primeiro dia de uso do PCDuino, instalei::

- openssh-client (cliente para conexao ssh)
- scrot (capturador de tela acionado via tecla PrintScreen)
- git (controle de versao de codigo)
- tree (visualizacao de uma arvore de diretorios no console)
- geany (editor para programacao)
- python-tk (biblioteca grafica Tkinter para o Python 2.7.3)

-------------------
Espaco disponivel
-------------------

Ao final da instalacao inicial restam 478MB na armazenagem NAND::

	$ df -h
	Filesystem      Size  Used Avail Use% Mounted on
	/dev/nandd      1.5G  925M  478M  66% /
	none            405M  4.0K  405M   1% /dev
	none            408M  284K  408M   1% /tmp
	none             82M  240K   82M   1% /run
	none            5.0M     0  5.0M   0% /run/lock
	none            408M  144K  408M   1% /run/shm
	none            408M   96K  408M   1% /var/tmp
