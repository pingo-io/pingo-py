try:
    import Tkinter
    import ttk
except:
    import tkinter as Tkinter

from Tkinter import N, S, W, E


class PinFrame(object):
    def __init__(self, root):
        _frame = ttk.Frame(root, padding="3 3 12 12")
        _frame.columnconfigure(0, weight=1)
        _frame.rowconfigure(0, weight=1)
        self.frame = _frame


class VddGndFrame(PinFrame):
    def __init__(self, root, volage):
        super(VddGndFrame, self).__init__(root)
        label = "VDD Pin %dV" % volage
        ttk.Label(self.frame, text=label).grid(column=0, row=0, sticky=W)


class GpioFrame(PinFrame):
    def __init__(self, root):
        super(GpioFrame, self).__init__(root)

        _state = Tkinter.StringVar()
        _state.set("0")
        self.state = _state

        _mode = Tkinter.StringVar()
        _mode.set("OUTPUT")
        self.mode = _mode

        self.box = ttk.Combobox(self.frame, textvariable=self.mode)
        self.box['values'] = ('OUTPUT', 'INPUT')
        self.box.current(0)
        self.box.bind("<<ComboboxSelected>>", self._change_mode)
        self.box.grid(column=5, row=0, sticky=E)
        # Implement on subclass
        #self.pin_widget = None


    def _change_mode(self, *args):
        _mode = self.mode.get()
        if _mode == "INPUT":
            self.mode.set("INPUT")
            self.pin_widget.configure(state='normal')
        else:
            self.mode.set("OUTPUT")
            self.state.set("1")
            self.pin_widget.configure(state='disabled')


class DigitalGuiFrame(GpioFrame):
    def __init__(self, root):
        super(DigitalGuiFrame, self).__init__(root)
        ttk.Label(self.frame, text="DigitalPin X").grid(column=0, row=0, sticky=W)
        self.pin_widget = Tkinter.Checkbutton(self.frame,
            variable=self.state)
        self.pin_widget.configure(state='disabled')
        self.pin_widget.grid(column=2, row=0, sticky="")
        ttk.Label(self.frame, textvariable=self.state).grid(column=1, row=0, sticky=W)


class AnalogGuiFrame(GpioFrame):
    def __init__(self, root):
        super(AnalogGuiFrame, self).__init__(root)
        ttk.Label(self.frame, text="AnalogPin X").grid(column=0, row=0, sticky=W)
        self.pin_widget = Tkinter.Scale(self.frame, from_=0, to=100,
                orient=Tkinter.HORIZONTAL)
        self.pin_widget.configure(state='disabled')
        self.pin_widget.grid(column=2, row=0, sticky=(W, E))


class pinGUIm(object):

    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.title("pingo :: pinGUIm")
        self.root.geometry("390x240")

        vf = VddGndFrame(self.root, 5)
        df = DigitalGuiFrame(self.root)
        af = AnalogGuiFrame(self.root)

        df.frame.grid(column=0, row=0, sticky=(N, W, E, S), padx=15, pady=15)
        af.frame.grid(column=0, row=1, sticky=(N, W, E, S), padx=15, pady=0)
        vf.frame.grid(column=0, row=2, sticky=(N, W, E, S), padx=15, pady=15)


gui = pinGUIm()
gui.root.mainloop()
