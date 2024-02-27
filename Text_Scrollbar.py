import tkinter
import tkinter as tk
from tkinter import ttk


class Text_ScrollBar(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_components()
        self.install_component()

    def init_components(self):
        self.textwidget = tk.Text(self, height=5, width=10)
        self.scrollBar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.textwidget.yview)
        self.text = 'Default Text'

    def install_component(self):
        self.textwidget.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollBar.pack(side=tk.RIGHT, fill=tk.Y)

    @property
    def text(self):
        return self.textwidget.get()

    @text.setter
    def text(self, txt):
        self.textwidget['state'] = tk.NORMAL
        self.textwidget.delete('1.0', tk.END)
        self.textwidget.insert(tk.END, txt)
        self.textwidget['state'] = tk.DISABLED