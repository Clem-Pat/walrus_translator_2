import tkinter as tk

alphabet = {
		"0": ["-----"],
		" ": [""],
		"1": [".----"],
		"2": ["..---"],
		"3": ["...--"],
		"4": ["....-"],
		"5": ["....."],
		"6": ["-...."],
		"7": ["--..."],
		"8": ["---.."],
		"9": ["----."],
		"!": ["-.-.--"],
		",": ["--..--"],
		".": [".-.-.-"],
		"a": [".-"],
		"b": ["-..."],
		"c": ["-.-."],
		"d": ["-.."],
		"e": ["."],
		"f": ["..-."],
		"g": ["--."],
		"h": ["...."],
		"i": [".."],
		"j": [".---"],
		"k": ["-.-"],
		"l": [".-.."],
		"m": ["--"],
		"n": ["-."],
		"o": ["---"],
		"p": [".--."],
		"q": ["--.-"],
		"r": [".-."],
		"s": ["..."],
		"t": ["-"],
		"u": ["..-"],
		"v": ["...-"],
		"w": [".--"],
		"x": ["-..-"],
		"y": ["-.--"],
		"z": ["--.."]}

class Tkinter_Input(tk.Entry):

    def __init__(self, app, id):
        tk.Entry.__init__(self, app)
        self.id, self.app = id, app
        if self.id == 0:
            self.x, self.y = 30, 50
            self.config(width=30, font='Arial 12', fg='grey')
            self.insert(0, 'Ecrire le message en français ici')
            self.bind('<Button-1>', self.clear)
            self.bind_all('<Key>', self.update)

    def clear(*args):
        self = args[0]
        self.delete(0, tk.END)
        label=self.app.labels[0]
        label.text=''
        label.config(text=label.text)

    def update(*args):
        self = args[0]
        self.config(fg='black')
        value = str(self.get())
        label = self.app.labels[0]
        label.text = ''
        for caracter in value:
            label.text += alphabet[caracter][0] + '/'
        label.config(text=label.text)


class Tkinter_Label(tk.Label):

    def __init__(self, app, id):
        tk.Label.__init__(self, app)
        self.id, self.app = id, app
        if self.id == 0:
            self.x, self.y = 30, 100
            self.text = "Le message en morse s'affiche ici"
            self.config(text=self.text, font='Arial 12', bg='light blue')
