from text_scrollbar import *
from fact_giver import *

class Fact_UI(tk.Frame):

    def __init__(self, root):
        super().__init__(root)
        self.root = root
        self.grid_config()
        self.init_components()
        self.install_components()
        self.root.mainloop()

    def grid_config(self):
        self.root.rowconfigure(0, weight=1, uniform=1)
        self.root.rowconfigure(1, weight=5, uniform=1)
        self.root.rowconfigure(2, weight=1, uniform=1)

        self.root.columnconfigure(0, weight=1, uniform=1)

    def init_components(self):
        self.root.title('Random Facts')
        self.root.geometry('600x300')
        self.factLabel = tk.Label(self.root, text='Random Facts', font=('Arial', 15))

        self.factDisplay = Text_ScrollBar(self.root)

        self.factButton = ttk.Button(self.root, text='Get Facts', command=self.insert_fact)

        self.fact_giver = Fact_giver()

    def install_components(self):
        self.factLabel.grid(row=0, column=0, padx=5, pady=5, sticky=tk.NSEW)
        self.factDisplay.grid(row=1, column=0, padx=5, pady=5, sticky=tk.NSEW)
        self.factButton.grid(row=2, column=0, padx=5, pady=5, sticky=tk.NSEW)

    def set_text(self, txt):
        self.factDisplay.text = txt

    def insert_fact(self):
        fact = self.fact_giver.fact()
        self.set_text(fact)



if __name__ == '__main__':
    root = tk.Tk()
    UI = Fact_UI(root)