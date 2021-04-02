import tkinter as tk
import tkinter_objects as obj

class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.length, self.height = 1200, 800
        self.x, self.y = 10, 10
        self.title("Morse Traductor 3000")
        self.configure(bg='light blue')
        self.geometry(f'{self.length}x{self.height}+{self.x}+{self.y}')
        self.inputs = [obj.Tkinter_Input(self, i) for i in range(1)]
        self.labels = [obj.Tkinter_Label(self, i) for i in range(1)]
        self.objects = [self.inputs, self.labels]
        self.bind('<Escape>', self.kill)
        self.place_all_objects()
        self.update()

    def kill(*args):
        self = args[0]
        self.destroy()

    def place_all_objects(*args):
        self = args[0]
        for list in self.objects:
            for object in list:
                object.place(x=object.x, y=object.y)
