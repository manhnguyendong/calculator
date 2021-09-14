from tkinter import *
from tkinter.ttk import *
from tkinter.messagebox import *
import numpy as np
import matplotlib.pyplot as plt

class main_window:
    def __init__(self):
        self.root = Tk()
        self.root.title('Calculator')
        self.root.geometry('600x500')
        self.root.resizable(False, False)
        self.root.tk.call("source", "D:/Test/test/sun-valley.tcl")
        self.root.tk.call("set_theme", "dark")
        self.a = DoubleVar()
        self.b = DoubleVar()
        self.c = DoubleVar()
        # self.enter_value()

    def reset(self):
        self.results = 0
        self.stores = ''
        self.stores_label = Label(self.screen, text='', width=40)
        self.stores_label.grid(column=0, row=0, sticky=W, ipadx=10)

    def reset_button(self):
        self.reset = Button(self.root, text='Reset', command=self.reset)
        self.reset.place(x='500', y='0')


class function:
    def __init__(self):
        self.memory = []

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
            try:
                self.stores_label.grid_forget()
                self.stores_label = Label(self.screen, text='', width=40)
                self.results = eval(self.stores)
                history = self.stores + ' = ' + str(self.results)
                self.stores = str(self.results)
                self.stores_label.config(text='=' + str(self.results))
                print(self.results)
                self.stores_label.grid(column=0, row=0, sticky=E, ipadx=10)
                self.prev_stores = self.stores
                print(history)

            except:
                showwarning(title='Warning', message='Try to enter another operator')
                self.stores_label = Label(self.screen, text='', width=40)
                self.results = 0
                self.stores = ''
                self.stores_label.grid(column=0, row=0, sticky=E, ipadx=10)

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
        if (self.prev_stores != ''):
            if self.results != 0:
                if(len(self.prev_stores) < len(self.stores)):
                    if(self.stores[len(self.prev_stores)] != '+' and self.stores[len(self.prev_stores)] != '-' and self.stores[len(self.prev_stores)] != '*' and self.stores[len(self.prev_stores)] != '/'):
                        self.stores_label = Label(self.screen, text='', width=40)
                        self.stores_label.grid(column=0, row=0, sticky=W, ipadx=10)
                        self.stores = ''
                        self.stores = self.stores + str(x)
                        self.prev_stores = ''
        self.stores_label = Label(self.screen, text=self.stores)
        self.stores_label.grid(column=0, row=0, sticky=W, ipadx=10)
        print(self.stores)

    def calsqrt(self):
        self.stores_label.grid_forget()
        self.stores_label = Label(self.screen, text='', width=40)
        self.results = np.sqrt(eval(self.stores))
        history = 'sqrt' + '(' + self.stores + ')' + ' = ' + str(self.results)
        self.stores = str(self.results)
        self.stores_label.config(text='=' + str(self.results))
        print(self.results)
        self.stores_label.grid(column=0, row=0, sticky=E, ipadx=10)
        self.prev_stores = self.stores
        print(history)

    def cal_sin(self):
        try:
            self.stores_label.grid_forget()
            self.stores_label = Label(self.screen, text='', width=40)
            self.results = np.sin(eval(self.stores))
            history = 'sin'+'(' + self.stores + ')'+ ' = ' + str(self.results)
            self.stores = str(self.results)
            self.stores_label.config(text='=' + str(self.results))
            print(self.results)
            self.stores_label.grid(column=0, row=0, sticky=E, ipadx=10)
            self.prev_stores = self.stores
            print(history)

        except:
            showwarning(title='Warning', message='Try to enter another operator')
            self.stores_label = Label(self.screen, text='', width=40)
            self.results = 0
            self.stores = ''
            self.stores_label.grid(column=0, row=0, sticky=E, ipadx=10)

    def cal_cos(self):
        try:
            self.stores_label.grid_forget()
            self.stores_label = Label(self.screen, text='', width=40)
            self.results = np.cos(eval(self.stores))
            history = 'cos' + '(' + self.stores + ')' + ' = ' + str(self.results)
            self.stores = str(self.results)
            self.stores_label.config(text='=' + str(self.results))
            print(self.results)
            self.stores_label.grid(column=0, row=0, sticky=E, ipadx=10)
            self.prev_stores = self.stores
            print(history)

        except:
            showwarning(title='Warning', message='Try to enter another operator')
            self.stores_label = Label(self.screen, text='', width=40)
            self.results = 0
            self.stores = ''
            self.stores_label.grid(column=0, row=0, sticky=E, ipadx=10)

    def cal_square(self):
        try:
            self.stores_label.grid_forget()
            self.stores_label = Label(self.screen, text='', width=40)
            self.results = eval(self.stores)**2
            history = self.stores + '^2' + ' = ' + str(self.results)
            self.stores = str(self.results)
            self.stores_label.config(text='=' + str(self.results))
            print(self.results)
            self.stores_label.grid(column=0, row=0, sticky=E, ipadx=10)
            self.prev_stores = self.stores
            print(history)

        except:
            showwarning(title='Warning', message='Try to enter another operator')
            self.stores_label = Label(self.screen, text='', width=40)
            self.results = 0
            self.stores = ''
            self.stores_label.grid(column=0, row=0, sticky=E, ipadx=10)

