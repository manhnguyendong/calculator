from tkinter import *
from tkinter.ttk import *

class main_window:
    def __init__(self):
        self.root = Tk()
        self.root.title('Calculator')
        self.root.geometry('500x650')
        self.root.tk.call("source", "D:/Test/test/sun-valley.tcl")
        self.root.tk.call("set_theme", "dark")

class number_button(main_window):
    def __init__(self):
        super().__init__()
        self.stores = ''
        self.display = ''
        self.prev_stores = ''
        self.results = 0
        self.num1 = 0
        self.show = 0
        self.button_Frame = LabelFrame(self.root, text='Number and Operation')
        self.button_Frame.grid(column=0, row=1)
        self.number_canvas = Canvas(self.button_Frame, width=300, height=500)
        self.number_canvas.grid(column=0, row=0)
        self.screen = LabelFrame(self.root, text='Screen')
        self.screen.grid(column=0, row=0)
        self.canvas = Canvas(self.screen, width=300, height=50)
        self.canvas.grid(column=0, row=1)

    def number(self):
        self._no1 = Button(self.number_canvas, text='1', command=lambda: self.print_number('1'))
        self._no1.grid(column=0, row=0, ipadx=10)
        self._no2 = Button(self.number_canvas, text='2', command=lambda: self.print_number('2'))
        self._no2.grid(column=1, row=0, padx=10, ipadx=10)
        self._no3 = Button(self.number_canvas, text='3', command=lambda: self.print_number('3'))
        self._no3.grid(column=2, row=0, padx=10, ipadx=10)
        self._no4 = Button(self.number_canvas, text='4', command=lambda: self.print_number('4'))
        self._no4.grid(column=0, row=1, padx=10, ipadx=10, pady=10)
        self._no5 = Button(self.number_canvas, text='5', command=lambda: self.print_number('5'))
        self._no5.grid(column=1, row=1, padx=10, ipadx=10, pady=10)
        self._no6 = Button(self.number_canvas, text='6', command=lambda: self.print_number('6'))
        self._no6.grid(column=2, row=1, padx=10, ipadx=10, pady=10)
        self._no7 = Button(self.number_canvas, text='7', command=lambda: self.print_number('7'))
        self._no7.grid(column=0, row=2, padx=10, ipadx=10, pady=(0, 10))
        self._no8 = Button(self.number_canvas, text='8', command=lambda: self.print_number('8'))
        self._no8.grid(column=1, row=2, padx=10, ipadx=10, pady=(0, 10))
        self._no9 = Button(self.number_canvas, text='9', command=lambda: self.print_number('9'))
        self._no9.grid(column=2, row=2, padx=10, ipadx=10, pady=(0, 10))
        self._no0 = Button(self.number_canvas, text='0', command=lambda: self.print_number('0'))
        self._no0.grid(column=0, row=3, padx=10, ipadx=10, pady=(0, 10))
        self._dot = Button(self.number_canvas, text='.', command=lambda: self.print_number('.'))
        self._dot.grid(column=1, row=3, padx=10, ipadx=11, pady=(0, 10))


    def operator(self):
        self._add = Button(self.number_canvas, text='+', command=lambda: self.calculate('+'))
        self._add.grid(column=3, row=0, padx=(0, 5), ipadx=25)
        self._minous = Button(self.number_canvas, text='-', command=lambda: self.calculate('-'))
        self._minous.grid(column=3, row=1, padx=(0, 5), ipadx=25)
        self._product = Button(self.number_canvas, text='*', command=lambda: self.calculate('*'))
        self._product.grid(column=3, row=2, padx=(0, 5), ipadx=25, pady=(0, 10))
        self._divide = Button(self.number_canvas, text='/', command=lambda: self.calculate('/'))
        self._divide.grid(column=3, row=3, padx=(0, 5), ipadx=25, pady=(0, 5))
        self._equal = Button(self.number_canvas, text='=', command=lambda: self.calculate('='))
        self._equal.grid(column=2, row=3, padx=10, ipadx=10, pady=(0, 10))

    def print_number(self, x):
        self.stores = self.stores + str(x)
        if self.results != 0:
            if(len(self.prev_stores) < len(self.stores)):
                if(self.stores[len(self.prev_stores)] not in ['+', '-', '*', '/']):
                    self.stores_label = Label(self.screen, text='', width=40)
                    self.stores_label.grid(column=0, row=0, sticky=W, ipadx=10)
                    self.stores = ''
                    self.stores = self.stores + str(x)
        self.stores_label = Label(self.screen, text=self.stores)
        self.stores_label.grid(column=0, row=0, sticky=W, ipadx=10)
        print(self.stores)


    def checkOperator(self, x):
        if(str(self.stores).find(x) != -1):
            return True
        else:
            return False

    def calculate(self, x):
        if (x == '+'):
            if (self.results == 0):
                self.stores = self.stores + '+'
                self.stores_label.config(text=self.stores)
                self.stores_label.grid(column=0, row=0, sticky=W, ipadx=10)
            else:
                self.stores = self.stores + '+'
                self.stores_label.config(text=self.stores)
                self.stores_label.grid(column=0, row=0, sticky=W, ipadx=10)
        if (x == '-'):
            if (self.results == 0):
                self.stores = '-'
                self.stores_label.config(text='-')
                self.stores_label.grid(column=0, row=0, sticky=W, ipadx=10)
            else:
                self.stores = (str(self.results) + '-')
                self.stores_label.config(text=self.stores)
                self.stores_label.grid(column=0, row=0, sticky=W, ipadx=10)
        if(x == '*'):
            self.stores = self.stores + '*'
            self.stores_label.config(text=self.stores)
            self.stores_label.grid(column=0, row=0, sticky=W, ipadx=10)

        if(x == '/'):
            self.stores = self.stores + '/'
            self.stores_label.config(text=self.stores)
            self.stores_label.grid(column=0, row=0, sticky=W, ipadx=10)
        if (x == '='):
            self.stores_label.grid_forget()
            self.stores_label = Label(self.screen, text='', width=40)
            self.results = eval(self.stores)
            self.stores = str(self.results)
            self.stores_label.config(text='=' + str(self.results))
            print(self.results)
            self.stores_label.grid(column=0, row=0, sticky=E, ipadx=10)
            self.prev_stores = self.stores


class screen_present(number_button):
    def __init__(self):
        super().__init__()
        self.number()
        self.operator()

def main():
    screen = screen_present()
    mainloop()


if __name__ == "__main__":
    main()

