from text_scrollbar import *
from fact_giver import *

class Fact_UI(tk.Frame):

    def __init__(self):
        self.root = tk.Tk()
        self.init_components()
        self.install_components()
        self.root.mainloop()

    def init_components(self):
        self.root.title('Random Facts')
        self.root.geometry('500x200')
        self.factLabel = tk.Label(self.root, text='Random Facts', font=('Arial', 15))

        self.factDisplay = Text_ScrollBar(self.root)

        self.factButton = ttk.Button(self.root, text='Get Facts', command=self.insert_fact)

        self.fact_giver = Fact_giver()

    def install_components(self):
        self.factLabel.pack(side=tk.TOP, padx=5, pady=5)
        self.factDisplay.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.BOTH, expand=True)
        self.factButton.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

    def set_text(self, txt):
        self.factDisplay.text = txt

    def insert_fact(self):
        fact = self.fact_giver.fact()
        self.set_text(fact)



if __name__ == '__main__':
    UI = Fact_UI()