class number_button(main_window, function):
    def __init__(self):
        super().__init__()
        self.stores = ''
        self.prev_stores = ''
        self.results = 0
        self.button_Frame = LabelFrame(self.root, text='Number and Operation')
        self.button_Frame.grid(column=0, row=1)
        self.number_canvas = Canvas(self.button_Frame, width=300, height=500)
        self.number_canvas.grid(column=0, row=0)
        self.screen = LabelFrame(self.root, text='Screen')
        self.screen.grid(column=0, row=0)
        self.canvas = Canvas(self.screen, width=300, height=40)
        self.canvas.grid(column=0, row=1, sticky=N)
        self.special = LabelFrame(self.root, text='Special Operator')
        self.special.grid(column=0, row=2)
        self.special_canvas = Canvas(self.special, width=300, height=100)
        self.special_canvas.grid(column=0, row=0)
        self.graph_show = LabelFrame(self.root, text='Graph option')
        self.graph_show.grid(column=2, row=2)
        self.graph_canvas = Canvas(self.graph_show, width=200, height=250)
        self.graph_canvas.grid(column=1, row=0, sticky=N)

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

    def special_operator(self):
        self._sqrt = Button(self.special_canvas, text='sqrt(x)', command=self.calsqrt)
        self._sqrt.grid(column=0, row=0, pady=(0, 5), ipadx=10, padx=10)
        self._sine = Button(self.special_canvas, text='sin(x)', command=self.cal_sin)
        self._sine.grid(column=1, row=0, pady=(0, 5), ipadx=10, padx=10)
        self._cosine = Button(self.special_canvas, text='cos(x)', command=self.cal_cos)
        self._cosine.grid(column=2, row=0, pady=(0, 5), ipadx=10, padx=10)
        self._square = Button(self.special_canvas, text='x^2', command=self.cal_square)
        self._square.grid(column=0, row=1, pady=(0, 5), ipadx=15, padx=10)

    def graph_option(self):
        self._sinx = Button(self.graph_canvas, text='f(x) = asin(bx)', command=self.plot_sinx)
        self._sinx.grid(column=0, row=0, pady=(0, 10))
        self._cosx = Button(self.graph_canvas, text='f(x) = acos(bx)', command=self.plot_cosx)
        self._cosx.grid(column=1, row=0, pady=(0, 10))
        self._parabol = Button(self.graph_canvas, text='f(x) = ax^2 + bx + c', command=self.plot_parabol)
        self._parabol.grid(column=0, row=1, padx=(20, 0), pady=(0, 5))
        self._exp = Button(self.graph_canvas, text='f(x)=x^a', command=self.plot_exp)
        self._exp.grid(column=1, row=1, pady=(0, 5))
        self.label_A = Label(self.graph_canvas, text='Value a')
        self.label_A.grid(column=0, row=2)
        self.label_A = Label(self.graph_canvas, text='Value b')
        self.label_A.grid(column=0, row=3)
        self.label_A = Label(self.graph_canvas, text='Value c')
        self.label_A.grid(column=0, row=4)
        self.entryA = Entry(self.graph_canvas, textvariable=self.a)
        self.entryA.grid(column=1, row=2)
        self.entryB = Entry(self.graph_canvas, textvariable=self.b)
        self.entryB.grid(column=1, row=3)
        self.entryC = Entry(self.graph_canvas, textvariable=self.c)
        self.entryC.grid(column=1, row=4)
        self.Submit = Button(self.graph_canvas, text='Submit', command=self.submit)
        self.Submit.grid(column=1, row=5)

    def submit(self):
        self.val_a = self.a.get()
        self.val_b = self.b.get()
        self.val_c = self.c.get()
        print(self.val_a, self.val_b, self.val_c)
        self.a.set('')
        self.b.set('')
        self.c.set('')

    def plot_sinx(self):
        x = np.linspace(-5, 5, 100)
        plt.plot(x, self.val_a * np.sin(self.val_b * x))
        plt.show()

    def plot_cosx(self):
        x = np.linspace(-5, 5, 100)
        plt.plot(x, self.val_a * np.cos(self.val_b * x))
        plt.show()

    def plot_parabol(self):
        x = np.linspace(-5, 5, 100)
        plt.plot(x, self.val_a *(x**2) + self.val_b*x + self.val_c)
        plt.show()

    def plot_exp(self):
        x = np.linspace(0, 10, 100)
        plt.plot(x, x**(self.val_a))
        plt.show()
class screen_present(number_button):
    def __init__(self):
        super().__init__()
        self.number()
        self.operator()
        self.reset_button()
        self.special_operator()
        self.graph_option()
        # self.enter_value_button()
def main():
    screen = screen_present()
    mainloop()

if __name__ == "__main__":
    main()
