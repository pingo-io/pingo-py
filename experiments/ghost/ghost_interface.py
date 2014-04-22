import pingo
import gtk

class MainWindow(gtk.Window):
    def __init__(self, ghost_board):
        gtk.Window.__init__(self)
        self.connect('destroy', gtk.main_quit)
        self.set_title('Pingo GhostBoard.')
        self.set_size_request(480, 320)
        self.set_position(gtk.WIN_POS_CENTER)
        self.set_border_width(1)

        vbox = gtk.VBox()

        hboxes = []
        for i in range(8):
            hboxes.append(gtk.HBox())

        npin = 0
        for hbox in hboxes:
            pack = [
                gtk.Entry(1),
                gtk.Button('ON'),
                gtk.Label(),
                gtk.VSeparator(),
                gtk.Label(),
                gtk.Button('ON'),
                gtk.Entry(1),
            ]
            # Entry
            npin +=1
            pin = ghost_board.pins[npin]
            pack[0].set_width_chars(3)
            if isinstance(pin, pingo.DigitalPin):
                pack[0].set_sensitive(False)
            # Button
            pack[1].set_size_request(40, 20)
            if isinstance(pin, pingo.GroundPin) or \
                isinstance(pin, pingo.VddPin):
                pack[1].set_sensitive(False)
            else:
                label = 'OFF' if pin.state is None else pin.state
                pack[1].set_label(label)
#            pack[1].connect("clicked", foo.bar)
            # Label
            pack[2].set_text(str(pin))

            # Label
            npin +=1
            pin = ghost_board.pins[npin]
            pack[4].set_text(str(pin))
            # Button
            pack[5].set_size_request(40, 20)
            if isinstance(pin, pingo.GroundPin) or \
                isinstance(pin, pingo.VddPin):
                pack[5].set_sensitive(False)
            else:
                label = 'OFF' if pin.state is None else pin.state
                pack[5].set_label(label)
#            pack[5].connect("clicked", foo.bar)
            # Entry
            pack[6].set_width_chars(3)
            if isinstance(pin, pingo.DigitalPin):
                pack[6].set_sensitive(False)

            for widget in pack:
                hbox.pack_start(widget, fill=False)

        hboxes.reverse()
        for box in hboxes:
            vbox.pack_end(box, fill=False)

        self.add(vbox)
        self.show_all()

b = pingo.ghost.GhostBoard()
x = MainWindow(b)
gtk.main()

